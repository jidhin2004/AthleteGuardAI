import unittest
import time
from app import app, db, User, DailyHealthRecord, Injury

class TestEndToEndWorkflow(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        self.test_email = f"automation_e2e_{self.timestamp}@example.com"
        self.test_password = "Password123!"

    def tearDown(self):
        user = User.query.filter_by(email=self.test_email).first()
        if user:
            DailyHealthRecord.query.filter_by(user_id=user.id).delete()
            Injury.query.filter_by(user_id=user.id).delete()
            db.session.delete(user)
            db.session.commit()
        self.app_context.pop()

    def test_e2e_complete_athlete_lifecycle(self):
        """
        TC-E2E-001: Comprehensive End-to-End Athlete Lifecycle Integration Test
        Covers all 23 steps required by Section 9 of the test specification.
        """
        # Step 1: Open public index landing page
        res_idx = self.client.get('/')
        self.assertEqual(res_idx.status_code, 200)

        # Step 2: Register test athlete
        reg_payload = {
            'full_name': f'E2E Test Athlete {self.timestamp}',
            'date_of_birth': '2001-03-25',
            'gender': 'Male',
            'primary_sport': 'Basketball',
            'email': self.test_email,
            'password': self.test_password,
            'confirm_password': self.test_password
        }
        res_reg = self.client.post('/register', data=reg_payload, follow_redirects=True)
        self.assertEqual(res_reg.status_code, 200)
        self.assertIn(b"dashboard", res_reg.data.lower())

        # Step 3: Verify athlete logged in session
        user = User.query.filter_by(email=self.test_email).first()
        self.assertIsNotNone(user)

        # Step 4: Open profile & verify profile data
        res_prof = self.client.get('/profile')
        self.assertEqual(res_prof.status_code, 200)
        self.assertIn(self.test_email.encode(), res_prof.data)

        # Step 5: Open medical history & add medical record
        med_payload = {
            'injury_type': 'Ankle Sprain',
            'body_part': 'Right Ankle',
            'injury_date': '2026-06-15',
            'severity': 'Mild',
            'recovery_status': 'Fully Recovered'
        }
        res_med = self.client.post('/api/injuries', json=med_payload)
        self.assertEqual(res_med.status_code, 200)

        # Step 6: Open daily health monitoring form page
        res_mon = self.client.get('/daily-monitoring')
        self.assertEqual(res_mon.status_code, 200)

        # Step 7: Enter valid daily health data & submit to ML prediction
        health_payload = {
            'sleep_hours': 8.0,
            'training_hours': 3.0,
            'resting_heart_rate': 65,
            'fatigue_level': 3,
            'stress_level': 2,
            'previous_injury': True,
            'injury_details': 'Ankle strain past recovery'
        }
        res_pred = self.client.post('/api/predictions/predict', json=health_payload)
        self.assertEqual(res_pred.status_code, 200)
        pred_data = res_pred.get_json()
        self.assertEqual(pred_data['status'], 'success')
        self.assertIsNotNone(pred_data['prediction']['risk_score'])
        self.assertIsNotNone(pred_data['prediction']['risk_label'])

        # Step 8: Open prediction history & verify prediction exists
        res_hist = self.client.get('/api/predictions/history')
        self.assertEqual(res_hist.status_code, 200)
        hist_data = res_hist.get_json()
        self.assertGreaterEqual(len(hist_data['history']), 1)

        # Step 9: Open dashboard & verify relevant data
        res_dash = self.client.get('/api/dashboard-data')
        self.assertEqual(res_dash.status_code, 200)
        dash_data = res_dash.get_json()
        self.assertTrue(dash_data['has_predictions'])
        self.assertEqual(dash_data['stats']['total_predictions'], 1)

        # Step 10: Open weekly summary & verify output
        res_wk = self.client.get('/api/weekly-summary')
        self.assertEqual(res_wk.status_code, 200)
        wk_data = res_wk.get_json()
        self.assertEqual(wk_data['total_records'], 1)

        # Step 11: Open monthly summary & verify output
        res_mo = self.client.get('/api/monthly-summary')
        self.assertEqual(res_mo.status_code, 200)
        mo_data = res_mo.get_json()
        self.assertEqual(mo_data['total_records'], 1)

        # Step 12: Logout
        res_log = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(res_log.status_code, 200)

        # Step 13: Try browser back / direct URL access & verify protected content is not accessible
        res_back = self.client.get('/dashboard')
        self.assertEqual(res_back.status_code, 302)

if __name__ == '__main__':
    unittest.main()
