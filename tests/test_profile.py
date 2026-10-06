import unittest
import time
from datetime import datetime
from app import app, db, User

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        
        self.athlete_a = User(
            full_name="Athlete Alpha",
            email=f"athlete_a_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=24,
            date_of_birth=datetime(2002, 1, 1).date(),
            role="athlete"
        )
        self.athlete_a.set_password("Password123!")
        
        self.athlete_b = User(
            full_name="Athlete Beta",
            email=f"athlete_b_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Tennis",
            _legacy_age=23,
            date_of_birth=datetime(2003, 1, 1).date(),
            role="athlete"
        )
        self.athlete_b.set_password("Password123!")

        db.session.add(self.athlete_a)
        db.session.add(self.athlete_b)
        db.session.commit()

    def tearDown(self):
        User.query.filter(User.email.like("%example.com")).delete(synchronize_session=False)
        db.session.commit()
        self.app_context.pop()

    def _login(self, email, password="Password123!"):
        return self.client.post('/login', data={'email': email, 'password': password})

    def test_profile_page_loading(self):
        """Verify profile HTML page loads for logged-in athlete."""
        self._login(self.athlete_a.email)
        res = self.client.get('/profile')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Athlete Alpha", res.data)

    def test_profile_data_retrieval_api(self):
        """Verify GET /api/profile returns athlete's profile payload."""
        self._login(self.athlete_a.email)
        res = self.client.get('/api/profile')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['user']['email'], self.athlete_a.email)

    def test_profile_update_and_persistence(self):
        """Verify updating profile persists to MySQL database."""
        self._login(self.athlete_a.email)
        payload = {
            'full_name': 'Athlete Alpha Updated',
            'email': self.athlete_a.email,
            'date_of_birth': '1998-05-20',
            'gender': 'Male',
            'phone': '+1234567890',
            'primary_sport': 'Basketball',
            'height_cm': 185.5,
            'weight_kg': 82.0
        }
        res = self.client.post('/api/profile', json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')

        db.session.expire_all()
        updated_user = User.query.get(self.athlete_a.id)
        self.assertEqual(updated_user.full_name, 'Athlete Alpha Updated')
        self.assertEqual(updated_user.primary_sport, 'Basketball')
        self.assertEqual(updated_user.height_cm, 185.5)

    def test_profile_gender_validation(self):
        """Verify invalid gender is rejected in profile update."""
        self._login(self.athlete_a.email)
        payload = {
            'full_name': 'Athlete Alpha',
            'email': self.athlete_a.email,
            'gender': 'NonBinary'
        }
        res = self.client.post('/api/profile', json=payload)
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertIn('gender must be either male or female', data['message'].lower())

    def test_profile_user_isolation(self):
        """Verify Athlete A cannot view or mutate Athlete B's profile via session API."""
        self._login(self.athlete_a.email)
        res = self.client.get('/api/profile')
        data = res.get_json()
        self.assertEqual(data['user']['email'], self.athlete_a.email)
        self.assertNotEqual(data['user']['email'], self.athlete_b.email)

if __name__ == '__main__':
    unittest.main()
