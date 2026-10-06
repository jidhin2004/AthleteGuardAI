import unittest
import time
from datetime import datetime
from app import app, db, User, DailyHealthRecord
from services.ml_service import ml_service

class TestPrediction(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.athlete = User(
            full_name="Athlete MLPredict",
            email=f"athlete_ml_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Swimming",
            _legacy_age=22,
            date_of_birth=datetime(2004, 1, 1).date(),
            role="athlete"
        )
        self.athlete.set_password("Password123!")
        db.session.add(self.athlete)
        db.session.commit()

    def tearDown(self):
        DailyHealthRecord.query.filter_by(user_id=self.athlete.id).delete()
        User.query.filter_by(id=self.athlete.id).delete()
        db.session.commit()
        self.app_context.pop()

    def _login(self):
        return self.client.post('/login', data={'email': self.athlete.email, 'password': 'Password123!'})

    def test_ml_service_direct_prediction(self):
        """Verify direct ml_service execution produces score (0-100%) and valid risk label."""
        pred = ml_service.predict_injury_risk(
            sleep_hours=8.0,
            training_hours=2.0,
            resting_heart_rate=60,
            fatigue_level=2,
            stress_level=2,
            previous_injury=False
        )
        self.assertIn('risk_score', pred)
        self.assertIn('risk_label', pred)
        self.assertGreaterEqual(pred['risk_score'], 0.0)
        self.assertLessEqual(pred['risk_score'], 100.0)
        self.assertIn(pred['risk_label'], ['Low Risk', 'Moderate Risk', 'High Risk'])

    def test_high_workload_prediction_escalation(self):
        """Verify high fatigue, high training hours, and previous injury result in elevated risk score."""
        low_risk_pred = ml_service.predict_injury_risk(
            sleep_hours=9.0, training_hours=1.0, resting_heart_rate=55,
            fatigue_level=1, stress_level=1, previous_injury=False
        )
        high_risk_pred = ml_service.predict_injury_risk(
            sleep_hours=4.0, training_hours=6.0, resting_heart_rate=95,
            fatigue_level=9, stress_level=9, previous_injury=True
        )
        self.assertGreater(high_risk_pred['risk_score'], low_risk_pred['risk_score'])

    def test_prediction_saved_to_history(self):
        """Verify submitting health monitoring saves prediction and displays in prediction history API."""
        self._login()
        payload = {
            'sleep_hours': 7.5,
            'training_hours': 3.0,
            'resting_heart_rate': 68,
            'fatigue_level': 4,
            'stress_level': 3,
            'previous_injury': False
        }
        res_pred = self.client.post('/api/predictions/predict', json=payload)
        self.assertEqual(res_pred.status_code, 200)

        res_hist = self.client.get('/api/predictions/history')
        self.assertEqual(res_hist.status_code, 200)
        data = res_hist.get_json()
        self.assertGreaterEqual(len(data['history']), 1)
        self.assertIsNotNone(data['history'][0]['risk_score'])

if __name__ == '__main__':
    unittest.main()
