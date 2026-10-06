import unittest
import time
from datetime import datetime
from app import app, db, User

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.athlete = User(
            full_name="Athlete SecurityTest",
            email=f"athlete_sec_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        self.athlete.set_password("Password123!")

        self.admin = User(
            full_name="Admin SecurityTest",
            email=f"admin_sec_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Admin",
            _legacy_age=35,
            date_of_birth=datetime(1991, 1, 1).date(),
            role="admin"
        )
        self.admin.set_password("AdminPass123!")

        db.session.add(self.athlete)
        db.session.add(self.admin)
        db.session.commit()

    def tearDown(self):
        User.query.filter(User.id.in_([self.athlete.id, self.admin.id])).delete(synchronize_session=False)
        db.session.commit()
        self.app_context.pop()

    def test_unauthenticated_access_blocked(self):
        """Verify unauthenticated user cannot access protected endpoints."""
        protected_routes = ['/dashboard', '/profile', '/daily-monitoring', '/prediction-history', '/admin/dashboard', '/coach/dashboard']
        for route in protected_routes:
            res = self.client.get(route)
            self.assertEqual(res.status_code, 302, f"Route {route} should redirect unauthenticated user to login.")

    def test_athlete_cannot_access_admin_endpoints(self):
        """Verify athlete role cannot access admin pages or admin REST APIs."""
        self.client.post('/login', data={'email': self.athlete.email, 'password': 'Password123!'})
        
        res_page = self.client.get('/admin/dashboard', follow_redirects=True)
        self.assertIn(b"access denied", res_page.data.lower())

        res_api = self.client.get('/api/admin/stats', follow_redirects=True)
        self.assertIn(b"access denied", res_api.data.lower())

    def test_registration_role_tampering_prevention(self):
        """Verify submitting role='admin' during registration is ignored and forces role='athlete'."""
        payload = {
            'full_name': 'Tamper Test User',
            'date_of_birth': '2000-01-01',
            'gender': 'Male',
            'primary_sport': 'Tennis',
            'email': f'tamper_{self.timestamp}@example.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!',
            'role': 'admin'
        }
        self.client.post('/register', data=payload)
        user = User.query.filter_by(email=f'tamper_{self.timestamp}@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.role, 'athlete', "Role must strictly be set to 'athlete' during public registration.")
        db.session.delete(user)
        db.session.commit()

    def test_bfcache_security_headers(self):
        """Verify anti-caching HTTP headers are returned to prevent back-button dashboard leaks after logout."""
        res = self.client.get('/login')
        self.assertEqual(res.headers.get('Cache-Control'), 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0')
        self.assertEqual(res.headers.get('Pragma'), 'no-cache')

if __name__ == '__main__':
    unittest.main()
