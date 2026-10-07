from datetime import datetime
from models import db

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False)
    sport = db.Column(db.String(50), nullable=False)
    season = db.Column(db.String(30), nullable=True, default='2026-27')
    description = db.Column(db.Text, nullable=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    team_code = db.Column(db.String(20), unique=True, nullable=False, index=True)
    status = db.Column(db.String(20), default='active', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        from models.user import User
        coach = db.session.get(User, self.coach_id)
        active_members_count = TeamMember.query.filter_by(team_id=self.id, status='active').count()
        return {
            'id': self.id,
            'team_name': self.team_name,
            'sport': self.sport,
            'season': self.season or '2026-27',
            'description': self.description or '',
            'coach_id': self.coach_id,
            'coach_name': coach.full_name if coach else 'Unknown Coach',
            'coach_email': coach.email if coach else '',
            'team_code': self.team_code,
            'status': self.status,
            'member_count': active_members_count,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'created_at_formatted': self.created_at.strftime('%b %d, %Y') if self.created_at else ''
        }


class TeamMember(db.Model):
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False, index=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    status = db.Column(db.String(20), default='active', nullable=False)  # 'active', 'removed', 'left'
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('team_id', 'athlete_id', name='uq_team_athlete'),
    )

    def to_dict(self):
        from models.user import User
        athlete = User.query.get(self.athlete_id)
        team = Team.query.get(self.team_id)
        coach = User.query.get(team.coach_id) if team else None

        return {
            'id': self.id,
            'team_id': self.team_id,
            'athlete_id': self.athlete_id,
            'athlete_name': athlete.full_name if athlete else 'Unknown Athlete',
            'athlete_email': athlete.email if athlete else '',
            'athlete_code': athlete.athlete_id if athlete else f"ATH-{self.athlete_id:04d}",
            'athlete_sport': athlete.primary_sport if athlete else '',
            'athlete_photo': athlete.profile_photo if athlete else None,
            'team_name': team.team_name if team else 'Unknown Team',
            'team_code': team.team_code if team else '',
            'team_sport': team.sport if team else '',
            'team_season': team.season if (team and team.season) else '2026-27',
            'team_description': team.description if (team and team.description) else '',
            'coach_id': team.coach_id if team else None,
            'coach_name': coach.full_name if coach else 'Unknown Coach',
            'status': self.status,
            'joined_at': self.joined_at.isoformat() if self.joined_at else None,
            'joined_at_formatted': self.joined_at.strftime('%b %d, %Y') if self.joined_at else ''
        }
