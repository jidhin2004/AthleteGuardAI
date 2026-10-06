import unittest
import time
from datetime import datetime, timedelta
from app import app, db, User, DailyHealthRecord

class TestSummaries(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.athlete_a = User(
            full_name="Athlete Summary A",
            email=f"athlete_sum_a_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        self.athlete_a.set_password("Password123!")

        self.athlete_b = User(
            full_name="Athlete Summary B",
            email=f"athlete_sum_b_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Tennis",
            _legacy_age=24,
            date_of_birth=datetime(2002, 1, 1).date(),
            role="athlete"
        )
        self.athlete_b.set_password("Password123!")

        db.session.add(self.athlete_a)
        db.session.add(self.athlete_b)
        db.session.commit()

    def tearDown(self):
        DailyHealthRecord.query.filter(DailyHealthRecord.user_id.in_([self.athlete_a.id, self.athlete_b.id])).delete(synchronize_session=False)
        User.query.filter(User.id.in_([self.athlete_a.id, self.athlete_b.id])).delete(synchronize_session=False)
        db.session.commit()
        self.app_context.pop()

    def _login(self, email):
        return self.client.post('/login', data={'email': email, 'password': 'Password123!'})

    def test_weekly_summary_empty(self):
        """Verify 7-day weekly summary handles 0 records gracefully."""
        self._login(self.athlete_a.email)
        res = self.client.get('/api/weekly-summary')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['period'], 'weekly')
        self.assertEqual(data['total_records'], 0)

    def test_monthly_summary_empty(self):
        """Verify 30-day monthly summary handles 0 records gracefully."""
        self._login(self.athlete_a.email)
        res = self.client.get('/api/monthly-summary')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['period'], 'monthly')
        self.assertEqual(data['total_records'], 0)

    def test_weekly_summary_with_records(self):
        """Verify 7-day summary calculates exact averages from active records."""
        today = datetime.utcnow().date()
        for i in range(3):
            d_str = (today - timedelta(days=i)).strftime('%Y-%m-%d')
            rec = DailyHealthRecord(
                user_id=self.athlete_a.id,
                record_date=d_str,
                sleep_hours=8.0,
                training_hours=2.0,
                resting_heart_rate=60,
                fatigue_level=2,
                stress_level=2,
                risk_score=20.0,
                risk_label="Low Risk"
            )
            db.session.add(rec)
        db.session.commit()

        self._login(self.athlete_a.email)
        res = self.client.get('/api/weekly-summary')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['total_records'], 3)
        self.assertEqual(data['averages']['sleep_hours'], 8.0)
        self.assertEqual(data['averages']['resting_heart_rate'], 60.0)

    def test_summary_user_isolation(self):
        """Verify Athlete A's summary does NOT include Athlete B's health records."""
        today_str = datetime.utcnow().strftime('%Y-%m-%d')
        rec_b = DailyHealthRecord(
            user_id=self.athlete_b.id,
            record_date=today_str,
            sleep_hours=5.0,
            training_hours=6.0,
            resting_heart_rate=90,
            fatigue_level=8,
            stress_level=8,
            risk_score=85.0,
            risk_label="High Risk"
        )
        db.session.add(rec_b)
        db.session.commit()

        self._login(self.athlete_a.email)
        res = self.client.get('/api/weekly-summary')
        data = res.get_json()
        self.assertEqual(data['total_records'], 0)

if __name__ == '__main__':
    unittest.main()
