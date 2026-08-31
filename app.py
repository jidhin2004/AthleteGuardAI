import os
import time
import base64
from datetime import datetime
from functools import wraps
from urllib.parse import quote_plus
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, inspect, text
from models import db
from models.user import User
from models.medical import Injury, MedicalCondition, Allergy, Medication, Surgery
from models.health import DailyHealthRecord
from services.ml_service import ml_service

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "athleteguard_ai_secret_key_mca_2026")

# Profile Upload Configuration
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads', 'profile_photos')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}
MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB

# MySQL Configuration (Primary Active Database)
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "AthleteGuard@2026!")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_NAME = os.environ.get("DB_NAME", "athleteguard_db")

USE_MYSQL = os.environ.get("USE_MYSQL", "true").lower() == "true"
SQLITE_URI = "sqlite:///athleteguard_dev.db"

encoded_password = quote_plus(DB_PASSWORD)
MYSQL_URI = f"mysql+pymysql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

selected_uri = SQLITE_URI
if USE_MYSQL:
    try:
        # Test MySQL Connection and Verify Database & Required Tables
        engine = create_engine(MYSQL_URI, connect_args={"connect_timeout": 5})
        with engine.connect() as conn:
            res = conn.execute(text("SELECT DATABASE()")).fetchone()
            current_db = res[0] if res else None
            
            inspector = inspect(engine)
            existing_tables = set(inspector.get_table_names())
            required_tables = {'users', 'daily_health_records', 'injuries', 'medical_conditions', 'allergies', 'medications', 'surgeries'}
            missing = required_tables - existing_tables
            if missing:
                raise RuntimeError(f"Connected to MySQL database '{current_db}', but missing required tables: {missing}")

        selected_uri = MYSQL_URI
        print(f"==================================================")
        print(f"[SUCCESS] Connected to ACTIVE MySQL database: '{current_db}' on {DB_HOST}:{DB_PORT}")
        print(f"[VERIFIED TABLES] All {len(required_tables)} required AthleteGuard AI tables exist in MySQL.")
        print(f"==================================================")
    except Exception as e:
        print(f"==================================================")
        print(f"[FATAL DATABASE ERROR] Failed to connect to MySQL database '{DB_NAME}' on {DB_HOST}:{DB_PORT}")
        print(f"Details: {e}")
        print(f"==================================================")
        raise RuntimeError(f"MySQL Connection Error: Failed to connect to MySQL database '{DB_NAME}'. Details: {e}")
else:
    selected_uri = SQLITE_URI
    print(f"[NOTE] Running with manual fallback SQLite database: {SQLITE_URI}")

app.config['SQLALCHEMY_DATABASE_URI'] = selected_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)

with app.app_context():
    db.create_all()
    # Migration helper: ensure 'role' column exists in 'users' table without data loss
    try:
        inspector = inspect(db.engine)
        columns = [c['name'] for c in inspector.get_columns('users')]
        if 'role' not in columns:
            db.session.execute(text("ALTER TABLE users ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT 'athlete'"))
            db.session.commit()
            print("Successfully verified database schema: 'role' column present in 'users' table.")
    except Exception as e:
        print(f"Database schema verification note: {e}")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def login_required(f):
    """Decorator to require login for protected routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in to access your AthleteGuard AI Dashboard.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """Decorator to restrict access strictly to authenticated Admin users."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in with Admin credentials to access the Admin Panel.", "warning")
            return redirect(url_for('login'))

        user_id = session.get('user_id')
        user = User.query.get(user_id)
        if not user or user.role != 'admin':
            flash("Access denied. Admin privileges are required to view this page.", "danger")
            return redirect(url_for('dashboard'))

        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    """Public Landing Page route."""
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login handler with password verification, role management, and session routing."""
    if 'user_id' in session:
        user_role = session.get('user_role')
        if user_role == 'admin':
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        remember = request.form.get('remember')

        if not email or not password:
            flash("Please enter both Athlete ID/Email and password.", "danger")
            return render_template('login.html')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session.permanent = True if remember else False
            session['user_id'] = user.id
            session['user_name'] = user.full_name
            session['user_email'] = user.email
            session['user_sport'] = user.primary_sport
            session['user_role'] = user.role or 'athlete'

            flash(f"Welcome back, {user.full_name}!", "success")
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid Athlete ID/Email or password. Please try again.", "danger")
            return render_template('login.html', error_msg="Invalid credentials. Please check your email and password.")

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration handler with password hashing and database storage."""
    if 'user_id' in session:
        user_role = session.get('user_role')
        if user_role == 'admin':
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        age = request.form.get('age', '').strip()
        gender = request.form.get('gender', '').strip()
        primary_sport = request.form.get('primary_sport', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not all([full_name, age, gender, primary_sport, email, password]):
            flash("All fields are required for registration.", "danger")
            return render_template('register.html')

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('register.html')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("An account with this email address already exists.", "warning")
            return render_template('register.html', error_msg="Email already registered. Try logging in instead.")

        try:
            # SECURITY: Hardcode role='athlete' on the backend regardless of client inputs
            new_user = User(
                full_name=full_name,
                age=int(age),
                gender=gender,
                primary_sport=primary_sport,
                email=email,
                role='athlete'
            )
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id
            session['user_name'] = new_user.full_name
            session['user_email'] = new_user.email
            session['user_sport'] = new_user.primary_sport
            session['user_role'] = new_user.role

            flash("Athlete Account created successfully! Welcome to your Dashboard.", "success")
            return redirect(url_for('dashboard'))

        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred during registration: {str(e)}", "danger")
            return render_template('register.html')

    return render_template('register.html')


# ==========================================
# ADMIN PAGE ROUTES & REST APIs
# ==========================================

@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    """Admin Dashboard Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('admin/dashboard.html', user=user)


@app.route('/admin/athletes')
@admin_required
def admin_athletes():
    """Admin Registered Athletes Management Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('admin/athletes.html', user=user)


@app.route('/admin/athletes/<int:user_id>')
@admin_required
def admin_athlete_detail(user_id):
    """Admin Read-Only Athlete Detail & Health Audit Page."""
    user = User.query.get(session.get('user_id'))
    athlete = User.query.filter_by(id=user_id, role='athlete').first_or_404()
    return render_template('admin/athlete_detail.html', user=user, athlete=athlete)


@app.route('/admin/health-records')
@admin_required
def admin_health_records():
    """Admin Daily Health Monitoring Records Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('admin/health_records.html', user=user)


@app.route('/admin/predictions')
@admin_required
def admin_predictions():
    """Admin Global Prediction Records Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('admin/predictions.html', user=user)


# ==========================================
# ADMIN REST APIs
# ==========================================

@app.route('/api/admin/stats', methods=['GET'])
@admin_required
def get_admin_stats():
    """API Endpoint returning live database statistics & risk distribution for Admin Dashboard."""
    try:
        total_athletes = User.query.filter(User.role == 'athlete').count()
        total_health_records = DailyHealthRecord.query.count()
        total_predictions = DailyHealthRecord.query.filter(DailyHealthRecord.risk_score.isnot(None)).count()
        
        low_risk_count = DailyHealthRecord.query.filter(DailyHealthRecord.risk_label.ilike('%low%')).count()
        medium_risk_count = DailyHealthRecord.query.filter(DailyHealthRecord.risk_label.ilike('%medium%')).count()
        high_risk_count = DailyHealthRecord.query.filter(DailyHealthRecord.risk_label.ilike('%high%')).count()

        # Recent Athletes (Latest 5 ordered by created_at)
        recent_athletes_query = User.query.filter(User.role == 'athlete').order_by(User.created_at.desc(), User.id.desc()).limit(5).all()
        recent_athletes = [a.to_dict() for a in recent_athletes_query]

        # Recent Predictions (Latest 5 ordered by created_at)
        recent_preds_query = DailyHealthRecord.query.filter(DailyHealthRecord.risk_score.isnot(None)).order_by(DailyHealthRecord.created_at.desc(), DailyHealthRecord.id.desc()).limit(5).all()
        recent_predictions = []
        for p in recent_preds_query:
            ath = User.query.get(p.user_id)
            rec_dict = p.to_dict()
            rec_dict['athlete_name'] = ath.full_name if ath else 'Unknown Athlete'
            rec_dict['athlete_sport'] = ath.primary_sport if ath else 'N/A'
            recent_predictions.append(rec_dict)

        return jsonify({
            'status': 'success',
            'stats': {
                'total_athletes': total_athletes,
                'total_health_records': total_health_records,
                'total_predictions': total_predictions,
                'low_risk_count': low_risk_count,
                'medium_risk_count': medium_risk_count,
                'high_risk_count': high_risk_count
            },
            'risk_distribution': {
                'labels': ['Low Risk', 'Medium Risk', 'High Risk'],
                'counts': [low_risk_count, medium_risk_count, high_risk_count],
                'colors': ['#22c55e', '#f59e0b', '#ef4444']
            },
            'recent_athletes': recent_athletes,
            'recent_predictions': recent_predictions
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Unable to load dashboard data. Please try again.'}), 500


@app.route('/api/admin/athletes', methods=['GET'])
@admin_required
def get_admin_athletes():
    """API Endpoint returning list of registered athletes with search & sport filtering."""
    try:
        query_str = request.args.get('q', '').strip().lower()
        sport_filter = request.args.get('sport', '').strip().lower()

        athletes_query = User.query.filter(User.role == 'athlete').order_by(User.created_at.desc(), User.id.desc()).all()
        result = []

        for ath in athletes_query:
            # Sport Filter
            if sport_filter and sport_filter != 'all':
                if ath.primary_sport.lower() != sport_filter:
                    continue

            # Search Filter (Name, Email, Athlete ID, Sport)
            if query_str:
                matches = (
                    query_str in ath.full_name.lower() or
                    query_str in ath.email.lower() or
                    query_str in ath.athlete_id.lower() or
                    query_str in ath.primary_sport.lower()
                )
                if not matches:
                    continue

            result.append(ath.to_dict())

        return jsonify({
            'status': 'success',
            'count': len(result),
            'athletes': result
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Unable to load athletes roster. Please try again.'}), 500


@app.route('/api/admin/athletes/<int:user_id>', methods=['GET'])
@admin_required
def get_admin_athlete_detail(user_id):
    """API Endpoint returning deep read-only profile & health overview for a specific athlete."""
    try:
        athlete = User.query.filter_by(id=user_id, role='athlete').first()
        if not athlete:
            return jsonify({'status': 'error', 'message': 'Athlete record not found.'}), 404

        # Query Medical History Records
        injuries = Injury.query.filter_by(user_id=user_id).order_by(Injury.id.desc()).all()
        conditions = MedicalCondition.query.filter_by(user_id=user_id).order_by(MedicalCondition.id.desc()).all()
        allergies = Allergy.query.filter_by(user_id=user_id).order_by(Allergy.id.desc()).all()
        medications = Medication.query.filter_by(user_id=user_id).order_by(Medication.id.desc()).all()
        surgeries = Surgery.query.filter_by(user_id=user_id).order_by(Surgery.id.desc()).all()

        # Query Daily Health & Prediction Records
        health_records = DailyHealthRecord.query.filter_by(user_id=user_id).order_by(DailyHealthRecord.record_date.desc(), DailyHealthRecord.id.desc()).all()

        # Calculate Summary Averages & Trends
        pred_records = [r for r in health_records if r.risk_score is not None]
        total_predictions = len(pred_records)
        latest_risk = pred_records[0].to_dict() if pred_records else None

        avg_sleep = round(sum(r.sleep_hours for r in health_records) / len(health_records), 1) if health_records else 0.0
        avg_training = round(sum(r.training_hours for r in health_records) / len(health_records), 1) if health_records else 0.0
        avg_hr = round(sum(r.resting_heart_rate for r in health_records) / len(health_records), 1) if health_records else 0.0
        avg_fatigue = round(sum(r.fatigue_level for r in health_records) / len(health_records), 1) if health_records else 0.0
        avg_stress = round(sum(r.stress_level for r in health_records) / len(health_records), 1) if health_records else 0.0

        low_count = sum(1 for r in pred_records if 'low' in (r.risk_label or '').lower())
        med_count = sum(1 for r in pred_records if 'medium' in (r.risk_label or '').lower())
        high_count = sum(1 for r in pred_records if 'high' in (r.risk_label or '').lower())

        # Recent 7 chronological records for trend chart
        chronological_records = sorted(health_records[:7], key=lambda x: x.record_date)
        trend_labels = [r.record_date for r in chronological_records]
        trend_sleep = [r.sleep_hours for r in chronological_records]
        trend_training = [r.training_hours for r in chronological_records]
        trend_hr = [r.resting_heart_rate for r in chronological_records]
        trend_risk = [r.risk_score if r.risk_score is not None else 0 for r in chronological_records]

        return jsonify({
            'status': 'success',
            'athlete': athlete.to_dict(),
            'summary_stats': {
                'total_predictions': total_predictions,
                'latest_risk': latest_risk,
                'avg_sleep': avg_sleep,
                'avg_training': avg_training,
                'avg_hr': avg_hr,
                'avg_fatigue': avg_fatigue,
                'avg_stress': avg_stress,
                'low_count': low_count,
                'med_count': med_count,
                'high_count': high_count
            },
            'medical_history': {
                'injuries': [i.to_dict() for i in injuries],
                'conditions': [c.to_dict() for c in conditions],
                'allergies': [a.to_dict() for a in allergies],
                'medications': [m.to_dict() for m in medications],
                'surgeries': [s.to_dict() for s in surgeries]
            },
            'health_records': [r.to_dict() for r in health_records],
            'predictions': [r.to_dict() for r in pred_records],
            'trends': {
                'labels': trend_labels,
                'sleep': trend_sleep,
                'training': trend_training,
                'resting_hr': trend_hr,
                'risk_score': trend_risk
            }
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Unable to load athlete details. Please try again.'}), 500


@app.route('/api/admin/health-records', methods=['GET'])
@admin_required
def get_admin_health_records():
    """API Endpoint returning global daily health monitoring log across all athletes."""
    try:
        query_str = request.args.get('q', '').strip().lower()
        records = DailyHealthRecord.query.order_by(DailyHealthRecord.record_date.desc(), DailyHealthRecord.id.desc()).all()
        
        result = []
        for r in records:
            ath = User.query.get(r.user_id)
            if not ath or ath.role == 'admin':
                continue

            rec_dict = r.to_dict()
            rec_dict['athlete_name'] = ath.full_name
            rec_dict['athlete_id'] = ath.athlete_id
            rec_dict['primary_sport'] = ath.primary_sport

            if query_str:
                matches = (
                    query_str in ath.full_name.lower() or
                    query_str in ath.athlete_id.lower() or
                    query_str in ath.primary_sport.lower() or
                    query_str in r.record_date.lower() or
                    query_str in (r.injury_details or '').lower()
                )
                if not matches:
                    continue

            result.append(rec_dict)

        return jsonify({
            'status': 'success',
            'count': len(result),
            'records': result
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Unable to load health records. Please try again.'}), 500


@app.route('/api/admin/predictions', methods=['GET'])
@admin_required
def get_admin_predictions():
    """API Endpoint returning global prediction records across all athletes with risk filter."""
    try:
        risk_filter = request.args.get('risk_level', '').strip().lower()
        query_str = request.args.get('q', '').strip().lower()

        records = DailyHealthRecord.query.filter(DailyHealthRecord.risk_score.isnot(None)).order_by(DailyHealthRecord.record_date.desc(), DailyHealthRecord.id.desc()).all()
        
        result = []
        for r in records:
            ath = User.query.get(r.user_id)
            if not ath or ath.role == 'admin':
                continue

            rec_dict = r.to_dict()
            rec_dict['athlete_name'] = ath.full_name
            rec_dict['athlete_id'] = ath.athlete_id
            rec_dict['primary_sport'] = ath.primary_sport

            # Risk Filter
            if risk_filter and risk_filter != 'all':
                if risk_filter not in (r.risk_label or '').lower():
                    continue

            # Search Filter
            if query_str:
                matches = (
                    query_str in ath.full_name.lower() or
                    query_str in ath.athlete_id.lower() or
                    query_str in ath.primary_sport.lower() or
                    query_str in (r.risk_label or '').lower() or
                    query_str in r.record_date.lower()
                )
                if not matches:
                    continue

            result.append(rec_dict)

        return jsonify({
            'status': 'success',
            'count': len(result),
            'records': result
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Unable to load prediction records. Please try again.'}), 500


@app.route('/logout')
def logout():
    """Session logout handler."""
    session.clear()
    flash("You have been signed out safely.", "info")
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Athlete Dashboard - Protected Route."""
    user = User.query.get(session.get('user_id'))
    if not user:
        session.clear()
        return redirect(url_for('login'))

    dashboard_data = {
        'injury_risk_percent': 18,
        'risk_level': 'Low Risk',
        'risk_badge_color': 'success',
        'last_prediction_date': '14 August 2026',
        'total_predictions': 12,
        'avg_sleep': 7.4,
        'avg_training': 3.2,
        'has_predictions': True
    }

    return render_template('dashboard.html', user=user, data=dashboard_data)


# ==========================================
# ATHLETE PROFILE MANAGEMENT & PHOTO UPLOAD
# ==========================================

@app.route('/profile')
@login_required
def profile():
    """Athlete Profile Management Page."""
    user = User.query.get(session.get('user_id'))
    if not user:
        session.clear()
        return redirect(url_for('login'))
    return render_template('profile.html', user=user)


@app.route('/api/profile', methods=['GET', 'POST'])
@login_required
def api_profile():
    """API Endpoint for fetching and updating Athlete Profile information."""
    user = User.query.get(session.get('user_id'))
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    if request.method == 'GET':
        return jsonify({'status': 'success', 'user': user.to_dict()})

    data = request.get_json() or request.form.to_dict()

    full_name = data.get('full_name', '').strip()
    email = data.get('email', '').strip()
    age = data.get('age')
    gender = data.get('gender', '').strip()
    phone = data.get('phone', '').strip()
    primary_sport = data.get('primary_sport', '').strip()
    height_cm = data.get('height_cm')
    weight_kg = data.get('weight_kg')
    emergency_name = data.get('emergency_name', '').strip()
    emergency_relationship = data.get('emergency_relationship', '').strip()
    emergency_phone = data.get('emergency_phone', '').strip()

    if not full_name:
        return jsonify({'status': 'error', 'message': 'Full Name cannot be empty.'}), 400

    if not email or '@' not in email:
        return jsonify({'status': 'error', 'message': 'Please enter a valid email address.'}), 400

    try:
        age_val = int(age)
        if age_val <= 0 or age_val > 120:
            return jsonify({'status': 'error', 'message': 'Age must be a valid positive number.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Age must be a valid number.'}), 400

    try:
        height_val = float(height_cm) if height_cm else 175.0
        if height_val <= 0 or height_val > 300:
            return jsonify({'status': 'error', 'message': 'Height must be a positive number.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Height must be a valid number.'}), 400

    try:
        weight_val = float(weight_kg) if weight_kg else 70.0
        if weight_val <= 0 or weight_val > 500:
            return jsonify({'status': 'error', 'message': 'Weight must be a positive number.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Weight must be a valid number.'}), 400

    try:
        user.full_name = full_name
        user.email = email
        user.age = age_val
        user.gender = gender if gender else user.gender
        user.phone = phone if phone else user.phone
        user.primary_sport = primary_sport if primary_sport else user.primary_sport
        user.height_cm = height_val
        user.weight_kg = weight_val
        user.emergency_name = emergency_name if emergency_name else user.emergency_name
        user.emergency_relationship = emergency_relationship if emergency_relationship else user.emergency_relationship
        user.emergency_phone = emergency_phone if emergency_phone else user.emergency_phone

        db.session.commit()

        session['user_name'] = user.full_name
        session['user_email'] = user.email
        session['user_sport'] = user.primary_sport

        return jsonify({
            'status': 'success',
            'message': 'Profile updated successfully.',
            'user': user.to_dict()
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update your profile. Please try again.'}), 500


@app.route('/api/profile/photo', methods=['POST'])
@login_required
def upload_profile_photo():
    """API Endpoint for uploading and persisting athlete profile photo."""
    user = User.query.get(session.get('user_id'))
    if not user:
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

    filename_saved = None
    ext = 'jpg'

    if 'profile_photo' in request.files:
        file = request.files['profile_photo']
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file.'}), 400

        if not allowed_file(file.filename):
            return jsonify({'status': 'error', 'message': 'Please upload a JPG, PNG, or WEBP image under 5 MB.'}), 400

        ext = file.filename.rsplit('.', 1)[1].lower()
        file_bytes = file.read()

        if len(file_bytes) > MAX_FILE_SIZE_BYTES:
            return jsonify({'status': 'error', 'message': 'Please upload a JPG, PNG, or WEBP image under 5 MB.'}), 400

        filename_saved = f"ath_{user.id:04d}.{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename_saved)
        
        with open(filepath, 'wb') as f:
            f.write(file_bytes)

    elif request.is_json and 'photo_base64' in request.json:
        base64_data = request.json['photo_base64']
        if ',' in base64_data:
            header, base64_data = base64_data.split(',', 1)
            if 'png' in header:
                ext = 'png'
            elif 'webp' in header:
                ext = 'webp'

        try:
            image_bytes = base64.b64decode(base64_data)
            if len(image_bytes) > MAX_FILE_SIZE_BYTES:
                return jsonify({'status': 'error', 'message': 'Please upload a JPG, PNG, or WEBP image under 5 MB.'}), 400

            filename_saved = f"ath_{user.id:04d}.{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename_saved)

            with open(filepath, 'wb') as f:
                f.write(image_bytes)
        except Exception as e:
            return jsonify({'status': 'error', 'message': 'Invalid image format.'}), 400
    else:
        return jsonify({'status': 'error', 'message': 'No image file provided.'}), 400

    try:
        timestamp = int(time.time())
        relative_url = f"/static/uploads/profile_photos/{filename_saved}?t={timestamp}"
        user.profile_photo = relative_url

        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Profile photo updated successfully.',
            'profile_photo_url': relative_url
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update your profile photo. Please try again.'}), 500


# ==========================================
# MEDICAL HISTORY MANAGEMENT MODULE
# ==========================================

@app.route('/medical-history')
@login_required
def medical_history():
    """Medical History Management Page."""
    user = User.query.get(session.get('user_id'))
    if not user:
        session.clear()
        return redirect(url_for('login'))
    return render_template('medical_history.html', user=user)


@app.route('/api/medical-history', methods=['GET'])
@login_required
def get_medical_history():
    """Returns summary counts & record lists for the authenticated athlete."""
    user_id = session.get('user_id')
    
    injuries = Injury.query.filter_by(user_id=user_id).order_by(Injury.created_at.desc()).all()
    conditions = MedicalCondition.query.filter_by(user_id=user_id).order_by(MedicalCondition.created_at.desc()).all()
    allergies = Allergy.query.filter_by(user_id=user_id).order_by(Allergy.created_at.desc()).all()
    medications = Medication.query.filter_by(user_id=user_id).order_by(Medication.created_at.desc()).all()
    surgeries = Surgery.query.filter_by(user_id=user_id).order_by(Surgery.created_at.desc()).all()

    payload = {
        'status': 'success',
        'summary': {
            'injuries_count': len(injuries),
            'conditions_count': len(conditions),
            'allergies_count': len(allergies),
            'surgeries_count': len(surgeries)
        },
        'injuries': [i.to_dict() for i in injuries],
        'conditions': [c.to_dict() for c in conditions],
        'allergies': [a.to_dict() for a in allergies],
        'medications': [m.to_dict() for m in medications],
        'surgeries': [s.to_dict() for s in surgeries]
    }
    return jsonify(payload)


@app.route('/api/injuries', methods=['POST'])
@login_required
def add_injury():
    user_id = session.get('user_id')
    data = request.get_json() or request.form.to_dict()

    injury_type = data.get('injury_type', '').strip()
    body_part = data.get('body_part', '').strip()
    injury_date = data.get('injury_date', '').strip()
    severity = data.get('severity', 'Moderate').strip()
    treatment = data.get('treatment', '').strip()
    recovery_status = data.get('recovery_status', 'Recovered').strip()
    notes = data.get('notes', '').strip()

    if not injury_type or not body_part or not injury_date:
        return jsonify({'status': 'error', 'message': 'Injury Type, Body Part, and Date are required.'}), 400

    try:
        injury = Injury(
            user_id=user_id,
            injury_type=injury_type,
            body_part=body_part,
            injury_date=injury_date,
            severity=severity,
            treatment=treatment,
            recovery_status=recovery_status,
            notes=notes
        )
        db.session.add(injury)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Injury record added successfully.', 'injury': injury.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to save injury record. Please try again.'}), 500


@app.route('/api/injuries/<int:injury_id>', methods=['PUT', 'DELETE'])
@login_required
def manage_injury(injury_id):
    user_id = session.get('user_id')
    injury = Injury.query.filter_by(id=injury_id, user_id=user_id).first()
    if not injury:
        return jsonify({'status': 'error', 'message': 'Injury record not found or unauthorized.'}), 404

    if request.method == 'DELETE':
        try:
            db.session.delete(injury)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Injury record deleted successfully.'})
        except Exception:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': 'Unable to delete injury record. Please try again.'}), 500

    data = request.get_json() or request.form.to_dict()
    injury.injury_type = data.get('injury_type', injury.injury_type).strip()
    injury.body_part = data.get('body_part', injury.body_part).strip()
    injury.injury_date = data.get('injury_date', injury.injury_date).strip()
    injury.severity = data.get('severity', injury.severity).strip()
    injury.treatment = data.get('treatment', injury.treatment).strip()
    injury.recovery_status = data.get('recovery_status', injury.recovery_status).strip()
    injury.notes = data.get('notes', injury.notes).strip()

    try:
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Injury record updated successfully.', 'injury': injury.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update injury record. Please try again.'}), 500


@app.route('/api/conditions', methods=['POST'])
@login_required
def add_condition():
    user_id = session.get('user_id')
    data = request.get_json() or request.form.to_dict()
    name = data.get('condition_name', '').strip()
    if not name:
        return jsonify({'status': 'error', 'message': 'Condition Name is required.'}), 400
    try:
        cond = MedicalCondition(user_id=user_id, condition_name=name, diagnosis_date=data.get('diagnosis_date', '').strip(), status=data.get('status', 'Active').strip(), notes=data.get('notes', '').strip())
        db.session.add(cond)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Medical condition added successfully.', 'condition': cond.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to save medical condition.'}), 500


@app.route('/api/conditions/<int:cond_id>', methods=['PUT', 'DELETE'])
@login_required
def manage_condition(cond_id):
    user_id = session.get('user_id')
    cond = MedicalCondition.query.filter_by(id=cond_id, user_id=user_id).first()
    if not cond:
        return jsonify({'status': 'error', 'message': 'Record not found.'}), 404
    if request.method == 'DELETE':
        try:
            db.session.delete(cond)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Medical condition deleted successfully.'})
        except Exception:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': 'Unable to delete medical condition.'}), 500

    data = request.get_json() or request.form.to_dict()
    cond.condition_name = data.get('condition_name', cond.condition_name).strip()
    cond.diagnosis_date = data.get('diagnosis_date', cond.diagnosis_date).strip()
    cond.status = data.get('status', cond.status).strip()
    cond.notes = data.get('notes', cond.notes).strip()
    try:
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Medical condition updated successfully.', 'condition': cond.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update medical condition.'}), 500


@app.route('/api/allergies', methods=['POST'])
@login_required
def add_allergy():
    user_id = session.get('user_id')
    data = request.get_json() or request.form.to_dict()
    name = data.get('allergy_name', '').strip()
    if not name:
        return jsonify({'status': 'error', 'message': 'Allergy Name is required.'}), 400
    try:
        allergy = Allergy(user_id=user_id, allergy_name=name, allergy_type=data.get('allergy_type', 'Medication').strip(), reaction=data.get('reaction', '').strip(), notes=data.get('notes', '').strip())
        db.session.add(allergy)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Allergy record added successfully.', 'allergy': allergy.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to save allergy record.'}), 500


@app.route('/api/allergies/<int:allergy_id>', methods=['PUT', 'DELETE'])
@login_required
def manage_allergy(allergy_id):
    user_id = session.get('user_id')
    allergy = Allergy.query.filter_by(id=allergy_id, user_id=user_id).first()
    if not allergy:
        return jsonify({'status': 'error', 'message': 'Record not found.'}), 404
    if request.method == 'DELETE':
        try:
            db.session.delete(allergy)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Allergy record deleted successfully.'})
        except Exception:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': 'Unable to delete allergy record.'}), 500

    data = request.get_json() or request.form.to_dict()
    allergy.allergy_name = data.get('allergy_name', allergy.allergy_name).strip()
    allergy.allergy_type = data.get('allergy_type', allergy.allergy_type).strip()
    allergy.reaction = data.get('reaction', allergy.reaction).strip()
    allergy.notes = data.get('notes', allergy.notes).strip()
    try:
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Allergy record updated successfully.', 'allergy': allergy.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update allergy record.'}), 500


@app.route('/api/medications', methods=['POST'])
@login_required
def add_medication():
    user_id = session.get('user_id')
    data = request.get_json() or request.form.to_dict()
    name = data.get('medication_name', '').strip()
    if not name:
        return jsonify({'status': 'error', 'message': 'Medication Name is required.'}), 400
    try:
        med = Medication(user_id=user_id, medication_name=name, dosage=data.get('dosage', '').strip(), frequency=data.get('frequency', '').strip(), start_date=data.get('start_date', '').strip(), end_date=data.get('end_date', '').strip(), notes=data.get('notes', '').strip())
        db.session.add(med)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Medication added successfully.', 'medication': med.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to save medication.'}), 500


@app.route('/api/medications/<int:med_id>', methods=['PUT', 'DELETE'])
@login_required
def manage_medication(med_id):
    user_id = session.get('user_id')
    med = Medication.query.filter_by(id=med_id, user_id=user_id).first()
    if not med:
        return jsonify({'status': 'error', 'message': 'Record not found.'}), 404
    if request.method == 'DELETE':
        try:
            db.session.delete(med)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Medication deleted successfully.'})
        except Exception:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': 'Unable to delete medication.'}), 500

    data = request.get_json() or request.form.to_dict()
    med.medication_name = data.get('medication_name', med.medication_name).strip()
    med.dosage = data.get('dosage', med.dosage).strip()
    med.frequency = data.get('frequency', med.frequency).strip()
    med.start_date = data.get('start_date', med.start_date).strip()
    med.end_date = data.get('end_date', med.end_date).strip()
    med.notes = data.get('notes', med.notes).strip()
    try:
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Medication updated successfully.', 'medication': med.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update medication.'}), 500


@app.route('/api/surgeries', methods=['POST'])
@login_required
def add_surgery():
    user_id = session.get('user_id')
    data = request.get_json() or request.form.to_dict()
    name = data.get('surgery_name', '').strip()
    bpart = data.get('body_part', '').strip()
    sdate = data.get('surgery_date', '').strip()
    if not name or not bpart or not sdate:
        return jsonify({'status': 'error', 'message': 'Surgery Name, Body Part, and Date are required.'}), 400
    try:
        surg = Surgery(user_id=user_id, surgery_name=name, body_part=bpart, surgery_date=sdate, hospital_clinic=data.get('hospital_clinic', '').strip(), notes=data.get('notes', '').strip())
        db.session.add(surg)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Surgery record added successfully.', 'surgery': surg.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to save surgery record.'}), 500


@app.route('/api/surgeries/<int:surg_id>', methods=['PUT', 'DELETE'])
@login_required
def manage_surgery(surg_id):
    user_id = session.get('user_id')
    surg = Surgery.query.filter_by(id=surg_id, user_id=user_id).first()
    if not surg:
        return jsonify({'status': 'error', 'message': 'Record not found.'}), 404
    if request.method == 'DELETE':
        try:
            db.session.delete(surg)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Surgery record deleted successfully.'})
        except Exception:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': 'Unable to delete surgery record.'}), 500

    data = request.get_json() or request.form.to_dict()
    surg.surgery_name = data.get('surgery_name', surg.surgery_name).strip()
    surg.body_part = data.get('body_part', surg.body_part).strip()
    surg.surgery_date = data.get('surgery_date', surg.surgery_date).strip()
    surg.hospital_clinic = data.get('hospital_clinic', surg.hospital_clinic).strip()
    surg.notes = data.get('notes', surg.notes).strip()
    try:
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Surgery record updated successfully.', 'surgery': surg.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update surgery record.'}), 500


# ==========================================
# DAILY HEALTH MONITORING & ML PREDICTION API
# ==========================================

@app.route('/daily-monitoring')
@login_required
def daily_monitoring():
    """Daily Health Monitoring Form Page."""
    user = User.query.get(session.get('user_id'))
    if not user:
        session.clear()
        return redirect(url_for('login'))

    today_str = datetime.utcnow().strftime('%Y-%m-%d')
    today_date_str = datetime.utcnow().strftime('%A, %B %d, %Y')
    
    today_record = DailyHealthRecord.query.filter_by(user_id=user.id, record_date=today_str).first()

    return render_template('daily_monitoring.html', user=user, today_date_str=today_date_str, today_record=today_record)


@app.route('/api/daily-monitoring/today', methods=['GET'])
@login_required
def get_today_health_record():
    """API endpoint returning today's health record for authenticated athlete."""
    user_id = session.get('user_id')
    today_str = datetime.utcnow().strftime('%Y-%m-%d')

    record = DailyHealthRecord.query.filter_by(user_id=user_id, record_date=today_str).first()

    if not record:
        return jsonify({'status': 'success', 'has_today_record': False, 'record': None})

    return jsonify({
        'status': 'success',
        'has_today_record': True,
        'record': record.to_dict()
    })


@app.route('/api/predictions/predict', methods=['POST'])
@login_required
def predict_injury_risk():
    """
    API Endpoint for submitting daily health parameters, running Random Forest ML model,
    persisting daily health record, and returning prediction results.
    """
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify({'status': 'error', 'message': 'Unauthorized athlete session.'}), 401

    data = request.get_json() or request.form.to_dict()

    try:
        sleep_hours = float(data.get('sleep_hours', 8.0))
        if sleep_hours < 0.0 or sleep_hours > 12.0:
            return jsonify({'status': 'error', 'message': 'Sleep Hours must be between 0 and 12 hours.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Sleep Hours must be a valid number.'}), 400

    try:
        training_hours = float(data.get('training_hours', 2.0))
        if training_hours < 0.0 or training_hours > 12.0:
            return jsonify({'status': 'error', 'message': 'Training Hours must be between 0 and 12 hours.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Training Hours must be a valid number.'}), 400

    try:
        resting_heart_rate = int(data.get('resting_heart_rate', 65))
        if resting_heart_rate < 30 or resting_heart_rate > 180:
            return jsonify({'status': 'error', 'message': 'Resting Heart Rate must be between 30 and 180 BPM.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Resting Heart Rate must be a valid integer.'}), 400

    try:
        fatigue_level = int(data.get('fatigue_level', 3))
        if fatigue_level < 1 or fatigue_level > 10:
            return jsonify({'status': 'error', 'message': 'Fatigue Level must be between 1 and 10.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Fatigue Level must be a valid integer.'}), 400

    try:
        stress_level = int(data.get('stress_level', 3))
        if stress_level < 1 or stress_level > 10:
            return jsonify({'status': 'error', 'message': 'Stress Level must be between 1 and 10.'}), 400
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Stress Level must be a valid integer.'}), 400

    prev_inj_val = data.get('previous_injury')
    if isinstance(prev_inj_val, str):
        previous_injury = prev_inj_val.strip().lower() in ['true', 'yes', '1']
    else:
        previous_injury = bool(prev_inj_val)

    injury_details = str(data.get('injury_details', '')).strip()

    # Invoke Scikit-Learn Random Forest ML Prediction Engine
    prediction = ml_service.predict_injury_risk(
        sleep_hours=sleep_hours,
        training_hours=training_hours,
        resting_heart_rate=resting_heart_rate,
        fatigue_level=fatigue_level,
        stress_level=stress_level,
        previous_injury=previous_injury
    )

    today_str = datetime.utcnow().strftime('%Y-%m-%d')

    try:
        # Check if record exists for today
        record = DailyHealthRecord.query.filter_by(user_id=user_id, record_date=today_str).first()
        if not record:
            record = DailyHealthRecord(user_id=user_id, record_date=today_str)
            db.session.add(record)

        record.sleep_hours = sleep_hours
        record.training_hours = training_hours
        record.resting_heart_rate = resting_heart_rate
        record.fatigue_level = fatigue_level
        record.stress_level = stress_level
        record.previous_injury = previous_injury
        record.injury_details = injury_details
        record.risk_score = prediction['risk_score']
        record.risk_label = prediction['risk_label']

        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Health monitoring recorded and injury risk analyzed successfully.',
            'record': record.to_dict(),
            'prediction': prediction
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to analyze your health data right now. Please try again.'}), 500


@app.route('/prediction-history')
@login_required
def prediction_history():
    """Prediction History Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('prediction_history.html', user=user)


@app.route('/api/predictions/history', methods=['GET'])
@login_required
def get_prediction_history():
    """API endpoint returning authenticated athlete's complete historical injury risk predictions."""
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify({'status': 'error', 'message': 'Unauthorized athlete session.'}), 401

    try:
        records = DailyHealthRecord.query.filter_by(user_id=user_id).order_by(
            DailyHealthRecord.record_date.desc(),
            DailyHealthRecord.id.desc()
        ).all()

        return jsonify({
            'status': 'success',
            'count': len(records),
            'records': [r.to_dict() for r in records]
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Unable to load prediction history. Please try again.'
        }), 500



@app.route('/weekly-summary')
@login_required
def weekly_summary():
    """Weekly Summary Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('weekly_summary.html', user=user)


@app.route('/monthly-summary')
@login_required
def monthly_summary():
    """Monthly Summary Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('monthly_summary.html', user=user)


@app.route('/api/dashboard-data')
@login_required
def get_dashboard_data():
    """API endpoint providing decoupled dashboard statistics, trends, and risk distributions."""
    user = User.query.get(session.get('user_id'))
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    payload = {
        'status': 'success',
        'has_predictions': True,
        'model_status': 'Random Forest Model Active',
        'user': {
            'id': user.id,
            'full_name': user.full_name,
            'primary_sport': user.primary_sport,
            'profile_photo': user.profile_photo
        },
        'stats': {
            'injury_risk_percent': 18,
            'risk_level': 'LOW RISK',
            'risk_badge_color': 'success',
            'total_predictions': 12,
            'avg_sleep_hrs': 7.4,
            'avg_training_hrs': 3.2,
            'last_prediction_date': '14 August 2026'
        },
        'risk_summary': {
            'risk_level': 'Low Risk',
            'risk_percent': 18,
            'predicted_on': '14 Aug 2026'
        },
        'health_trends': {
            '7_days': {
                'labels': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                'sleep': [7.5, 7.0, 7.8, 6.9, 7.4, 8.1, 7.2],
                'training': [3.0, 3.5, 2.5, 4.0, 3.2, 2.0, 3.5],
                'resting_hr': [66, 68, 65, 71, 67, 64, 68]
            },
            '30_days': {
                'labels': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
                'sleep': [7.2, 7.5, 7.3, 7.6],
                'training': [3.1, 3.4, 3.0, 3.3],
                'resting_hr': [67, 66, 68, 65]
            }
        },
        'risk_distribution': {
            'labels': ['Low Risk', 'Medium Risk', 'High Risk'],
            'counts': [7, 3, 2],
            'colors': ['#22c55e', '#f59e0b', '#ef4444']
        },
        'recent_predictions': [
            {'date': '14 Aug 2026', 'risk_level': 'Low', 'risk_percent': 18, 'status': 'Completed', 'badge_class': 'success'},
            {'date': '11 Aug 2026', 'risk_level': 'Medium', 'risk_percent': 54, 'status': 'Completed', 'badge_class': 'warning'},
            {'date': '08 Aug 2026', 'risk_level': 'Low', 'risk_percent': 21, 'status': 'Completed', 'badge_class': 'success'}
        ],
        'todays_health_overview': {
            'sleep_hrs': '7.4 hrs',
            'training_hrs': '3.2 hrs',
            'heart_rate': '72 bpm',
            'fatigue': 'Low',
            'stress': 'Moderate',
            'previous_injury': 'No',
            'has_today_data': True
        }
    }

    return jsonify(payload)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"AthleteGuard AI running on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
