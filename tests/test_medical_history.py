import unittest
import time
from datetime import datetime
from app import app, db, User, Injury, MedicalCondition, Allergy, Medication, Surgery

class TestMedicalHistory(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        self.athlete = User(
            full_name="Athlete MedTest",
            email=f"athlete_med_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Soccer",
            _legacy_age=25,
            date_of_birth=datetime(2001, 1, 1).date(),
            role="athlete"
        )
        self.athlete.set_password("Password123!")

        self.athlete_b = User(
            full_name="Athlete MedIsolation",
            email=f"athlete_med_b_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Running",
            _legacy_age=24,
            date_of_birth=datetime(2002, 1, 1).date(),
            role="athlete"
        )
        self.athlete_b.set_password("Password123!")

        db.session.add(self.athlete)
        db.session.add(self.athlete_b)
        db.session.commit()

    def tearDown(self):
        Injury.query.filter_by(user_id=self.athlete.id).delete()
        MedicalCondition.query.filter_by(user_id=self.athlete.id).delete()
        Allergy.query.filter_by(user_id=self.athlete.id).delete()
        User.query.filter(User.email.like("athlete_med_%")).delete(synchronize_session=False)
        db.session.commit()
        self.app_context.pop()

    def _login(self, email):
        return self.client.post('/login', data={'email': email, 'password': 'Password123!'})

    def test_get_medical_history_empty(self):
        """Verify fetching medical history for athlete with 0 records."""
        self._login(self.athlete.email)
        res = self.client.get('/api/medical-history')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['summary']['injuries_count'], 0)

    def test_add_and_manage_injury(self):
        """Verify adding, updating, and deleting an injury record."""
        self._login(self.athlete.email)
        payload = {
            'injury_type': 'Hamstring Strain',
            'body_part': 'Thigh',
            'injury_date': '2026-08-10',
            'severity': 'Moderate',
            'treatment': 'Rest and Physical Therapy',
            'recovery_status': 'Recovering',
            'notes': 'Occurred during sprint training'
        }
        res = self.client.post('/api/injuries', json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        injury_id = data['injury']['id']

        injury = Injury.query.get(injury_id)
        self.assertIsNotNone(injury)
        self.assertEqual(injury.user_id, self.athlete.id)

        update_payload = {
            'injury_type': 'Hamstring Strain',
            'body_part': 'Thigh',
            'injury_date': '2026-08-10',
            'severity': 'Mild',
            'recovery_status': 'Fully Recovered'
        }
        res_up = self.client.put(f'/api/injuries/{injury_id}', json=update_payload)
        self.assertEqual(res_up.status_code, 200)

        res_del = self.client.delete(f'/api/injuries/{injury_id}')
        self.assertEqual(res_del.status_code, 200)
        self.assertIsNone(Injury.query.get(injury_id))

    def test_medical_history_user_isolation(self):
        """Verify Athlete B cannot modify or delete Athlete A's injury record."""
        injury = Injury(
            user_id=self.athlete.id,
            injury_type="Ankle Sprain",
            body_part="Ankle",
            injury_date="2026-07-01",
            severity="Mild"
        )
        db.session.add(injury)
        db.session.commit()

        self._login(self.athlete_b.email)
        res = self.client.delete(f'/api/injuries/{injury.id}')
        self.assertEqual(res.status_code, 404)

        self.assertIsNotNone(Injury.query.get(injury.id))

if __name__ == '__main__':
    unittest.main()
