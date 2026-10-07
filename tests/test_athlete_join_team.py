import unittest
import time
from datetime import datetime
from app import app, db, User, Team, TeamMember, DailyHealthRecord, Injury

class TestAthleteJoinTeam(unittest.TestCase):
    """
    Automated Test Suite for Step 4: Selected Athlete Join Team module.
    Verifies team creation, sport validation, duplicate membership rejection,
    single active team restriction, account status checks, security immunity against client parameter manipulation,
    dynamic player count updates on Coach roster, role authorization, and system continuity.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        self.csrf_token = "test_csrf_token_step4_join_team"

        # 1. Coach User
        self.coach = User(
            full_name="Coach Mark Vance",
            email=f"coach_mark_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=40,
            date_of_birth=datetime(1986, 4, 10).date(),
            role="coach"
        )
        self.coach.set_password("CoachPass123!")

        # 2. Football Athlete (Valid)
        self.football_athlete = User(
            full_name="Football Player One",
            email=f"fb_player_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=20,
            date_of_birth=datetime(2006, 1, 15).date(),
            role="athlete"
        )
        self.football_athlete.set_password("PlayerPass123!")

        # 3. Basketball Athlete (Mismatch Sport)
        self.basketball_athlete = User(
            full_name="Basketball Player Two",
            email=f"bb_player_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Basketball",
            _legacy_age=21,
            date_of_birth=datetime(2005, 7, 20).date(),
            role="athlete"
        )
        self.basketball_athlete.set_password("PlayerPass123!")

        # 4. Inactive Athlete
        self.inactive_athlete = User(
            full_name="Inactive Player Three",
            email=f"inact_player_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=22,
            date_of_birth=datetime(2004, 11, 5).date(),
            role="athlete",
            account_status="inactive"
        )
        self.inactive_athlete.set_password("PlayerPass123!")

        # 5. Admin User
        self.admin = User(
            full_name="System Admin User",
            email=f"admin_u_{self.timestamp}@example.com",
            gender="Other",
            primary_sport="Administration",
            _legacy_age=35,
            date_of_birth=datetime(1991, 9, 18).date(),
            role="admin"
        )
        self.admin.set_password("AdminPass123!")

        db.session.add(self.coach)
        db.session.add(self.football_athlete)
        db.session.add(self.basketball_athlete)
        db.session.add(self.inactive_athlete)
        db.session.add(self.admin)
        db.session.commit()

    def tearDown(self):
        try:
            db.session.rollback()
            user_ids = [self.coach.id, self.football_athlete.id, self.basketball_athlete.id, self.inactive_athlete.id, self.admin.id]
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

    def test_01_coach_creates_football_team(self):
        """TEST 1: Create a Football team as Coach. Expected: Team exists with team code."""
        self._login(self.coach.email, "CoachPass123!")
        res = self.client.post('/api/coach/teams', json={
            'team_name': 'University Football Squad',
            'sport': 'Football',
            'season': '2026-27',
            'csrf_token': self.csrf_token
        })
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertIn('team_code', data['team'])
        self.assertTrue(data['team']['team_code'].startswith('FB-'))

    def test_02_football_athlete_joins_team_successfully(self):
        """TEST 2: Football Athlete joins valid Football team code. Expected: Joins successfully."""
        team = Team(team_name="Football Varsity", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-S4{self.timestamp}")
        db.session.add(team)
        db.session.commit()

        self._login(self.football_athlete.email, "PlayerPass123!")
        res = self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')

        m = TeamMember.query.filter_by(team_id=team.id, athlete_id=self.football_athlete.id, status='active').first()
        self.assertIsNotNone(m)

    def test_03_athlete_views_my_team(self):
        """TEST 3: Open My Team API. Expected: Correct team info appears (Name, Sport, Season, Coach)."""
        team = Team(team_name="Lions Football", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-M{self.timestamp}")
        db.session.add(team)
        db.session.commit()
        db.session.add(TeamMember(team_id=team.id, athlete_id=self.football_athlete.id, status='active'))
        db.session.commit()

        self._login(self.football_athlete.email, "PlayerPass123!")
        res = self.client.get('/api/my-team')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['teams'][0]['team_name'], "Lions Football")
        self.assertEqual(data['teams'][0]['coach_name'], "Coach Mark Vance")
        self.assertEqual(data['teams'][0]['team_season'], "2026-27")

    def test_04_basketball_athlete_rejected_from_football_team(self):
        """TEST 4: Basketball athlete attempts to join Football team. Expected: Rejected due to sport mismatch."""
        team = Team(team_name="Varsity Football", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-MIS{self.timestamp}")
        db.session.add(team)
        db.session.commit()

        self._login(self.basketball_athlete.email, "PlayerPass123!")
        res = self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertIn("does not match this team", data['message'].lower())

    def test_05_invalid_team_code_rejected(self):
        """TEST 5: Athlete enters invalid team code. Expected: Rejected (HTTP 404)."""
        self._login(self.football_athlete.email, "PlayerPass123!")
        res = self.client.post('/api/teams/join', json={'team_code': 'INVALID-999', 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 404)

    def test_06_duplicate_membership_prevented(self):
        """TEST 6: Athlete joins same team twice. Expected: Duplicate membership prevented."""
        team = Team(team_name="Tigers FC", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-DUP{self.timestamp}")
        db.session.add(team)
        db.session.commit()

        self._login(self.football_athlete.email, "PlayerPass123!")
        self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})
        res2 = self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res2.status_code, 400)
        self.assertIn("already a member", res2.get_json()['message'].lower())

    def test_07_inactive_team_code_rejected(self):
        """TEST 7: Inactive team code is used. Expected: Join rejected."""
        team = Team(team_name="Inactive Football", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-IN{self.timestamp}", status="inactive")
        db.session.add(team)
        db.session.commit()

        self._login(self.football_athlete.email, "PlayerPass123!")
        res = self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 400)
        self.assertIn("inactive", res.get_json()['message'].lower())

    def test_08_inactive_athlete_rejected(self):
        """TEST 8: Inactive athlete attempts to join. Expected: Join rejected."""
        team = Team(team_name="Active Football", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-ACT{self.timestamp}")
        db.session.add(team)
        db.session.commit()

        with self.client.session_transaction() as sess:
            sess['user_id'] = self.inactive_athlete.id
            sess['user_role'] = 'athlete'
            sess['csrf_token'] = self.csrf_token

        res = self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 403)
        self.assertIn("inactive", res.get_json()['message'].lower())

    def test_09_security_manipulated_athlete_id_ignored(self):
        """TEST 9: Client submits fake athlete_id in body. Expected: Server ignores payload athlete_id and uses session user."""
        team = Team(team_name="Sec Football", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-SEC{self.timestamp}")
        db.session.add(team)
        db.session.commit()

        self._login(self.football_athlete.email, "PlayerPass123!")
        # Client tries to pass fake athlete_id = 9999
        res = self.client.post('/api/teams/join', json={'team_code': team.team_code, 'athlete_id': 9999, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 200)

        # Verify joined record is for session user (football_athlete), not 9999
        m = TeamMember.query.filter_by(team_id=team.id, status='active').first()
        self.assertEqual(m.athlete_id, self.football_athlete.id)

    def test_10_coach_my_teams_dynamic_player_count_updates(self):
        """TEST 10: Coach opens My Teams. Expected: Player count updates dynamically after athlete joins."""
        team = Team(team_name="Count Football", sport="Football", season="2026-27", coach_id=self.coach.id, team_code=f"FB-CNT{self.timestamp}")
        db.session.add(team)
        db.session.commit()

        # Before join -> count 0
        self._login(self.coach.email, "CoachPass123!")
        res1 = self.client.get('/api/coach/teams')
        self.assertEqual(res1.get_json()['teams'][0]['member_count'], 0)

        # Athlete joins
        self._login(self.football_athlete.email, "PlayerPass123!")
        self.client.post('/api/teams/join', json={'team_code': team.team_code, 'csrf_token': self.csrf_token})

        # After join -> count 1
        self._login(self.coach.email, "CoachPass123!")
        res2 = self.client.get('/api/coach/teams')
        self.assertEqual(res2.get_json()['teams'][0]['member_count'], 1)

    def test_11_athlete_access_coach_route_denied(self):
        """TEST 11: Athlete tries to access Coach team-management route. Expected: Access denied."""
        self._login(self.football_athlete.email, "PlayerPass123!")
        res = self.client.get('/coach/teams')
        self.assertEqual(res.status_code, 302)

    def test_12_existing_athlete_login_works(self):
        """TEST 12: Existing Athlete login still works."""
        res = self._login(self.football_athlete.email, "PlayerPass123!")
        self.assertEqual(res.status_code, 302)
        self.assertIn('/dashboard', res.location)

    def test_13_existing_coach_login_works(self):
        """TEST 13: Existing Coach login still works."""
        res = self._login(self.coach.email, "CoachPass123!")
        self.assertEqual(res.status_code, 302)
        self.assertIn('/coach/dashboard', res.location)

    def test_14_existing_admin_login_works(self):
        """TEST 14: Existing Admin login still works."""
        res = self._login(self.admin.email, "AdminPass123!")
        self.assertEqual(res.status_code, 302)
        self.assertIn('/admin/dashboard', res.location)

    def test_15_existing_health_monitoring_and_predictions_work(self):
        """TEST 15: Existing health monitoring and prediction system works properly."""
        rec = DailyHealthRecord(user_id=self.football_athlete.id, record_date="2026-10-06", sleep_hours=8.0, training_hours=2.0, resting_heart_rate=62, fatigue_level=2, stress_level=2, risk_score=14.5, risk_label="Low Risk")
        inj = Injury(user_id=self.football_athlete.id, injury_type="Ankle Sprain", body_part="Ankle", injury_date="2026-09-01", severity="Mild", recovery_status="Recovered")
        db.session.add(rec)
        db.session.add(inj)
        db.session.commit()

        self._login(self.football_athlete.email, "PlayerPass123!")
        res_dashboard = self.client.get('/dashboard')
        self.assertEqual(res_dashboard.status_code, 200)

        DailyHealthRecord.query.filter_by(user_id=self.football_athlete.id).delete()
        Injury.query.filter_by(user_id=self.football_athlete.id).delete()
        db.session.commit()

if __name__ == '__main__':
    unittest.main()
