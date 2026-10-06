import unittest
import time
from datetime import datetime
from app import app, db, User

class TestCoach(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.coach = User(
            full_name="Head Coach Smith",
            email=f"coach_test_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=38,
            date_of_birth=datetime(1988, 1, 1).date(),
            role="coach"
        )
        self.coach.set_password("CoachPass123!")

        self.athlete = User(
            full_name="Athlete CoachTestTarget",
            email=f"athlete_ct_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=22,
            date_of_birth=datetime(2004, 1, 1).date(),
            role="athlete"
        )
        self.athlete.set_password("Password123!")

        db.session.add(self.coach)
        db.session.add(self.athlete)
        db.session.commit()

    def tearDown(self):
        User.query.filter(User.id.in_([self.coach.id, self.athlete.id])).delete(synchronize_session=False)
        db.session.commit()
        self.app_context.pop()

    def test_coach_login_redirection(self):
        """Verify coach login redirects to /coach/dashboard."""
        res = self.client.post('/login', data={'email': self.coach.email, 'password': 'CoachPass123!'})
        self.assertEqual(res.status_code, 302)
        self.assertIn('/coach/dashboard', res.location)

    def test_coach_dashboard_page_rendering(self):
        """Verify coach dashboard loads HTML page for authenticated coach."""
        self.client.post('/login', data={'email': self.coach.email, 'password': 'CoachPass123!'})
        res = self.client.get('/coach/dashboard')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Head Coach Smith", res.data)

    def test_athlete_blocked_from_coach_dashboard(self):
        """Verify athlete role is blocked from accessing /coach/dashboard."""
        self.client.post('/login', data={'email': self.athlete.email, 'password': 'Password123!'})
        res = self.client.get('/coach/dashboard', follow_redirects=True)
        self.assertIn(b"access denied", res.data.lower())

if __name__ == '__main__':
    unittest.main()
