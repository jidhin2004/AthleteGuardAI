import unittest
import time
from datetime import datetime, timedelta
from app import app, db, User, Team, TeamMember, DailyHealthRecord
from services.ml_service import ml_service

class TestTeamDailyCheckinTracking(unittest.TestCase):
    """
    Automated Test Suite for TEAM DAILY HEALTH CHECK-IN TRACKING module.
    Verifies coach daily check-in tracking statistics (submitted, pending, completion rate),
    empty states, status transitions, coach team isolation security, athlete check-in status reminder API,
    role authorization, yesterday update labeling, and Random Forest prediction integrity.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        self.csrf_token = "test_csrf_token_daily_checkin"
        self.today_str = datetime.utcnow().strftime('%Y-%m-%d')
        self.yesterday_str = (datetime.utcnow().date() - timedelta(days=1)).strftime('%Y-%m-%d')

        # Create Coach A
        self.coach_a = User(
            full_name="Coach Football Alpha",
            email=f"coach_a_chk_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=40,
            date_of_birth=datetime(1986, 4, 10).date(),
            role="coach"
        )
        self.coach_a.set_password("CoachPass123!")

        # Create Coach B
        self.coach_b = User(
            full_name="Coach Basketball Beta",
            email=f"coach_b_chk_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Basketball",
            _legacy_age=38,
            date_of_birth=datetime(1988, 9, 15).date(),
            role="coach"
        )
        self.coach_b.set_password("CoachPass123!")

        # Create Athlete 1
        self.athlete_1 = User(
            full_name="Athlete Alpha One",
            email=f"athlete_1_chk_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=20,
            date_of_birth=datetime(2006, 2, 10).date(),
            role="athlete",
            account_status="active"
        )
        self.athlete_1.set_password("Password123!")

        # Create Athlete 2
        self.athlete_2 = User(
            full_name="Athlete Beta Two",
            email=f"athlete_2_chk_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=22,
            date_of_birth=datetime(2004, 6, 25).date(),
            role="athlete",
            account_status="active"
        )
        self.athlete_2.set_password("Password123!")

        db.session.add(self.coach_a)
        db.session.add(self.coach_b)
        db.session.add(self.athlete_1)
        db.session.add(self.athlete_2)
        db.session.commit()

        # Create Team for Coach A
        self.team_a = Team(
            team_name=f"Varsity Football Squad {self.timestamp}",
            sport="Football",
            season="2026-27",
            coach_id=self.coach_a.id,
            team_code=f"FB-A{self.timestamp}"
        )
        db.session.add(self.team_a)
        db.session.commit()

    def tearDown(self):
        try:
            db.session.rollback()
            DailyHealthRecord.query.filter(DailyHealthRecord.user_id.in_([self.athlete_1.id, self.athlete_2.id])).delete()
            TeamMember.query.filter(TeamMember.team_id == self.team_a.id).delete()
            Team.query.filter(Team.coach_id.in_([self.coach_a.id, self.coach_b.id])).delete()
            User.query.filter(User.id.in_([self.coach_a.id, self.coach_b.id, self.athlete_1.id, self.athlete_2.id])).delete(synchronize_session=False)
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.remove()
        self.app_context.pop()

    def _login(self, email, password):
        res = self.client.post('/login', data={'email': email, 'password': password})
        with self.client.session_transaction() as sess:
            sess['csrf_token'] = self.csrf_token
        return res

    def test_01_100_percent_completion_team(self):
        """TEST 1: 100% completion team - all players submitted today's health data."""
        # Add athlete 1 and athlete 2 to team_a
        m1 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_1.id, status='active')
        m2 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_2.id, status='active')
        db.session.add_all([m1, m2])

        # Add today's health record for both athletes
        rec1 = DailyHealthRecord(user_id=self.athlete_1.id, record_date=self.today_str, sleep_hours=8.0, training_hours=2.0, resting_heart_rate=60, fatigue_level=2, stress_level=2, risk_score=12.5, risk_label="Low Risk")
        rec2 = DailyHealthRecord(user_id=self.athlete_2.id, record_date=self.today_str, sleep_hours=7.5, training_hours=3.0, resting_heart_rate=65, fatigue_level=3, stress_level=3, risk_score=18.0, risk_label="Low Risk")
        db.session.add_all([rec1, rec2])
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['total_players'], 2)
        self.assertEqual(data['submitted'], 2)
        self.assertEqual(data['pending'], 0)
        self.assertEqual(data['completion_percentage'], 100.0)

        for p in data['players']:
            self.assertEqual(p['checkin_status'], 'Submitted')
            self.assertEqual(p['last_update'], 'Today')

    def test_02_partial_completion_team(self):
        """TEST 2: Partial completion team - 1 submitted today, 1 pending."""
        m1 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_1.id, status='active')
        m2 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_2.id, status='active')
        db.session.add_all([m1, m2])

        # Only athlete 1 submitted today
        rec1 = DailyHealthRecord(user_id=self.athlete_1.id, record_date=self.today_str, sleep_hours=8.0, training_hours=2.0, resting_heart_rate=60, fatigue_level=2, stress_level=2, risk_score=12.5, risk_label="Low Risk")
        db.session.add(rec1)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['total_players'], 2)
        self.assertEqual(data['submitted'], 1)
        self.assertEqual(data['pending'], 1)
        self.assertEqual(data['completion_percentage'], 50.0)

    def test_03_zero_percent_completion_team(self):
        """TEST 3: 0% completion team - 2 players, neither submitted today."""
        m1 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_1.id, status='active')
        m2 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_2.id, status='active')
        db.session.add_all([m1, m2])
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['total_players'], 2)
        self.assertEqual(data['submitted'], 0)
        self.assertEqual(data['pending'], 2)
        self.assertEqual(data['completion_percentage'], 0.0)

    def test_04_empty_team_zero_players(self):
        """TEST 4: Empty team with 0 players returns total_players=0, completion=0.0."""
        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['total_players'], 0)
        self.assertEqual(data['submitted'], 0)
        self.assertEqual(data['pending'], 0)
        self.assertEqual(data['completion_percentage'], 0.0)
        self.assertEqual(len(data['players']), 0)

    def test_05_status_transition_pending_to_submitted(self):
        """TEST 5: Real-time transition from Pending to Submitted upon record creation."""
        m1 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_1.id, status='active')
        db.session.add(m1)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        
        # Initial check - should be Pending
        res1 = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res1.get_json()['submitted'], 0)
        self.assertEqual(res1.get_json()['players'][0]['checkin_status'], 'Pending')

        # Athlete submits daily health record
        self._login(self.athlete_1.email, "Password123!")
        pred_res = self.client.post('/api/predictions/predict', json={
            'sleep_hours': 8.0,
            'training_hours': 2.5,
            'resting_heart_rate': 62,
            'fatigue_level': 3,
            'stress_level': 2,
            'previous_injury': False,
            'csrf_token': self.csrf_token
        })
        self.assertEqual(pred_res.status_code, 200)

        # Coach checks again - should now be Submitted
        self._login(self.coach_a.email, "CoachPass123!")
        res2 = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res2.get_json()['submitted'], 1)
        self.assertEqual(res2.get_json()['completion_percentage'], 100.0)
        self.assertEqual(res2.get_json()['players'][0]['checkin_status'], 'Submitted')

    def test_06_coach_team_isolation_guard(self):
        """TEST 6: Coach A cannot view check-ins for Coach B's team."""
        team_b = Team(
            team_name=f"Coach B Team {self.timestamp}",
            sport="Basketball",
            season="2026-27",
            coach_id=self.coach_b.id,
            team_code=f"BB-B{self.timestamp}"
        )
        db.session.add(team_b)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{team_b.id}/daily-checkins')
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.get_json()['status'], 'error')

    def test_07_athlete_checkin_status_reminder_api(self):
        """TEST 7: GET /api/athlete/today-checkin-status reflects exact submission state."""
        self._login(self.athlete_1.email, "Password123!")

        # Before submission
        res1 = self.client.get('/api/athlete/today-checkin-status')
        self.assertEqual(res1.status_code, 200)
        self.assertFalse(res1.get_json()['is_submitted'])

        # Submit daily health monitoring record
        self.client.post('/api/predictions/predict', json={
            'sleep_hours': 7.5,
            'training_hours': 3.0,
            'resting_heart_rate': 65,
            'fatigue_level': 4,
            'stress_level': 3,
            'previous_injury': False,
            'csrf_token': self.csrf_token
        })

        # After submission
        res2 = self.client.get('/api/athlete/today-checkin-status')
        self.assertEqual(res2.status_code, 200)
        self.assertTrue(res2.get_json()['is_submitted'])

    def test_08_athlete_role_forbidden_from_coach_checkins(self):
        """TEST 8: Athlete role is forbidden from accessing coach team daily-checkins endpoint."""
        self._login(self.athlete_1.email, "Password123!")
        res = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res.status_code, 302)  # Redirected due to coach_required decorator

    def test_09_previous_day_health_update_labeling(self):
        """TEST 9: Yesterday record shows last_update='Yesterday' and checkin_status='Pending'."""
        m1 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_1.id, status='active')
        rec_yesterday = DailyHealthRecord(
            user_id=self.athlete_1.id,
            record_date=self.yesterday_str,
            sleep_hours=7.0,
            training_hours=3.5,
            resting_heart_rate=68,
            fatigue_level=4,
            stress_level=4,
            risk_score=22.0,
            risk_label="Low Risk"
        )
        db.session.add_all([m1, rec_yesterday])
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        self.assertEqual(data['submitted'], 0)
        self.assertEqual(data['pending'], 1)
        player = data['players'][0]
        self.assertEqual(player['checkin_status'], 'Pending')
        self.assertEqual(player['last_update'], 'Yesterday')

    def test_10_system_and_prediction_integrity(self):
        """TEST 10: Check-in tracking preserves Random Forest ML model predictions & risk scores."""
        m1 = TeamMember(team_id=self.team_a.id, athlete_id=self.athlete_1.id, status='active')
        db.session.add(m1)
        db.session.commit()

        self._login(self.athlete_1.email, "Password123!")
        pred_res = self.client.post('/api/predictions/predict', json={
            'sleep_hours': 4.0,
            'training_hours': 8.0,
            'resting_heart_rate': 95,
            'fatigue_level': 9,
            'stress_level': 9,
            'previous_injury': True,
            'csrf_token': self.csrf_token
        })
        self.assertEqual(pred_res.status_code, 200)
        pred_data = pred_res.get_json()['prediction']
        self.assertIn('risk_score', pred_data)
        self.assertIn('risk_label', pred_data)

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{self.team_a.id}/daily-checkins')
        self.assertEqual(res.status_code, 200)
        player = res.get_json()['players'][0]
        self.assertIsNotNone(player['risk_score'])
        self.assertEqual(player['risk_score'], round(pred_data['risk_score'], 1))

if __name__ == '__main__':
    unittest.main()
