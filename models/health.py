from datetime import datetime
from models import db

class DailyHealthRecord(db.Model):
    __tablename__ = 'daily_health_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    record_date = db.Column(db.String(10), nullable=False, index=True) # YYYY-MM-DD
    
    sleep_hours = db.Column(db.Float, nullable=False, default=8.0)
    training_hours = db.Column(db.Float, nullable=False, default=2.0)
    resting_heart_rate = db.Column(db.Integer, nullable=False, default=65)
    fatigue_level = db.Column(db.Integer, nullable=False, default=3) # 1 - 10
    stress_level = db.Column(db.Integer, nullable=False, default=3)  # 1 - 10
    previous_injury = db.Column(db.Boolean, nullable=False, default=False)
    injury_details = db.Column(db.String(255), nullable=True)

    risk_score = db.Column(db.Float, nullable=True)
    risk_label = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'record_date', name='uq_user_daily_record'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'record_date': self.record_date,
            'sleep_hours': float(self.sleep_hours),
            'training_hours': float(self.training_hours),
            'resting_heart_rate': int(self.resting_heart_rate),
            'fatigue_level': int(self.fatigue_level),
            'stress_level': int(self.stress_level),
            'previous_injury': bool(self.previous_injury),
            'injury_details': self.injury_details or '',
            'risk_score': round(float(self.risk_score), 1) if self.risk_score is not None else None,
            'risk_label': self.risk_label or 'Not Calculated',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
