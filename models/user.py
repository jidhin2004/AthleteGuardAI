from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    _legacy_age = db.Column('age', db.Integer, nullable=True)
    gender = db.Column(db.String(20), nullable=False)
    primary_sport = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Profile & Health Metric Fields
    phone = db.Column(db.String(20), nullable=True)
    height_cm = db.Column(db.Float, nullable=True)
    weight_kg = db.Column(db.Float, nullable=True)
    emergency_name = db.Column(db.String(100), nullable=True)
    emergency_relationship = db.Column(db.String(50), nullable=True)
    emergency_phone = db.Column(db.String(20), nullable=True)
    profile_photo = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(20), nullable=False, default='athlete')
    account_status = db.Column(db.String(20), nullable=False, default='active')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Hashes and stores the password securely."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the plain password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    @property
    def age(self):
        """Calculates current age dynamically from date_of_birth."""
        if not self.date_of_birth:
            return self._legacy_age or 0
        today = datetime.utcnow().date()
        dob = self.date_of_birth
        if isinstance(dob, str):
            try:
                dob = datetime.strptime(dob, '%Y-%m-%d').date()
            except ValueError:
                return self._legacy_age or 0
        calc = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            calc -= 1
        return max(0, calc)

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
        return None

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
            'date_of_birth': self.date_of_birth.strftime('%Y-%m-%d') if self.date_of_birth else None,
            'date_of_birth_formatted': self.date_of_birth.strftime('%d/%m/%Y') if self.date_of_birth else '',
            'age': self.age,
            'gender': self.gender,
            'primary_sport': self.primary_sport,
            'email': self.email,
            'phone': self.phone,
            'height_cm': self.height_cm,
            'weight_kg': self.weight_kg,
            'bmi': self.bmi,
            'bmi_category': self.bmi_category,
            'emergency_name': self.emergency_name,
            'emergency_relationship': self.emergency_relationship,
            'emergency_phone': self.emergency_phone,
            'profile_photo': self.profile_photo,
            'role': self.role or 'athlete',
            'account_status': self.account_status or 'active',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<User {self.email}>"
