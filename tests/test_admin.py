import unittest
import time
from datetime import datetime
from app import app, db, User, DailyHealthRecord, AdminNote, Notification

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)

        # Create Test Admin User with required non-null fields for MySQL
        self.admin = User(
            full_name="Admin Test User",
            email=f"admin_test_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Admin",
            _legacy_age=35,
            date_of_birth=datetime(1990, 1, 1).date(),
            role="admin"
        )
        self.admin.set_password("AdminPass123!")

        # Create Test Athlete User
        self.athlete = User(
            full_name="Athlete AdminTarget",
            email=f"athlete_adm_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Basketball",
            _legacy_age=25,
            date_of_birth=datetime(2000, 1, 1).date(),
            role="athlete"
        )
        self.athlete.set_password("Password123!")

        db.session.add(self.admin)
        db.session.add(self.athlete)
        db.session.commit()

        # Create a health record under Athlete
        self.health_record = DailyHealthRecord(
            user_id=self.athlete.id,
            record_date="2026-09-10",
            sleep_hours=6.0,
            training_hours=4.0,
            resting_heart_rate=75,
            fatigue_level=6,
            stress_level=5,
            risk_score=55.0,
            risk_label="Medium Risk",
            review_status="Pending Review"
        )
        db.session.add(self.health_record)
        db.session.commit()

    def tearDown(self):
        AdminNote.query.filter_by(athlete_id=self.athlete.id).delete()
        Notification.query.filter_by(athlete_id=self.athlete.id).delete()
        DailyHealthRecord.query.filter_by(user_id=self.athlete.id).delete()
        User.query.filter(User.id.in_([self.admin.id, self.athlete.id])).delete(synchronize_session=False)
        db.session.commit()
        self.app_context.pop()

    def _login_admin(self):
        return self.client.post('/login', data={'email': self.admin.email, 'password': 'AdminPass123!'})

    def _login_athlete(self):
        return self.client.post('/login', data={'email': self.athlete.email, 'password': 'Password123!'})

    def test_admin_001_login(self):
        """ADMIN-001: Admin login with valid credentials."""
        res = self._login_admin()
        self.assertEqual(res.status_code, 302)
        self.assertIn('/admin/dashboard', res.location)

    def test_admin_002_dashboard_loads(self):
        """ADMIN-002: Admin dashboard page rendering."""
        self._login_admin()
        res = self.client.get('/admin/dashboard')
        self.assertEqual(res.status_code, 200)

    def test_admin_003_stats_api(self):
        """ADMIN-003: Admin statistics API returns live database counts."""
        self._login_admin()
        res = self.client.get('/api/admin/stats')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('total_athletes', data['stats'])

    def test_admin_004_to_006_athletes_roster_search_filter(self):
        """ADMIN-004 to ADMIN-006: Athlete roster listing, search, and sport filtering."""
        self._login_admin()
        # Listing
        res = self.client.get('/api/admin/athletes')
        self.assertEqual(res.status_code, 200)

        # Search
        res_s = self.client.get(f'/api/admin/athletes?q=AdminTarget')
        data_s = res_s.get_json()
        self.assertEqual(len(data_s['athletes']), 1)

        # Filter
        res_f = self.client.get('/api/admin/athletes?sport=basketball')
        data_f = res_f.get_json()
        self.assertGreaterEqual(len(data_f['athletes']), 1)

    def test_admin_007_athlete_detail(self):
        """ADMIN-007: Admin detail view for specific athlete."""
        self._login_admin()
        res = self.client.get(f'/api/admin/athletes/{self.athlete.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['athlete']['email'], self.athlete.email)

    def test_admin_008_health_records(self):
        """ADMIN-008: Admin health records global list."""
        self._login_admin()
        res = self.client.get('/api/admin/health-records')
        self.assertEqual(res.status_code, 200)

    def test_admin_009_predictions(self):
        """ADMIN-009: Admin predictions list."""
        self._login_admin()
        res = self.client.get('/api/admin/predictions')
        self.assertEqual(res.status_code, 200)

    def test_admin_010_to_012_case_review_notes_notification(self):
        """ADMIN-010 to ADMIN-012: Case review, status update, admin notes, and athlete notification visibility."""
        self._login_admin()
        
        # Update Case Status
        res_st = self.client.put(f'/api/admin/cases/{self.health_record.id}/status', json={
            'review_status': 'Under Review',
            'note': 'Initiated review'
        })
        self.assertEqual(res_st.status_code, 200)

        # Add Admin Note
        res_note = self.client.post(f'/api/admin/cases/{self.health_record.id}/notes', json={
            'note': 'Please rest for 2 days.'
        })
        self.assertEqual(res_note.status_code, 200)

        # Verify Notification for Athlete
        self.client.get('/logout')
        self._login_athlete()
        res_notif = self.client.get('/api/notifications')
        self.assertEqual(res_notif.status_code, 200)
        data_n = res_notif.get_json()
        self.assertGreaterEqual(data_n['count'], 1)

    def test_admin_013_deactivate_activate_athlete(self):
        """ADMIN-013: Admin deactivates and reactivates athlete account."""
        self._login_admin()
        
        # Deactivate
        res_deact = self.client.post(f'/api/admin/athletes/{self.athlete.id}/deactivate')
        self.assertEqual(res_deact.status_code, 200)
        user_check = User.query.get(self.athlete.id)
        self.assertEqual(user_check.account_status, 'inactive')

        # Activate
        res_act = self.client.post(f'/api/admin/athletes/{self.athlete.id}/activate')
        self.assertEqual(res_act.status_code, 200)
        user_check_2 = User.query.get(self.athlete.id)
        self.assertEqual(user_check_2.account_status, 'active')

    def test_admin_014_logout(self):
        """ADMIN-014: Admin logout."""
        self._login_admin()
        res = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
