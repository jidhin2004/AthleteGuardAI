import unittest
import time
from datetime import datetime
from app import app, db, User, Team, TeamMember

class TestCoachTeamCreation(unittest.TestCase):
    """
    Automated Test Suite for Step 3: Coach Team Creation module.
    Verifies team creation, server-side team code generation, database storage,
    dynamic player count, coach-level data isolation, and authorization guards.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        self.csrf_token = "test_csrf_token_step3_team_creation"

        # Create Coach A
        self.coach_a = User(
            full_name="Coach Football Primary",
            email=f"coach_fc_a_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=38,
            date_of_birth=datetime(1988, 5, 12).date(),
            role="coach"
        )
        self.coach_a.set_password("CoachPass123!")

        # Create Coach B
        self.coach_b = User(
            full_name="Coach Basketball Secondary",
            email=f"coach_bk_b_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Basketball",
            _legacy_age=42,
            date_of_birth=datetime(1984, 8, 20).date(),
            role="coach"
        )
        self.coach_b.set_password("CoachPass123!")

        # Create Athlete User
        self.athlete = User(
            full_name="Athlete Player Test",
            email=f"athlete_p3_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=21,
            date_of_birth=datetime(2005, 3, 15).date(),
            role="athlete"
        )
        self.athlete.set_password("Password123!")

        db.session.add(self.coach_a)
        db.session.add(self.coach_b)
        db.session.add(self.athlete)
        db.session.commit()

    def tearDown(self):
        try:
            db.session.rollback()
            TeamMember.query.filter(TeamMember.athlete_id == self.athlete.id).delete()
            Team.query.filter(Team.coach_id.in_([self.coach_a.id, self.coach_b.id])).delete()
            User.query.filter(User.id.in_([self.coach_a.id, self.coach_b.id, self.athlete.id])).delete(synchronize_session=False)
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

    def test_01_coach_creates_football_team(self):
        """TEST 1: Coach A creates University Football Team; verified in MySQL with generated code."""
        self._login(self.coach_a.email, "CoachPass123!")
        payload = {
            'team_name': 'University Football Team',
            'sport': 'Football',
            'season': '2026-27',
            'description': 'Official university varsity football squad.',
            'csrf_token': self.csrf_token
        }
        res = self.client.post('/api/coach/teams', json=payload)
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('team', data)
        self.assertEqual(data['team']['team_name'], 'University Football Team')
        self.assertEqual(data['team']['sport'], 'Football')
        self.assertEqual(data['team']['season'], '2026-27')
        self.assertEqual(data['team']['member_count'], 0)

        # Database verification
        team_db = Team.query.filter_by(team_code=data['team']['team_code']).first()
        self.assertIsNotNone(team_db)
        self.assertEqual(team_db.coach_id, self.coach_a.id)
        self.assertEqual(team_db.status, 'active')

    def test_02_server_side_unique_team_code_generated(self):
        """TEST 2: Verifies unique team code generated server-side for sports."""
        self._login(self.coach_a.email, "CoachPass123!")
        res1 = self.client.post('/api/coach/teams', json={'team_name': 'Team Alpha', 'sport': 'Basketball', 'season': '2026-27', 'csrf_token': self.csrf_token})
        res2 = self.client.post('/api/coach/teams', json={'team_name': 'Team Beta', 'sport': 'Basketball', 'season': '2026-27', 'csrf_token': self.csrf_token})
        self.assertEqual(res1.status_code, 201)
        self.assertEqual(res2.status_code, 201)

        code1 = res1.get_json()['team']['team_code']
        code2 = res2.get_json()['team']['team_code']
        self.assertNotEqual(code1, code2)
        self.assertTrue(code1.startswith('BB-'))
        self.assertTrue(code2.startswith('BB-'))

    def test_03_coach_views_my_teams_dynamic_player_count(self):
        """TEST 3: Coach lists created teams; dynamic player count verified from DB."""
        team = Team(
            team_name='University Cricket Team',
            sport='Cricket',
            season='2026-27',
            coach_id=self.coach_a.id,
            team_code=f'CR-TEST{self.timestamp}'
        )
        db.session.add(team)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get('/api/coach/teams')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['teams'][0]['member_count'], 0)

    def test_04_coach_isolation_security(self):
        """TEST 4: Coach A cannot view or manage Coach B's teams."""
        team_b = Team(
            team_name='Coach B Volleyball Team',
            sport='Volleyball',
            season='2026-27',
            coach_id=self.coach_b.id,
            team_code=f'VB-B{self.timestamp}'
        )
        db.session.add(team_b)
        db.session.commit()

        # Coach A logs in
        self._login(self.coach_a.email, "CoachPass123!")
        res_list = self.client.get('/api/coach/teams')
        self.assertEqual(res_list.status_code, 200)
        teams = res_list.get_json()['teams']
        # Coach A list must NOT include Coach B's team
        self.assertNotIn(team_b.id, [t['id'] for t in teams])

        # Coach A direct access attempt
        res_detail = self.client.get(f'/api/coach/teams/{team_b.id}')
        self.assertEqual(res_detail.status_code, 403)

    def test_05_athlete_forbidden_from_coach_team_creation(self):
        """TEST 5: Athlete role forbidden from accessing Coach team creation endpoint."""
        self._login(self.athlete.email, "Password123!")
        res = self.client.post('/api/coach/teams', json={'team_name': 'Rogue Athlete Team', 'sport': 'Football', 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 302) # Redirected to athlete dashboard

    def test_06_unauthenticated_user_access_blocked(self):
        """TEST 6: Unauthenticated user attempt to create team redirected to login."""
        res_get = self.client.get('/coach/teams')
        self.assertEqual(res_get.status_code, 302)
        self.assertIn('/login', res_get.location)

        res_post = self.client.post('/api/coach/teams', json={'team_name': 'Anon Team', 'sport': 'Athletics'}, headers={'X-CSRFToken': self.csrf_token})
        self.assertIn(res_post.status_code, [302, 400, 403])

if __name__ == '__main__':
    unittest.main()
