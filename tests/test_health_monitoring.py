import unittest
import time
from datetime import datetime
from app import app, db, User, DailyHealthRecord

class TestHealthMonitoring(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.athlete = User(
            full_name="Athlete HealthTest",
            email=f"athlete_health_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Basketball",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
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

    def test_health_monitoring_page_loads(self):
        """Verify daily-monitoring form page loads."""
        self._login()
        res = self.client.get('/daily-monitoring')
        self.assertEqual(res.status_code, 200)

    def test_valid_health_record_submission(self):
        """Verify submitting valid daily health parameters persists to MySQL DB."""
        self._login()
        payload = {
            'sleep_hours': 8.0,
            'training_hours': 2.5,
            'resting_heart_rate': 62,
            'fatigue_level': 3,
            'stress_level': 2,
            'previous_injury': False,
            'injury_details': ''
        }
        res = self.client.post('/api/predictions/predict', json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')

        today_str = datetime.utcnow().strftime('%Y-%m-%d')
        rec = DailyHealthRecord.query.filter_by(user_id=self.athlete.id, record_date=today_str).first()
        self.assertIsNotNone(rec)
        self.assertEqual(rec.sleep_hours, 8.0)
        self.assertEqual(rec.resting_heart_rate, 62)

    def test_invalid_health_values_rejected(self):
        """Verify out-of-bounds health metrics (sleep > 12h, negative resting HR) are rejected."""
        self._login()
        res1 = self.client.post('/api/predictions/predict', json={'sleep_hours': 25.0})
        self.assertEqual(res1.status_code, 400)
        
        res2 = self.client.post('/api/predictions/predict', json={'resting_heart_rate': 250})
        self.assertEqual(res2.status_code, 400)

if __name__ == '__main__':
    unittest.main()
