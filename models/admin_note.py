from datetime import datetime
from models import db

class AdminNote(db.Model):
    __tablename__ = 'admin_notes'

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    prediction_id = db.Column(db.Integer, db.ForeignKey('daily_health_records.id'), nullable=False, index=True)
    note = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        from models.user import User
        admin_user = User.query.get(self.admin_id)
        return {
            'id': self.id,
            'admin_id': self.admin_id,
            'admin_name': admin_user.full_name if admin_user else 'Admin',
            'athlete_id': self.athlete_id,
            'prediction_id': self.prediction_id,
            'note': self.note,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'created_at_formatted': self.created_at.strftime('%b %d, %Y %I:%M %p') if self.created_at else ''
        }
