import os
import json
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

def train_and_save_model():
    print("==================================================")
    print("ATHLETEGUARD AI — RANDOM FOREST MODEL TRAINING")
    print("==================================================")

    np.random.seed(42)
    n_samples = 1500

    # 1. Generate Synthetic Sports Biomechanics Dataset
    sleep = np.random.uniform(4.0, 10.0, n_samples)          # Sleep hours (4 - 10)
    training = np.random.uniform(0.5, 6.0, n_samples)       # Training hours (0.5 - 6.0)
    rhr = np.random.uniform(45.0, 95.0, n_samples)           # Resting HR (45 - 95 BPM)
    fatigue = np.random.randint(1, 11, n_samples)            # Fatigue (1 - 10)
    stress = np.random.randint(1, 11, n_samples)             # Stress (1 - 10)
    prev_inj = np.random.choice([0, 1], n_samples, p=[0.7, 0.3]) # History (0/1)

    X = np.column_stack([sleep, training, rhr, fatigue, stress, prev_inj])

    # 2. Balanced Multi-Factor Risk Index Calculation
    risk_index = (
        np.maximum(0, (8.0 - sleep)) * 3.5 +
        np.maximum(0, (training - 2.0)) * 4.0 +
        np.maximum(0, (rhr - 60.0)) * 0.3 +
        fatigue * 2.5 +
        stress * 2.0 +
        prev_inj * 12.0
    )

    y = np.zeros(n_samples, dtype=int)
    y[risk_index >= 32.0] = 1  # Medium Risk
    y[risk_index >= 52.0] = 2  # High Risk

    # Print Class Distribution
    classes, counts = np.unique(y, return_counts=True)
    print("\n1. DATASET GENERATION:")
    print(f"Total Samples: {n_samples}")
    for cls, count in zip(classes, counts):
        label = "Low Risk (0)" if cls == 0 else ("Medium Risk (1)" if cls == 1 else "High Risk (2)")
        print(f" - {label}: {count} samples ({count / n_samples * 100:.1f}%)")

    # 3. Train/Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n2. TRAIN / TEST SPLIT:")
    print(f" - Training Set: {X_train.shape[0]} samples")
    print(f" - Testing Set: {X_test.shape[0]} samples")

    # 4. Train Random Forest Classifier
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    rf_model.fit(X_train, y_train)
    print("\n3. MODEL TRAINING:")
    print(" - Model: RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)")
    print(" - Status: Training Completed Successfully.")

    # 5. Evaluate Performance Metrics on Test Set
    y_pred = rf_model.predict(X_test)
    
    acc = float(accuracy_score(y_test, y_pred))
    prec = float(precision_score(y_test, y_pred, average='weighted'))
    rec = float(recall_score(y_test, y_pred, average='weighted'))
    f1 = float(f1_score(y_test, y_pred, average='weighted'))
    cm = confusion_matrix(y_test, y_pred).tolist()

    print("\n4. EVALUATION METRICS:")
    print(f" - Accuracy:  {acc * 100:.2f}%")
    print(f" - Precision: {prec * 100:.2f}%")
    print(f" - Recall:    {rec * 100:.2f}%")
    print(f" - F1-Score:  {f1 * 100:.2f}%")

    print("\n5. CONFUSION MATRIX:")
    print("           Pred Low  Pred Med  Pred High")
    print(f"True Low:   {cm[0][0]:<9} {cm[0][1]:<9} {cm[0][2]:<9}")
    print(f"True Med:   {cm[1][0]:<9} {cm[1][1]:<9} {cm[1][2]:<9}")
    print(f"True High:  {cm[2][0]:<9} {cm[2][1]:<9} {cm[2][2]:<9}")

    print("\nCLASSIFICATION REPORT:")
    print(classification_report(y_test, y_pred, target_names=['Low Risk', 'Medium Risk', 'High Risk']))

    # 6. Serialize Trained Model and Metrics Artifacts
    output_dir = os.path.join(os.path.dirname(__file__), 'models')
    os.makedirs(output_dir, exist_ok=True)

    model_filepath = os.path.join(output_dir, 'athleteguard_rf_model.joblib')
    metrics_filepath = os.path.join(output_dir, 'model_metrics.json')

    joblib.dump(rf_model, model_filepath)
    
    metrics_data = {
        'accuracy': acc,
        'precision': prec,
        'recall': rec,
        'f1_score': f1,
        'confusion_matrix': cm,
        'total_samples': n_samples,
        'train_samples': X_train.shape[0],
        'test_samples': X_test.shape[0]
    }

    with open(metrics_filepath, 'w') as f:
        json.dump(metrics_data, f, indent=2)

    print("\n6. MODEL SERIALIZATION:")
    print(f" - Model saved to: {model_filepath}")
    print(f" - Metrics saved to: {metrics_filepath}")
    print("\n==================================================")
    print("TRAINING PIPELINE EXECUTED SUCCESSFULLY!")
    print("==================================================")

if __name__ == '__main__':
    train_and_save_model()
