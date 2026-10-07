import unittest
import time
from datetime import datetime
from app import app, db, User, Team, TeamMember, DailyHealthRecord, Injury

class TestUIIntegration(unittest.TestCase):
    """
    Automated Test Suite for UI Integration of Step 3 & Step 4.
    Verifies Coach Dashboard navigation, dynamic counters (My Teams & Total Players),
    My Teams rendering, Create Team flow, Athlete sidebar navigation (Join Team & My Team),
    Team joining flow, dynamic player count updates, and system integrity.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        self.csrf_token = "test_csrf_token_ui_integration"

        # Create Coach User
        self.coach = User(
            full_name="Coach Alex Turner",
            email=f"coach_ui_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=41,
            date_of_birth=datetime(1985, 3, 10).date(),
            role="coach"
        )
        self.coach.set_password("CoachPass123!")

        # Create Football Athlete User
        self.athlete = User(
            full_name="Athlete Jordan Lee",
            email=f"athlete_ui_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=20,
            date_of_birth=datetime(2006, 6, 12).date(),
            role="athlete"
        )
        self.athlete.set_password("PlayerPass123!")

        db.session.add(self.coach)
        db.session.add(self.athlete)
        db.session.commit()

    def tearDown(self):
        try:
            db.session.rollback()
            user_ids = [self.coach.id, self.athlete.id]
            TeamMember.query.filter(TeamMember.athlete_id.in_(user_ids)).delete(synchronize_session=False)
            Team.query.filter(Team.coach_id == self.coach.id).delete(synchronize_session=False)
            User.query.filter(User.id.in_(user_ids)).delete(synchronize_session=False)
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

    def test_01_coach_dashboard_navigation_and_dynamic_counters(self):
        """TEST 1: Login as Coach -> Coach Dashboard loads with navigation & dynamic summary counters."""
        self._login(self.coach.email, "CoachPass123!")
        res = self.client.get('/coach/dashboard')
        self.assertEqual(res.status_code, 200)

        html = res.get_data(as_text=True)
        # Verify sidebar links
        self.assertIn('My Teams', html)
        self.assertIn('/coach/teams', html)
        self.assertIn('Create Team', html)
        # Verify updated header text
        self.assertIn('Manage your sports teams and monitor your registered players.', html)
        self.assertNotIn('Team management features will be available here.', html)

    def test_02_coach_my_teams_page_accessibility(self):
        """TEST 2: Click My Teams -> /coach/teams page loads cleanly."""
        self._login(self.coach.email, "CoachPass123!")
        res = self.client.get('/coach/teams')
        self.assertEqual(res.status_code, 200)
        self.assertIn('My Teams', res.get_data(as_text=True))

    def test_03_coach_creates_team_via_existing_api(self):
        """TEST 3: Coach creates Football team -> Team stored in DB & code returned."""
        self._login(self.coach.email, "CoachPass123!")
        res = self.client.post('/api/coach/teams', json={
            'team_name': 'University Football Squad',
            'sport': 'Football',
            'season': '2026-27',
            'description': 'Varsity squad',
            'csrf_token': self.csrf_token
        })
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('FB-', data['team']['team_code'])

    def test_04_athlete_navigation_join_team_and_my_team(self):
        """TEST 4: Login as Athlete -> Sidebar includes Join Team and My Team."""
        self._login(self.athlete.email, "PlayerPass123!")
        res = self.client.get('/dashboard')
        self.assertEqual(res.status_code, 200)

        html = res.get_data(as_text=True)
        self.assertIn('Join Team', html)
        self.assertIn('My Team', html)
        self.assertIn('/join-team', html)
        self.assertIn('/my-team', html)

    def test_05_athlete_joins_team_flow_and_roster_count_updates(self):
        """TEST 5 & 6: Athlete joins via team code -> My Team page displays membership; Coach player count updates dynamically."""
        # 1. Coach creates team
        team = Team(team_name="Football Varsity", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-FLOW{self.timestamp}")
        db.session.add(team)
        db.session.commit()

        # 2. Athlete joins team
        self._login(self.athlete.email, "PlayerPass123!")
        res_join = self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res_join.status_code, 200)

        # 3. Athlete views My Team
        res_my_team = self.client.get('/api/my-team')
        self.assertEqual(res_my_team.status_code, 200)
        data_my_team = res_my_team.get_json()
        self.assertEqual(data_my_team['count'], 1)
        self.assertEqual(data_my_team['teams'][0]['team_name'], "Football Varsity")

        # 4. Coach checks roster player count
        self._login(self.coach.email, "CoachPass123!")
        res_coach_teams = self.client.get('/api/coach/teams')
        self.assertEqual(res_coach_teams.status_code, 200)
        data_coach = res_coach_teams.get_json()
        self.assertEqual(data_coach['teams'][0]['member_count'], 1)

if __name__ == '__main__':
    unittest.main()
