import unittest
import time
from datetime import datetime
from app import app, db, User

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        self.test_email = f"automation_test_athlete_{self.timestamp}@example.com"
        self.test_password = "Password123!"

    def tearDown(self):
        user = User.query.filter(User.email.like("automation_test_athlete_%")).all()
        for u in user:
            db.session.delete(u)
        db.session.commit()
        self.app_context.pop()

    def test_tc_auth_001_valid_registration(self):
        """TC-AUTH-001: Valid athlete registration creates account in MySQL DB."""
        payload = {
            'full_name': f'Automation Test Athlete {self.timestamp}',
            'date_of_birth': '2000-01-15',
            'gender': 'Male',
            'primary_sport': 'Football',
            'email': self.test_email,
            'password': self.test_password,
            'confirm_password': self.test_password
        }
        res = self.client.post('/register', data=payload, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        
        user = User.query.filter_by(email=self.test_email).first()
        self.assertIsNotNone(user, "User should be created in MySQL database")
        self.assertEqual(user.gender, 'Male')
        self.assertEqual(user.role, 'athlete')

    def test_tc_auth_002_duplicate_email(self):
        """TC-AUTH-002: Duplicate email registration is rejected."""
        payload = {
            'full_name': f'Automation Test Athlete {self.timestamp}',
            'date_of_birth': '2000-01-15',
            'gender': 'Male',
            'primary_sport': 'Football',
            'email': self.test_email,
            'password': self.test_password,
            'confirm_password': self.test_password
        }
        self.client.post('/register', data=payload)
        res = self.client.post('/register', data=payload, follow_redirects=True)
        self.assertIn(b"already registered", res.data.lower() + res.data)

    def test_tc_auth_003_invalid_empty_fields(self):
        """TC-AUTH-003: Invalid or empty required fields fail registration."""
        payload = {
            'full_name': '',
            'date_of_birth': '',
            'gender': 'Other',
            'primary_sport': 'Tennis',
            'email': f'invalid_{self.timestamp}@example.com',
            'password': '123',
            'confirm_password': '123'
        }
        res = self.client.post('/register', data=payload, follow_redirects=True)
        self.assertIn(b"required", res.data.lower())

    def test_tc_auth_004_valid_athlete_login(self):
        """TC-AUTH-004: Valid athlete login succeeds and opens dashboard."""
        user = User(
            full_name="Test Athlete Auth4",
            email=self.test_email,
            gender="Female",
            primary_sport="Basketball",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        user.set_password(self.test_password)
        db.session.add(user)
        db.session.commit()

        res = self.client.post('/login', data={'email': self.test_email, 'password': self.test_password}, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"dashboard", res.data.lower())

    def test_tc_auth_005_invalid_password(self):
        """TC-AUTH-005: Login with wrong password is rejected."""
        user = User(
            full_name="Test Athlete Auth5",
            email=self.test_email,
            gender="Male",
            primary_sport="Soccer",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        user.set_password(self.test_password)
        db.session.add(user)
        db.session.commit()

        res = self.client.post('/login', data={'email': self.test_email, 'password': 'WrongPassword123!'}, follow_redirects=True)
        self.assertIn(b"invalid credentials", res.data.lower())

    def test_tc_auth_006_non_existing_account(self):
        """TC-AUTH-006: Login with non-existing email is rejected."""
        res = self.client.post('/login', data={'email': 'non_existent_99999@example.com', 'password': 'Password123!'}, follow_redirects=True)
        self.assertIn(b"invalid credentials", res.data.lower())

    def test_tc_auth_007_logout(self):
        """TC-AUTH-007: Logout terminates session."""
        user = User(
            full_name="Test Athlete Auth7",
            email=self.test_email,
            gender="Female",
            primary_sport="Running",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        user.set_password(self.test_password)
        db.session.add(user)
        db.session.commit()

        self.client.post('/login', data={'email': self.test_email, 'password': self.test_password})
        res = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"sign in", res.data.lower())

    def test_tc_auth_008_browser_back_protection(self):
        """TC-AUTH-008: Authenticated dashboard cannot be accessed without session after logout."""
        user = User(
            full_name="Test Athlete Auth8",
            email=self.test_email,
            gender="Male",
            primary_sport="Swimming",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        user.set_password(self.test_password)
        db.session.add(user)
        db.session.commit()

        self.client.post('/login', data={'email': self.test_email, 'password': self.test_password})
        self.client.get('/logout')

        res = self.client.get('/dashboard')
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.headers.get('Cache-Control'), 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0')

    def test_tc_auth_009_inactive_athlete_login(self):
        """TC-AUTH-009: Inactive athlete login is blocked."""
        user = User(
            full_name="Test Inactive Athlete",
            email=self.test_email,
            gender="Male",
            primary_sport="Boxing",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete",
            account_status="deactivated"
        )
        user.set_password(self.test_password)
        db.session.add(user)
        db.session.commit()

        res = self.client.post('/login', data={'email': self.test_email, 'password': self.test_password}, follow_redirects=True)
        self.assertIn(b"deactivated", res.data.lower())

if __name__ == '__main__':
    unittest.main()
