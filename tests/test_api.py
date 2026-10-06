import unittest
import time
from datetime import datetime
from app import app, db, User

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.athlete = User(
            full_name="API Test Athlete",
            email=f"api_test_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Soccer",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        self.athlete.set_password("Password123!")
        db.session.add(self.athlete)
        db.session.commit()

    def tearDown(self):
        User.query.filter_by(id=self.athlete.id).delete()
        db.session.commit()
        self.app_context.pop()

    def _login(self):
        return self.client.post('/login', data={'email': self.athlete.email, 'password': 'Password123!'})

    def test_api_latency_and_schema(self):
        """Verify API response returns in under 2 seconds and contains expected JSON keys."""
        self._login()
        start_time = time.time()
        res = self.client.get('/api/dashboard-data')
        elapsed_ms = (time.time() - start_time) * 1000

        self.assertEqual(res.status_code, 200)
        self.assertLess(elapsed_ms, 2000.0, "Dashboard API response should be under 2000ms")
        data = res.get_json()
        self.assertIn('status', data)

    def test_api_404_non_existent_endpoint(self):
        """Verify requesting invalid API route returns 404."""
        self._login()
        res = self.client.get('/api/non-existent-route-123')
        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()
