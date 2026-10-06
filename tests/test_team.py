import unittest
import time
from datetime import datetime
from app import app, db, User, Team, TeamMember, DailyHealthRecord, Injury

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.timestamp = int(time.time() * 1000)
        self.csrf_token = "test_csrf_token_value_step3"

        # Create Coach A
        self.coach_a = User(
            full_name="Head Coach Alpha",
            email=f"coach_a_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=38,
            date_of_birth=datetime(1988, 1, 1).date(),
            role="coach"
        )
        self.coach_a.set_password("CoachPass123!")

        # Create Coach B
        self.coach_b = User(
            full_name="Head Coach Beta",
            email=f"coach_b_{self.timestamp}@example.com",
            gender="Female",
            primary_sport="Basketball",
            _legacy_age=40,
            date_of_birth=datetime(1986, 1, 1).date(),
            role="coach"
        )
        self.coach_b.set_password("CoachPass123!")

        # Create Athlete User
        self.athlete = User(
            full_name="Athlete Player One",
            email=f"athlete_p1_{self.timestamp}@example.com",
            gender="Male",
            primary_sport="Football",
            _legacy_age=22,
            date_of_birth=datetime(2004, 1, 1).date(),
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

    def test_01_coach_login_dashboard(self):
        """TEST 1: Coach logs in and reaches Coach Dashboard."""
        res = self._login(self.coach_a.email, "CoachPass123!")
        self.assertEqual(res.status_code, 302)
        self.assertIn('/coach/dashboard', res.location)

    def test_02_and_03_coach_create_team_and_unique_code(self):
        """TEST 2 & 3: Coach creates Football team; unique team code generated and saved to DB."""
        self._login(self.coach_a.email, "CoachPass123!")
        payload = {
            'team_name': 'College Football Squad',
            'sport': 'Football',
            'csrf_token': self.csrf_token
        }
        res = self.client.post('/api/coach/teams', json=payload)
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('team_code', data['team'])
        self.assertTrue(data['team']['team_code'].startswith('FB-'))

        team = Team.query.filter_by(team_code=data['team']['team_code']).first()
        self.assertIsNotNone(team)
        self.assertEqual(team.coach_id, self.coach_a.id)

    def test_04_coach_teams_isolation(self):
        """TEST 4: Coach opens My Teams; only that Coach's teams are returned."""
        t1 = Team(team_name="Coach A Team", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-A{self.timestamp}")
        t2 = Team(team_name="Coach B Team", sport="Basketball", coach_id=self.coach_b.id, team_code=f"BB-B{self.timestamp}")
        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get('/api/coach/teams')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['teams'][0]['team_name'], "Coach A Team")

    def test_05_athlete_joins_team_valid_code(self):
        """TEST 5: Athlete enters valid team code and joins team."""
        t1 = Team(team_name="Lions Football", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-L{self.timestamp}")
        db.session.add(t1)
        db.session.commit()

        self._login(self.athlete.email, "Password123!")
        res = self.client.post('/api/teams/join', json={'team_code': t1.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')

        m = TeamMember.query.filter_by(team_id=t1.id, athlete_id=self.athlete.id, status='active').first()
        self.assertIsNotNone(m)

    def test_06_duplicate_membership_prevented(self):
        """TEST 6: Athlete attempts to join same team code twice -> rejected."""
        t1 = Team(team_name="Tigers FC", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-T{self.timestamp}")
        db.session.add(t1)
        db.session.commit()

        self._login(self.athlete.email, "Password123!")
        self.client.post('/api/teams/join', json={'team_code': t1.team_code, 'csrf_token': self.csrf_token})
        
        # Second attempt
        res = self.client.post('/api/teams/join', json={'team_code': t1.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertIn("already an active member", data['message'].lower())

    def test_07_athlete_views_my_team(self):
        """TEST 7: Athlete opens My Team endpoint and views correct membership data."""
        t1 = Team(team_name="Eagles Squad", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-E{self.timestamp}")
        db.session.add(t1)
        db.session.commit()
        m = TeamMember(team_id=t1.id, athlete_id=self.athlete.id, status='active')
        db.session.add(m)
        db.session.commit()

        self._login(self.athlete.email, "Password123!")
        res = self.client.get('/api/my-team')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['teams'][0]['team_name'], "Eagles Squad")
        self.assertEqual(data['teams'][0]['coach_name'], "Head Coach Alpha")

    def test_08_coach_views_team_members(self):
        """TEST 8: Coach opens team details and views active members."""
        t1 = Team(team_name="Panthers Football", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-P{self.timestamp}")
        db.session.add(t1)
        db.session.commit()
        m = TeamMember(team_id=t1.id, athlete_id=self.athlete.id, status='active')
        db.session.add(m)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{t1.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['member_count'], 1)
        self.assertEqual(data['members'][0]['athlete_name'], "Athlete Player One")

    def test_09_coach_removes_athlete_preserves_data(self):
        """TEST 9: Coach removes athlete; membership deactivated; user account, health & medical records preserved."""
        t1 = Team(team_name="Bears FC", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-B{self.timestamp}")
        db.session.add(t1)
        db.session.commit()
        m = TeamMember(team_id=t1.id, athlete_id=self.athlete.id, status='active')
        db.session.add(m)
        
        rec = DailyHealthRecord(user_id=self.athlete.id, record_date="2026-09-20", sleep_hours=8.0, training_hours=2.0, resting_heart_rate=60, fatigue_level=2, stress_level=2, risk_score=15.0, risk_label="Low Risk")
        inj = Injury(user_id=self.athlete.id, injury_type="Hamstring Strain", body_part="Thigh", injury_date="2026-08-01", severity="Mild", recovery_status="Recovered")
        db.session.add(rec)
        db.session.add(inj)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.post(f'/api/coach/teams/{t1.id}/members/{self.athlete.id}/remove', json={'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 200)

        m_check = TeamMember.query.filter_by(team_id=t1.id, athlete_id=self.athlete.id).first()
        self.assertEqual(m_check.status, 'removed')

        self.assertIsNotNone(User.query.get(self.athlete.id))
        self.assertIsNotNone(DailyHealthRecord.query.filter_by(user_id=self.athlete.id).first())
        self.assertIsNotNone(Injury.query.filter_by(user_id=self.athlete.id).first())

        DailyHealthRecord.query.filter_by(user_id=self.athlete.id).delete()
        Injury.query.filter_by(user_id=self.athlete.id).delete()
        db.session.commit()

    def test_10_coach_a_cannot_access_coach_b_team(self):
        """TEST 10: Coach A attempts to view Coach B's team -> Denied (HTTP 403)."""
        t2 = Team(team_name="Coach B Private Team", sport="Basketball", coach_id=self.coach_b.id, team_code=f"BB-PB{self.timestamp}")
        db.session.add(t2)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.get(f'/api/coach/teams/{t2.id}')
        self.assertEqual(res.status_code, 403)

    def test_11_athlete_cannot_access_coach_team_routes(self):
        """TEST 11: Athlete attempts to access coach team-management route -> Redirected/Denied (302)."""
        self._login(self.athlete.email, "Password123!")
        res = self.client.get('/coach/teams')
        self.assertEqual(res.status_code, 302) # Redirects to dashboard with flash message

    def test_12_unauthenticated_user_team_access(self):
        """TEST 12: Unauthenticated user attempts team access -> Login required redirect (302)."""
        res1 = self.client.get('/coach/teams')
        self.assertEqual(res1.status_code, 302)
        res2 = self.client.get('/join-team')
        self.assertEqual(res2.status_code, 302)

    def test_13_athlete_cannot_create_team(self):
        """TEST 13: Athlete attempts to create a team -> Denied (302 redirect or 403)."""
        self._login(self.athlete.email, "Password123!")
        res = self.client.post('/api/coach/teams', json={'team_name': 'Unauthorized Team', 'sport': 'Football', 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 302)

    def test_14_coach_cannot_join_team_via_athlete_endpoint(self):
        """TEST 14: Coach attempts to join team using athlete endpoint -> Denied (403)."""
        t1 = Team(team_name="Spartans Squad", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-S{self.timestamp}")
        db.session.add(t1)
        db.session.commit()

        self._login(self.coach_a.email, "CoachPass123!")
        res = self.client.post('/api/teams/join', json={'team_code': t1.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 403)

    def test_15_inactive_team_code_rejected(self):
        """TEST 15: Athlete tries to join an inactive team code -> Joining rejected."""
        t_inact = Team(team_name="Inactive Squad", sport="Football", coach_id=self.coach_a.id, team_code=f"FB-IN{self.timestamp}", status="inactive")
        db.session.add(t_inact)
        db.session.commit()

        self._login(self.athlete.email, "Password123!")
        res = self.client.post('/api/teams/join', json={'team_code': t_inact.team_code, 'csrf_token': self.csrf_token})
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertIn("inactive", data['message'].lower())

if __name__ == '__main__':
    unittest.main()
