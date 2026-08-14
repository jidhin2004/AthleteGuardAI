from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    primary_sport = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Profile & Health Metric Fields
    phone = db.Column(db.String(20), nullable=True, default='+91 98765 43210')
    height_cm = db.Column(db.Float, nullable=True, default=175.0)
    weight_kg = db.Column(db.Float, nullable=True, default=70.0)
    emergency_name = db.Column(db.String(100), nullable=True, default='Emergency Contact')
    emergency_relationship = db.Column(db.String(50), nullable=True, default='Parent / Guardian')
    emergency_phone = db.Column(db.String(20), nullable=True, default='+91 91234 56789')
    profile_photo = db.Column(db.String(255), nullable=True) # Relative path: /static/uploads/profile_photos/ath_0001.jpg
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Hashes and stores the password securely."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the plain password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    @property
    def athlete_id(self):
        """Generates a standardized Athlete ID string (e.g. ATH-0001)."""
        return f"ATH-{self.id:04d}"

    @property
    def initials(self):
        """Generates fallback initials from Full Name (e.g. Marcus Vance -> MV)."""
        if not self.full_name:
            return "M"
        parts = self.full_name.strip().split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[1][0]}".upper()
        return self.full_name[0].upper()

    @property
    def bmi(self):
        """Calculates Body Mass Index (BMI) dynamically from weight (kg) and height (cm)."""
        if self.height_cm and self.height_cm > 0 and self.weight_kg and self.weight_kg > 0:
            height_m = self.height_cm / 100.0
            return round(self.weight_kg / (height_m * height_m), 1)
        return 22.9

    @property
    def bmi_category(self):
        """Determines standard BMI classification and styling badge."""
        val = self.bmi
        if val is None:
            return {'label': 'N/A', 'badge_class': 'badge bg-secondary'}
        if val < 18.5:
            return {'label': 'Underweight', 'badge_class': 'badge bg-info text-dark'}
        elif 18.5 <= val <= 24.9:
            return {'label': 'Normal', 'badge_class': 'badge bg-success'}
        elif 25.0 <= val <= 29.9:
            return {'label': 'Overweight', 'badge_class': 'badge bg-warning text-dark'}
        else:
            return {'label': 'Obese', 'badge_class': 'badge bg-danger'}

    def to_dict(self):
        return {
            'id': self.id,
            'athlete_id': self.athlete_id,
            'full_name': self.full_name,
            'initials': self.initials,
            'age': self.age,
            'gender': self.gender,
            'primary_sport': self.primary_sport,
            'email': self.email,
            'phone': self.phone or '+91 98765 43210',
            'height_cm': self.height_cm or 175.0,
            'weight_kg': self.weight_kg or 70.0,
            'bmi': self.bmi,
            'bmi_category': self.bmi_category,
            'emergency_name': self.emergency_name or 'Emergency Contact',
            'emergency_relationship': self.emergency_relationship or 'Parent / Guardian',
            'emergency_phone': self.emergency_phone or '+91 91234 56789',
            'profile_photo': self.profile_photo,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<User {self.email}>"
