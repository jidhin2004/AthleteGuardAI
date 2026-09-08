from datetime import datetime
from models import db

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    message = db.Column(db.Text, nullable=False)
    related_prediction_id = db.Column(db.Integer, db.ForeignKey('daily_health_records.id'), nullable=True, index=True)
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        from models.user import User
        admin_user = User.query.get(self.admin_id)
        return {
            'id': self.id,
            'athlete_id': self.athlete_id,
            'admin_id': self.admin_id,
            'admin_name': admin_user.full_name if admin_user else 'Administrator',
            'message': self.message,
            'related_prediction_id': self.related_prediction_id,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'created_at_formatted': self.created_at.strftime('%b %d, %Y %I:%M %p') if self.created_at else ''
        }
