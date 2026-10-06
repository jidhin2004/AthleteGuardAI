import unittest
import time
from datetime import datetime
from app import app, db, User, DailyHealthRecord

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.athlete = User(
            full_name="Athlete DashTest",
            email=f"athlete_dash_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Track",
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

    def test_dashboard_page_rendering(self):
        """Verify dashboard HTML page loads for logged in athlete."""
        self._login()
        res = self.client.get('/dashboard')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Athlete DashTest", res.data)

    def test_dashboard_api_empty_state(self):
        """Verify dashboard API handles new user with zero predictions gracefully."""
        self._login()
        res = self.client.get('/api/dashboard-data')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertFalse(data['has_predictions'])

    def test_dashboard_api_populated_state(self):
        """Verify dashboard API calculates metrics and chart series when records exist."""
        rec = DailyHealthRecord(
            user_id=self.athlete.id,
            record_date="2026-09-01",
            sleep_hours=8.0,
            training_hours=2.0,
            resting_heart_rate=65,
            fatigue_level=2,
            stress_level=2,
            risk_score=15.5,
            risk_label="Low Risk"
        )
        db.session.add(rec)
        db.session.commit()

        self._login()
        res = self.client.get('/api/dashboard-data')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['has_predictions'])
        self.assertEqual(data['stats']['total_predictions'], 1)
        self.assertEqual(data['stats']['injury_risk_percent'], 15.5)

if __name__ == '__main__':
    unittest.main()
