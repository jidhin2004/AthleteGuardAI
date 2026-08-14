from datetime import datetime
from models import db

class Injury(db.Model):
    __tablename__ = 'injuries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    injury_type = db.Column(db.String(100), nullable=False) # e.g. Hamstring Strain
    body_part = db.Column(db.String(100), nullable=False)   # e.g. Left Thigh
    injury_date = db.Column(db.String(20), nullable=False)   # e.g. 2026-03-12 or 12 March 2026
    severity = db.Column(db.String(30), nullable=False)      # Mild, Moderate, Severe
    treatment = db.Column(db.String(150), nullable=True)     # Physiotherapy, Rest, Surgery
    recovery_status = db.Column(db.String(30), nullable=False)# Recovered, Under Treatment, Ongoing
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'injury_type': self.injury_type,
            'body_part': self.body_part,
            'injury_date': self.injury_date,
            'severity': self.severity,
            'treatment': self.treatment or 'N/A',
            'recovery_status': self.recovery_status,
            'notes': self.notes or '',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class MedicalCondition(db.Model):
    __tablename__ = 'medical_conditions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    condition_name = db.Column(db.String(100), nullable=False) # e.g. Asthma, Hypertension
    diagnosis_date = db.Column(db.String(20), nullable=True)   # e.g. 2025-06-10
    status = db.Column(db.String(30), nullable=False)          # Active, Managed, Resolved
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'condition_name': self.condition_name,
            'diagnosis_date': self.diagnosis_date or 'N/A',
            'status': self.status,
            'notes': self.notes or '',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Allergy(db.Model):
    __tablename__ = 'allergies'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    allergy_name = db.Column(db.String(100), nullable=False) # e.g. Penicillin, Peanuts
    allergy_type = db.Column(db.String(50), nullable=False)   # Medication, Food, Environmental, Other
    reaction = db.Column(db.String(150), nullable=True)      # Skin Rash, Anaphylaxis
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'allergy_name': self.allergy_name,
            'allergy_type': self.allergy_type,
            'reaction': self.reaction or 'N/A',
            'notes': self.notes or '',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Medication(db.Model):
    __tablename__ = 'medications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    medication_name = db.Column(db.String(100), nullable=False) # e.g. Albuterol, Ibuprofen
    dosage = db.Column(db.String(50), nullable=True)            # e.g. 200mg
    frequency = db.Column(db.String(50), nullable=True)         # Once Daily, As Needed
    start_date = db.Column(db.String(20), nullable=True)
    end_date = db.Column(db.String(20), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'medication_name': self.medication_name,
            'dosage': self.dosage or 'N/A',
            'frequency': self.frequency or 'N/A',
            'start_date': self.start_date or 'N/A',
            'end_date': self.end_date or 'Ongoing',
            'notes': self.notes or '',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Surgery(db.Model):
    __tablename__ = 'surgeries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    surgery_name = db.Column(db.String(120), nullable=False)  # e.g. ACL Reconstruction
    body_part = db.Column(db.String(100), nullable=False)     # e.g. Right Knee
    surgery_date = db.Column(db.String(20), nullable=False)    # e.g. 2024-05-15
    hospital_clinic = db.Column(db.String(150), nullable=True)# e.g. Sports Health Medical Center
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'surgery_name': self.surgery_name,
            'body_part': self.body_part,
            'surgery_date': self.surgery_date,
            'hospital_clinic': self.hospital_clinic or 'N/A',
            'notes': self.notes or '',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
