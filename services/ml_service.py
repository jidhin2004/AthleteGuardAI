import os
import numpy as np

try:
    from sklearn.ensemble import RandomForestClassifier
    import joblib
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False


class RandomForestInjuryPredictor:
    """
    Random Forest Machine Learning Service for Sports Injury Prediction.
    Evaluates athlete daily health parameters and computes explainable injury risk scores.
    """

    def __init__(self):
        self.sklearn_available = SKLEARN_AVAILABLE
        self.model = None
        self.is_loaded_from_disk = False

        if self.sklearn_available:
            self._load_or_train_model()

    def _load_or_train_model(self):
        """Loads serialized model from disk if available, otherwise trains baseline model."""
        model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'athleteguard_rf_model.joblib')
        model_path = os.path.abspath(model_path)

        if os.path.exists(model_path):
            try:
                self.model = joblib.load(model_path)
                self.is_loaded_from_disk = True
                print(f"[ML Service] Successfully loaded pre-trained Random Forest model from {model_path}")
                return
            except Exception as e:
                print(f"[ML Service] Failed to load model file ({e}). Re-training model...")

        # Fallback to dynamic training if model file is missing
        self._train_baseline_model()

    def _train_baseline_model(self):
        """Train Random Forest model on balanced synthetic dataset."""
        try:
            np.random.seed(42)
            n_samples = 1500

            sleep = np.random.uniform(4.0, 10.0, n_samples)
            training = np.random.uniform(0.5, 6.0, n_samples)
            rhr = np.random.uniform(45.0, 95.0, n_samples)
            fatigue = np.random.randint(1, 11, n_samples)
            stress = np.random.randint(1, 11, n_samples)
            prev_inj = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])

            X = np.column_stack([sleep, training, rhr, fatigue, stress, prev_inj])

            risk_index = (
                np.maximum(0, (8.0 - sleep)) * 3.5 +
                np.maximum(0, (training - 2.0)) * 4.0 +
                np.maximum(0, (rhr - 60.0)) * 0.3 +
                fatigue * 2.5 +
                stress * 2.0 +
                prev_inj * 12.0
            )

            y = np.zeros(n_samples, dtype=int)
            y[risk_index >= 32.0] = 1
            y[risk_index >= 52.0] = 2

            self.model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
            self.model.fit(X, y)
            print("[ML Service] Trained balanced baseline Random Forest model in memory.")
        except Exception as e:
            print(f"[ML Service] Error training model: {e}")
            self.sklearn_available = False

    def predict_injury_risk(self, sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury):
        """
        Calculates explicit injury risk score percentage (0-100%) and risk classification.
        """
        prev_inj_val = 1 if previous_injury else 0

        if self.sklearn_available and self.model is not None:
            try:
                input_features = np.array([[sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, prev_inj_val]])
                probabilities = self.model.predict_proba(input_features)[0]
                
                p_low = probabilities[0] if len(probabilities) > 0 else 0.0
                p_med = probabilities[1] if len(probabilities) > 1 else 0.0
                p_high = probabilities[2] if len(probabilities) > 2 else 0.0

                weighted_risk_percent = (p_low * 12.0 + p_med * 45.0 + p_high * 88.0)
            except Exception as e:
                print(f"[ML Service] Prediction calculation error ({e}). Using fallback.")
                weighted_risk_percent = self._fallback_calc(sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury)
        else:
            weighted_risk_percent = self._fallback_calc(sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury)

        # Boundary adjustments for safety
        if fatigue_level >= 8 or stress_level >= 8 or (previous_injury and training_hours >= 4.0):
            weighted_risk_percent = max(weighted_risk_percent, 58.0)

        if sleep_hours >= 7.5 and fatigue_level <= 5 and stress_level <= 4 and not previous_injury and training_hours <= 3.5:
            weighted_risk_percent = min(weighted_risk_percent, 28.0)

        risk_score = round(float(np.clip(weighted_risk_percent, 10.0, 95.0)), 1)

        if risk_score < 30.0:
            risk_label = "Low Risk"
            badge_color = "success"
        elif risk_score < 60.0:
            risk_label = "Medium Risk"
            badge_color = "warning"
        else:
            risk_label = "High Risk"
            badge_color = "danger"

        factors = []
        if sleep_hours < 7.0:
            factors.append(f"Suboptimal sleep duration ({sleep_hours} hrs, recommended 7–9 hrs)")
        if training_hours >= 4.0:
            factors.append(f"High training duration ({training_hours} hrs)")
        if fatigue_level >= 6:
            factors.append(f"Elevated fatigue score ({fatigue_level}/10)")
        if stress_level >= 6:
            factors.append(f"High stress level ({stress_level}/10)")
        if resting_heart_rate >= 75:
            factors.append(f"Elevated resting heart rate ({resting_heart_rate} BPM)")
        if previous_injury:
            factors.append("History of previous sports injuries")

        if not factors:
            factors.append("Balanced recovery, sleep, and workload metrics")

        recommendations = []
        if sleep_hours < 7.0:
            recommendations.append("Prioritize 8+ hours of nighttime sleep for optimal muscle recovery.")
        if fatigue_level >= 6 or training_hours >= 4.0:
            recommendations.append("Consider incorporating active recovery or reducing high-intensity training load tomorrow.")
        if stress_level >= 6:
            recommendations.append("Perform breathwork or guided relaxation to reduce physiological stress.")
        if not recommendations:
            recommendations.append("Maintain current training load and healthy recovery protocols.")

        return {
            'risk_score': risk_score,
            'risk_label': risk_label,
            'badge_color': badge_color,
            'contributing_factors': factors,
            'recommendations': recommendations
        }

    def _fallback_calc(self, sleep, training, rhr, fatigue, stress, prev_inj):
        score = 15.0
        score += max(0, (7.5 - sleep) * 5.0)
        score += max(0, (training - 2.5) * 6.0)
        score += max(0, (rhr - 65) * 0.5)
        score += fatigue * 2.5
        score += stress * 2.0
        if prev_inj:
            score += 12.0
        return score


ml_service = RandomForestInjuryPredictor()
