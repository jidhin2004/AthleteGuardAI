import os
import time
import base64
import re
import secrets
import hmac
import io
from datetime import datetime, timedelta
from functools import wraps
from urllib.parse import quote_plus
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, inspect, text
from models import db
from models.user import User
from models.medical import Injury, MedicalCondition, Allergy, Medication, Surgery
from models.health import DailyHealthRecord
from models.admin_note import AdminNote
from models.notification import Notification
from models.team import Team, TeamMember
from services.ml_service import ml_service

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "athleteguard_ai_secret_key_mca_2026")


def validate_password_strength(password):
    """Enforces 8+ chars, 1 uppercase, 1 lowercase, 1 digit, 1 special character."""
    if not password or len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter (A-Z)."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter (a-z)."
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number (0-9)."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character (e.g. !@#$%^&*)."
    return True, ""


def generate_csrf_token():
    """Generates or retrieves unique session CSRF token."""
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(32)
    return session['csrf_token']


@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf_token)


@app.before_request
def csrf_protect():
    """CSRF Token Verification Middleware for all state-changing HTTP requests."""
    if request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
        if request.endpoint == 'static':
            return None

        session_token = session.get('csrf_token')
        if not session_token:
            session_token = generate_csrf_token()

        header_token = request.headers.get('X-CSRFToken')
        form_token = request.form.get('csrf_token')
        json_token = None
        if request.is_json and isinstance(request.json, dict):
            json_token = request.json.get('csrf_token')

        request_token = header_token or form_token or json_token

        if request.path in ['/login', '/register'] and not request_token:
            return None

        if not request_token or not hmac.compare_digest(str(request_token), str(session_token)):
            if request.is_json or request.path.startswith('/api/'):
                return jsonify({'status': 'error', 'message': 'CSRF token validation failed. Invalid or missing CSRF token.'}), 400
            else:
                flash("CSRF security verification failed. Please try again.", "danger")
                return render_template('login.html')


@app.after_request
def add_security_headers(response):
    """Enforces strict anti-caching HTTP headers on non-static responses to prevent BFCache dashboard leaks after logout."""
    if request.endpoint != 'static':
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response


# Profile Upload Configuration
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads', 'profile_photos')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}
MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB


def validate_image_file(file_bytes, filename):
    """Validates binary image payload size, extension, MIME type, and Pillow stream integrity."""
    if not file_bytes:
        return False, "Empty file payload provided.", None

    if len(file_bytes) > MAX_FILE_SIZE_BYTES:
        return False, "Please upload a JPG, PNG, or WEBP image under 5 MB.", None

    ext = filename.rsplit('.', 1)[1].lower() if filename and '.' in filename else 'jpg'
    if ext not in ALLOWED_EXTENSIONS:
        return False, "Please upload a JPG, PNG, or WEBP image under 5 MB.", None

    try:
        img = Image.open(io.BytesIO(file_bytes))
        img.verify()
        img_format = (img.format or '').lower()
        if img_format not in ['jpeg', 'png', 'webp']:
            return False, f"Invalid image MIME type ({img.format}). Allowed formats: JPEG, PNG, WEBP.", None
    except Exception:
        return False, "File content is corrupted or not a valid image file.", None

    return True, "", ext

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
    # Migration helper: ensure required columns exist in MySQL tables without data loss
    try:
        inspector = inspect(db.engine)
        
        # Check users table
        user_columns = [c['name'] for c in inspector.get_columns('users')]
        if 'role' not in user_columns:
            db.session.execute(text("ALTER TABLE users ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT 'athlete'"))
            db.session.commit()
        if 'account_status' not in user_columns:
            db.session.execute(text("ALTER TABLE users ADD COLUMN account_status VARCHAR(20) NOT NULL DEFAULT 'active'"))
            db.session.commit()
        if 'date_of_birth' not in user_columns:
            db.session.execute(text("ALTER TABLE users ADD COLUMN date_of_birth DATE NULL"))
            db.session.commit()
            db.session.execute(text("UPDATE users SET date_of_birth = DATE_SUB(CURDATE(), INTERVAL IFNULL(age, 25) YEAR) WHERE date_of_birth IS NULL"))
            db.session.commit()

        # Check daily_health_records table
        health_columns = [c['name'] for c in inspector.get_columns('daily_health_records')]
        if 'review_status' not in health_columns:
            db.session.execute(text("ALTER TABLE daily_health_records ADD COLUMN review_status VARCHAR(30) NOT NULL DEFAULT 'Pending Review'"))
            db.session.commit()
        if 'reviewed_by' not in health_columns:
            db.session.execute(text("ALTER TABLE daily_health_records ADD COLUMN reviewed_by INT NULL"))
            db.session.commit()
        if 'reviewed_at' not in health_columns:
            db.session.execute(text("ALTER TABLE daily_health_records ADD COLUMN reviewed_at DATETIME NULL"))
            db.session.commit()

        print("[SCHEMA VERIFIED] Successfully verified MySQL database schema columns and tables.")
    except Exception as e:
        print(f"Database schema verification note: {e}")


def calculate_age(dob_input):
    """Calculates exact age in years from date_of_birth (date object or YYYY-MM-DD string)."""
    if not dob_input:
        return None
    if isinstance(dob_input, str):
        try:
            dob_input = datetime.strptime(dob_input.strip(), '%Y-%m-%d').date()
        except ValueError:
            return None
    today = datetime.utcnow().date()
    calc = today.year - dob_input.year
    if (today.month, today.day) < (dob_input.month, dob_input.day):
        calc -= 1
    return max(0, calc)


def validate_dob_and_gender(dob_str, gender_str):
    """
    Authoritative server-side validator:
    - Gender must strictly be either 'Male' or 'Female'.
    - Date of Birth must be present, valid YYYY-MM-DD format, not in the future, and produce 1 <= Age <= 120.
    """
    if not gender_str or gender_str.strip() not in ['Male', 'Female']:
        return False, "Gender must be selected as either Male or Female."

    if not dob_str or not dob_str.strip():
        return False, "Date of Birth is required."

    try:
        dob = datetime.strptime(dob_str.strip(), '%Y-%m-%d').date()
    except ValueError:
        return False, "Invalid Date of Birth format. Please select a valid date (YYYY-MM-DD)."

    today = datetime.utcnow().date()
    if dob > today:
        return False, "Date of Birth cannot be in the future."

    calc_age = calculate_age(dob)
    if calc_age is None or calc_age < 1 or calc_age > 120:
        return False, f"Date of Birth produces an invalid athlete age ({calc_age}). Age must be between 1 and 120 years."

    return True, ""


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


def coach_required(f):
    """Decorator to restrict access strictly to authenticated Coach users."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in with Coach credentials to access the Coach Dashboard.", "warning")
            return redirect(url_for('login'))

        user_id = session.get('user_id')
        user = User.query.get(user_id)
        if not user or user.role != 'coach':
            flash("Access denied. Coach privileges are required to view this page.", "danger")
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
    if request.method == 'GET' and 'user_id' in session:
        user_role = session.get('user_role')
        if user_role == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif user_role == 'coach':
            return redirect(url_for('coach_dashboard'))
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        remember = request.form.get('remember')

        if not email or not password:
            flash("Please enter both Athlete ID/Email and password.", "danger")
            return render_template('login.html')

        db.session.expire_all()
        identifier = email.strip()
        user = None
        if identifier.upper().startswith('ATH-'):
            try:
                raw_id = int(identifier.split('-')[1])
                user = db.session.get(User, raw_id)
            except (IndexError, ValueError):
                user = None

        if not user:
            user = User.query.filter(db.func.lower(User.email) == identifier.lower()).first()

        if user:
            db.session.refresh(user)

        if user and user.check_password(password):
            if (user.account_status or 'active').lower() == 'inactive':
                role_label = user.role.capitalize() if user.role else 'Athlete'
                msg = f"Your {role_label} account has been deactivated by the administrator. Please contact support."
                flash(msg, "danger")
                return render_template('login.html')

            session.clear()
            session.permanent = True if remember else False
            session['user_id'] = user.id
            session['user_name'] = user.full_name
            session['user_email'] = user.email
            session['user_sport'] = user.primary_sport
            session['user_role'] = user.role or 'athlete'

            flash(f"Welcome back, {user.full_name}!", "success")
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user.role == 'coach':
                return redirect(url_for('coach_dashboard'))
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid Athlete ID/Email or password. Please try again.", "danger")
            return render_template('login.html')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration handler with password hashing and database storage."""
    if 'user_id' in session:
        user_role = session.get('user_role')
        if user_role == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif user_role == 'coach':
            return redirect(url_for('coach_dashboard'))
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        date_of_birth = request.form.get('date_of_birth', '').strip()
        gender = request.form.get('gender', '').strip()
        primary_sport = request.form.get('primary_sport', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not all([full_name, date_of_birth, gender, primary_sport, email, password]):
            flash("All fields are required for registration.", "danger")
            return render_template('register.html', error_msg="All fields are required.")

        is_valid_dg, dg_err = validate_dob_and_gender(date_of_birth, gender)
        if not is_valid_dg:
            flash(dg_err, "danger")
            return render_template('register.html', error_msg=dg_err)

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('register.html', error_msg="Passwords do not match.")

        is_strong, pwd_err = validate_password_strength(password)
        if not is_strong:
            flash(pwd_err, "danger")
            return render_template('register.html', error_msg=pwd_err)

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("An account with this email address already exists.", "warning")
            return render_template('register.html', error_msg="Email already registered. Try logging in instead.")

        try:
            dob_date = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
            calc_age = calculate_age(dob_date)

            # SECURITY: Hardcode role='athlete' on the backend regardless of client inputs
            new_user = User(
                full_name=full_name,
                date_of_birth=dob_date,
                _legacy_age=calc_age,
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
# COACH DASHBOARD ROUTE & MANAGEMENT APIs
# ==========================================

@app.route('/coach/dashboard')
@coach_required
def coach_dashboard():
    """Coach Dashboard Landing Page - Protected Route for Coach Users."""
    coach_id = session.get('user_id')
    user = db.session.get(User, coach_id)
    if not user:
        session.clear()
        return redirect(url_for('login'))

    teams = Team.query.filter_by(coach_id=coach_id).all()
    teams_count = len(teams)
    team_ids = [t.id for t in teams]
    total_players_count = TeamMember.query.filter(TeamMember.team_id.in_(team_ids), TeamMember.status == 'active').count() if team_ids else 0

    return render_template('coach/dashboard.html', user=user, teams_count=teams_count, total_players_count=total_players_count, teams=teams)


@app.route('/api/admin/create-coach', methods=['POST'])
@admin_required
def admin_create_coach():
    """API Endpoint for Admins to create or upgrade Coach accounts securely."""
    data = request.get_json() if request.is_json else request.form
    full_name = (data.get('full_name') or '').strip()
    email = (data.get('email') or '').strip()
    password = (data.get('password') or '').strip()
    primary_sport = (data.get('primary_sport') or 'General Sports').strip()

    if not full_name or not email or not password:
        return jsonify({'status': 'error', 'message': 'Full name, email, and password are required.'}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        existing_user.role = 'coach'
        existing_user.full_name = full_name
        existing_user.primary_sport = primary_sport or existing_user.primary_sport
        existing_user.set_password(password)
        existing_user.account_status = 'active'
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': f"Account for '{full_name}' upgraded to Coach successfully.",
            'user': existing_user.to_dict()
        })

    is_strong, pwd_err = validate_password_strength(password)
    if not is_strong:
        return jsonify({'status': 'error', 'message': pwd_err}), 400

    try:
        new_coach = User(
            full_name=full_name,
            _legacy_age=35,
            gender='Other',
            primary_sport=primary_sport or 'General Sports',
            email=email,
            role='coach',
            account_status='active'
        )
        new_coach.set_password(password)
        db.session.add(new_coach)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': f"Coach account for '{full_name}' created successfully.",
            'user': new_coach.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Database error: {str(e)}'}), 500

def generate_unique_team_code(sport):
    """
    Generates a unique, readable Team Code with sport prefix and random alphanumeric string.
    Example: Football -> FB-7K29Q, Basketball -> BB-4P8LX
    """
    sport_prefixes = {
        'Football': 'FB',
        'Basketball': 'BB',
        'Cricket': 'CR',
        'Volleyball': 'VB',
        'Athletics': 'AT',
        'Other': 'TM'
    }
    prefix = sport_prefixes.get(sport.strip().capitalize() if sport else 'Other', 'TM')
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    for _ in range(100):
        code_suffix = ''.join(secrets.choice(alphabet) for _ in range(5))
        code = f"{prefix}-{code_suffix}"
        if not Team.query.filter_by(team_code=code).first():
            return code
    return f"{prefix}-{secrets.token_hex(3).upper()}"


# ==========================================
# STEP 3: COACH TEAM CREATION & MANAGEMENT APIs
# ==========================================

@app.route('/coach/teams')
@coach_required
def coach_teams_page():
    """Coach My Teams Landing Page - Protected Route for Coach Users."""
    user = User.query.get(session.get('user_id'))
    if not user:
        session.clear()
        return redirect(url_for('login'))
    return render_template('coach/teams.html', user=user)


@app.route('/api/coach/teams', methods=['GET', 'POST'])
@coach_required
def api_coach_teams():
    """API for Coach to list their created teams or create a new team."""
    coach_id = session.get('user_id')
    user = User.query.get(coach_id)
    if not user or user.role != 'coach':
        return jsonify({'status': 'error', 'message': 'Unauthorized coach access.'}), 403

    if request.method == 'GET':
        teams = Team.query.filter_by(coach_id=coach_id).order_by(Team.created_at.desc()).all()
        return jsonify({
            'status': 'success',
            'count': len(teams),
            'teams': [t.to_dict() for t in teams]
        })

    data = request.get_json() or request.form.to_dict()
    team_name = data.get('team_name', '').strip()
    sport = data.get('sport', '').strip()
    season = data.get('season', '2026-27').strip() or '2026-27'
    description = data.get('description', '').strip()

    if not team_name:
        return jsonify({'status': 'error', 'message': 'Team Name is required.'}), 400

    if len(team_name) > 100:
        return jsonify({'status': 'error', 'message': 'Team Name cannot exceed 100 characters.'}), 400

    allowed_sports = ['Football', 'Basketball', 'Cricket', 'Volleyball', 'Athletics', 'Other']
    if not sport or sport not in allowed_sports:
        return jsonify({'status': 'error', 'message': f'Sport must be one of: {", ".join(allowed_sports)}'}), 400

    try:
        team_code = generate_unique_team_code(sport)
        new_team = Team(
            team_name=team_name,
            sport=sport,
            season=season,
            description=description,
            coach_id=coach_id,
            team_code=team_code,
            status='active'
        )
        db.session.add(new_team)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': f"Team '{team_name}' created successfully with code '{team_code}'.",
            'team': new_team.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Unable to create team: {str(e)}'}), 500


@app.route('/coach/teams/<int:team_id>')
@coach_required
def coach_team_detail_page(team_id):
    """Coach View Team Detail Page - Protected Route."""
    coach_id = session.get('user_id')
    user = User.query.get(coach_id)
    team = Team.query.filter_by(id=team_id, coach_id=coach_id).first()
    if not team:
        flash("Access denied. You can only view teams you created.", "danger")
        return redirect(url_for('coach_teams_page'))
    return render_template('coach/team_detail.html', user=user, team=team)


@app.route('/api/coach/teams/<int:team_id>', methods=['GET'])
@coach_required
def api_coach_team_detail(team_id):
    """API Endpoint returning team details and member roster for coach-owned team."""
    coach_id = session.get('user_id')
    team = Team.query.filter_by(id=team_id, coach_id=coach_id).first()
    if not team:
        return jsonify({'status': 'error', 'message': 'Team not found or unauthorized.'}), 403

    memberships = TeamMember.query.filter_by(team_id=team_id, status='active').order_by(TeamMember.joined_at.desc()).all()
    members_data = [m.to_dict() for m in memberships]

    return jsonify({
        'status': 'success',
        'team': team.to_dict(),
        'member_count': len(members_data),
        'members': members_data
    })


@app.route('/api/coach/teams/<int:team_id>/members/<int:athlete_id>/remove', methods=['POST'])
@coach_required
def api_coach_remove_member(team_id, athlete_id):
    """API Endpoint for Coach to remove an athlete from their team."""
    coach_id = session.get('user_id')
    team = Team.query.filter_by(id=team_id, coach_id=coach_id).first()
    if not team:
        return jsonify({'status': 'error', 'message': 'Team not found or unauthorized.'}), 403

    membership = TeamMember.query.filter_by(team_id=team_id, athlete_id=athlete_id, status='active').first()
    if not membership:
        return jsonify({'status': 'error', 'message': 'Athlete is not an active member of this team.'}), 404

    try:
        membership.status = 'removed'
        db.session.commit()
        athlete = User.query.get(athlete_id)
        athlete_name = athlete.full_name if athlete else 'Athlete'
        return jsonify({
            'status': 'success',
            'message': f"'{athlete_name}' has been removed from '{team.team_name}'."
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to remove member.'}), 500


# ==========================================
# STEP 3: ATHLETE TEAM JOINING & VIEWING APIs
# ==========================================

@app.route('/join-team')
@login_required
def join_team_page():
    """Athlete Join Team Page."""
    user = User.query.get(session.get('user_id'))
    if not user:
        session.clear()
        return redirect(url_for('login'))
    if user.role != 'athlete':
        flash("Only athletes can join teams.", "warning")
        return redirect(url_for('dashboard'))
    return render_template('join_team.html', user=user)


@app.route('/api/teams/join', methods=['POST'])
@login_required
def api_join_team():
    """
    API Endpoint for Selected Athlete to enter a Team Code and join a team.
    Enforces server-side authentication, account status check, team code validity,
    team status, primary sport matching, duplicate membership check, and single active team constraint.
    """
    user_id = session.get('user_id')
    user = db.session.get(User, user_id)
    if not user or user.role != 'athlete':
        return jsonify({'status': 'error', 'message': 'Only athletes are permitted to join teams.'}), 403

    if (user.account_status or 'active').lower() != 'active':
        return jsonify({'status': 'error', 'message': 'Your athlete account is inactive and cannot join teams.'}), 403

    data = request.get_json() or request.form.to_dict()
    team_code = data.get('team_code', '').strip().upper()

    if not team_code:
        return jsonify({'status': 'error', 'message': 'Team Code is required.'}), 400

    team = Team.query.filter_by(team_code=team_code).first()
    if not team:
        return jsonify({'status': 'error', 'message': f"No team found matching code '{team_code}'."}), 404

    if (team.status or 'active').lower() != 'active':
        return jsonify({'status': 'error', 'message': f"Team '{team.team_name}' is currently inactive and not accepting new members."}), 400

    # 1. Sport matching validation (Case-insensitive)
    athlete_sport = (user.primary_sport or '').strip().lower()
    team_sport = (team.sport or '').strip().lower()
    if athlete_sport != team_sport:
        return jsonify({
            'status': 'error',
            'message': f"This team is for {team.sport}. Your registered primary sport ({user.primary_sport}) does not match this team."
        }), 400

    # 2. Duplicate membership check for this exact team
    existing_in_same_team = TeamMember.query.filter_by(team_id=team.id, athlete_id=user_id, status='active').first()
    if existing_in_same_team:
        return jsonify({'status': 'error', 'message': 'You are already a member of this team.'}), 400

    # 3. Single active team constraint across all teams
    existing_in_other_team = TeamMember.query.filter(
        TeamMember.athlete_id == user_id,
        TeamMember.team_id != team.id,
        TeamMember.status == 'active'
    ).first()
    if existing_in_other_team:
        return jsonify({'status': 'error', 'message': 'You are already assigned to another active team.'}), 400

    try:
        membership = TeamMember.query.filter_by(team_id=team.id, athlete_id=user_id).first()
        if membership:
            membership.status = 'active'
            membership.joined_at = datetime.utcnow()
        else:
            membership = TeamMember(
                team_id=team.id,
                athlete_id=user_id,
                status='active'
            )
            db.session.add(membership)

        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': f"Successfully joined '{team.team_name}'!",
            'team': team.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Unable to join team: {str(e)}'}), 500


@app.route('/my-team')
@login_required
def my_team_page():
    """Athlete My Team View Page."""
    user = User.query.get(session.get('user_id'))
    if not user:
        session.clear()
        return redirect(url_for('login'))
    if user.role != 'athlete':
        return redirect(url_for('coach_teams_page') if user.role == 'coach' else url_for('admin_dashboard'))
    return render_template('my_team.html', user=user)


@app.route('/api/my-team', methods=['GET'])
@login_required
def api_get_my_team():
    """API Endpoint returning athlete's active team memberships."""
    user_id = session.get('user_id')
    memberships = TeamMember.query.filter_by(athlete_id=user_id, status='active').order_by(TeamMember.joined_at.desc()).all()
    teams_list = [m.to_dict() for m in memberships]

    return jsonify({
        'status': 'success',
        'count': len(teams_list),
        'teams': teams_list
    })


@app.route('/api/teams/leave', methods=['POST'])
@login_required
def api_leave_team():
    """API Endpoint for Athlete to leave a team."""
    user_id = session.get('user_id')
    data = request.get_json() or request.form.to_dict()
    team_id = data.get('team_id')

    if not team_id:
        return jsonify({'status': 'error', 'message': 'Team ID is required.'}), 400

    membership = TeamMember.query.filter_by(team_id=team_id, athlete_id=user_id, status='active').first()
    if not membership:
        return jsonify({'status': 'error', 'message': 'Active team membership not found.'}), 404

    try:
        membership.status = 'left'
        db.session.commit()
        team = Team.query.get(team_id)
        team_name = team.team_name if team else 'the team'
        return jsonify({
            'status': 'success',
            'message': f"You have left '{team_name}'."
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to leave team. Please try again.'}), 500


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
        active_athletes = User.query.filter(User.role == 'athlete', db.or_(User.account_status == 'active', User.account_status.is_(None))).count()
        inactive_athletes = User.query.filter(User.role == 'athlete', User.account_status == 'inactive').count()

        total_health_records = DailyHealthRecord.query.count()
        total_predictions = DailyHealthRecord.query.filter(DailyHealthRecord.risk_score.isnot(None)).count()
        
        low_risk_count = DailyHealthRecord.query.filter(DailyHealthRecord.risk_label.ilike('%low%')).count()
        medium_risk_count = DailyHealthRecord.query.filter(DailyHealthRecord.risk_label.ilike('%medium%')).count()
        high_risk_count = DailyHealthRecord.query.filter(DailyHealthRecord.risk_label.ilike('%high%')).count()
        pending_reviews_count = DailyHealthRecord.query.filter(DailyHealthRecord.review_status == 'Pending Review').count()

        # Priority Cases Query: High and Medium risk cases needing review (review_status != 'Resolved' and review_status != 'No Action Required')
        priority_query = DailyHealthRecord.query.filter(
            DailyHealthRecord.risk_score.isnot(None),
            DailyHealthRecord.review_status.notin_(['Resolved', 'No Action Required'])
        ).all()

        # Sort priority cases: 1. HIGH before MEDIUM, 2. Higher score first, 3. Recency
        def priority_sort_key(r):
            is_high = 1 if 'high' in (r.risk_label or '').lower() else 0
            score = r.risk_score or 0.0
            return (is_high, score, r.record_date or '')

        sorted_priority = sorted(priority_query, key=priority_sort_key, reverse=True)

        priority_cases = []
        for p in sorted_priority[:10]:
            ath = User.query.get(p.user_id)
            if not ath:
                continue
            p_dict = p.to_dict()
            p_dict['athlete_name'] = ath.full_name
            p_dict['athlete_id'] = ath.athlete_id
            p_dict['primary_sport'] = ath.primary_sport
            priority_cases.append(p_dict)

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
                'active_athletes': active_athletes,
                'inactive_athletes': inactive_athletes,
                'total_health_records': total_health_records,
                'total_predictions': total_predictions,
                'low_risk_count': low_risk_count,
                'medium_risk_count': medium_risk_count,
                'high_risk_count': high_risk_count,
                'pending_reviews_count': pending_reviews_count
            },
            'priority_cases': priority_cases,
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


# ==========================================
# ADMIN CASE REVIEWS & NOTES REST APIs
# ==========================================

@app.route('/api/admin/cases/<int:record_id>', methods=['GET'])
@admin_required
def get_admin_case_detail(record_id):
    """API Endpoint returning comprehensive case detail including health inputs, medical context, and notes."""
    record = DailyHealthRecord.query.get(record_id)
    if not record:
        return jsonify({'status': 'error', 'message': 'Prediction record not found.'}), 404

    athlete = User.query.get(record.user_id)
    if not athlete:
        return jsonify({'status': 'error', 'message': 'Athlete user not found.'}), 404

    notes = AdminNote.query.filter_by(prediction_id=record.id).order_by(AdminNote.created_at.desc()).all()
    injuries = Injury.query.filter_by(user_id=athlete.id).order_by(Injury.id.desc()).all()
    surgeries = Surgery.query.filter_by(user_id=athlete.id).order_by(Surgery.id.desc()).all()

    rec_dict = record.to_dict()
    rec_dict['athlete_name'] = athlete.full_name
    rec_dict['athlete_id'] = athlete.athlete_id
    rec_dict['primary_sport'] = athlete.primary_sport

    return jsonify({
        'status': 'success',
        'record': rec_dict,
        'athlete': athlete.to_dict(),
        'notes': [n.to_dict() for n in notes],
        'medical_summary': {
            'injuries': [i.to_dict() for i in injuries],
            'surgeries': [s.to_dict() for s in surgeries]
        }
    })


@app.route('/api/admin/cases/<int:record_id>/status', methods=['PUT'])
@admin_required
def update_case_status(record_id):
    """API Endpoint for Admin to update prediction case review status."""
    record = DailyHealthRecord.query.get(record_id)
    if not record:
        return jsonify({'status': 'error', 'message': 'Prediction record not found.'}), 404

    data = request.get_json() or request.form.to_dict()
    new_status = data.get('review_status', '').strip()
    allowed_statuses = ['Pending Review', 'Under Review', 'Needs Attention', 'Monitoring', 'Resolved', 'No Action Required']
    
    if new_status not in allowed_statuses:
        return jsonify({'status': 'error', 'message': f"Invalid review status. Allowed: {allowed_statuses}"}), 400

    admin_id = session.get('user_id')
    try:
        record.review_status = new_status
        record.reviewed_by = admin_id
        record.reviewed_at = datetime.utcnow()
        db.session.commit()

        # Check if an optional note was submitted with the status update
        note_text = data.get('note', '').strip()
        if note_text:
            note_obj = AdminNote(
                admin_id=admin_id,
                athlete_id=record.user_id,
                prediction_id=record.id,
                note=note_text
            )
            db.session.add(note_obj)

            admin_user = User.query.get(admin_id)
            admin_name = admin_user.full_name if admin_user else 'Administrator'
            notif_msg = f"Your health assessment from {record.record_date} ({record.risk_label}) status was updated to '{new_status}' by {admin_name}. Note: {note_text}"
            
            notif = Notification(
                athlete_id=record.user_id,
                admin_id=admin_id,
                message=notif_msg,
                related_prediction_id=record.id
            )
            db.session.add(notif)
            db.session.commit()

        rec_dict = record.to_dict()
        ath = User.query.get(record.user_id)
        if ath:
            rec_dict['athlete_name'] = ath.full_name
            rec_dict['athlete_id'] = ath.athlete_id

        return jsonify({
            'status': 'success',
            'message': f"Case status updated to '{new_status}' successfully.",
            'record': rec_dict
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update case status. Please try again.'}), 500


@app.route('/api/admin/cases/<int:record_id>/notes', methods=['POST'])
@admin_required
def add_case_note(record_id):
    """API Endpoint for Admin to add an administrative note to a case and notify athlete."""
    record = DailyHealthRecord.query.get(record_id)
    if not record:
        return jsonify({'status': 'error', 'message': 'Prediction record not found.'}), 404

    data = request.get_json() or request.form.to_dict()
    note_text = data.get('note', '').strip()
    if not note_text:
        return jsonify({'status': 'error', 'message': 'Note text cannot be empty.'}), 400

    admin_id = session.get('user_id')
    admin_user = User.query.get(admin_id)

    try:
        note_obj = AdminNote(
            admin_id=admin_id,
            athlete_id=record.user_id,
            prediction_id=record.id,
            note=note_text
        )
        db.session.add(note_obj)

        # Post notification to corresponding athlete
        notif_msg = f"Your recent health assessment ({record.record_date}) has been reviewed by the administrator: {note_text}"
        notif = Notification(
            athlete_id=record.user_id,
            admin_id=admin_id,
            message=notif_msg,
            related_prediction_id=record.id
        )
        db.session.add(notif)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Admin note added and athlete notified successfully.',
            'note': note_obj.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to save note. Please try again.'}), 500


@app.route('/api/admin/notes/<int:note_id>', methods=['PUT', 'DELETE'])
@admin_required
def manage_admin_note(note_id):
    """API Endpoint for editing or deleting an admin note."""
    note_obj = AdminNote.query.get(note_id)
    if not note_obj:
        return jsonify({'status': 'error', 'message': 'Note not found.'}), 404

    if request.method == 'DELETE':
        try:
            db.session.delete(note_obj)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Admin note deleted successfully.'})
        except Exception:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': 'Unable to delete note.'}), 500

    data = request.get_json() or request.form.to_dict()
    new_text = data.get('note', '').strip()
    if not new_text:
        return jsonify({'status': 'error', 'message': 'Note content cannot be empty.'}), 400

    try:
        note_obj.note = new_text
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Admin note updated successfully.', 'note': note_obj.to_dict()})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update note.'}), 500


@app.route('/api/admin/notifications', methods=['POST'])
@admin_required
def create_admin_notification():
    """
    API Endpoint for Admin to send a direct notification/recommendation to a specific athlete.
    Payload: { "athlete_id": int, "related_prediction_id": int|null, "message": str }
    """
    data = request.get_json() or request.form.to_dict()

    athlete_id = data.get('athlete_id')
    try:
        athlete_id = int(athlete_id)
    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Invalid or missing athlete ID.'}), 400

    athlete = User.query.get(athlete_id)
    if not athlete or athlete.role == 'admin':
        return jsonify({'status': 'error', 'message': 'Athlete not found.'}), 404

    message = data.get('message', '').strip()
    if not message:
        return jsonify({'status': 'error', 'message': 'Notification message cannot be empty.'}), 400

    related_prediction_id = data.get('related_prediction_id')
    if related_prediction_id:
        try:
            related_prediction_id = int(related_prediction_id)
            record = DailyHealthRecord.query.get(related_prediction_id)
            if not record:
                return jsonify({'status': 'error', 'message': 'Related prediction record not found.'}), 404
            if record.user_id != athlete_id:
                return jsonify({'status': 'error', 'message': 'Selected prediction record does not belong to this athlete.'}), 400
        except (ValueError, TypeError):
            return jsonify({'status': 'error', 'message': 'Invalid related prediction ID.'}), 400
    else:
        related_prediction_id = None

    admin_id = session.get('user_id')

    try:
        notif = Notification(
            athlete_id=athlete_id,
            admin_id=admin_id,
            message=message,
            related_prediction_id=related_prediction_id
        )
        db.session.add(notif)

        # If linked to a prediction record, also store an AdminNote
        if related_prediction_id:
            note_obj = AdminNote(
                admin_id=admin_id,
                athlete_id=athlete_id,
                prediction_id=related_prediction_id,
                note=message
            )
            db.session.add(note_obj)

        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Notification sent successfully.',
            'notification': notif.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to send notification. Please try again.'}), 500


# ==========================================
# ATHLETE ACCOUNT MANAGEMENT APIs
# ==========================================

@app.route('/api/admin/athletes/<int:user_id>/activate', methods=['POST'])
@admin_required
def activate_athlete_account(user_id):
    """API Endpoint to activate an athlete account."""
    athlete = User.query.get(user_id)
    if not athlete:
        return jsonify({'status': 'error', 'message': 'Athlete user not found.'}), 404

    if athlete.role == 'admin':
        return jsonify({'status': 'error', 'message': 'Cannot modify administrator accounts.'}), 400

    try:
        athlete.account_status = 'active'
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': f"Athlete account for '{athlete.full_name}' has been activated successfully.",
            'athlete': athlete.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to activate account.'}), 500


@app.route('/api/admin/athletes/<int:user_id>/deactivate', methods=['POST'])
@admin_required
def deactivate_athlete_account(user_id):
    """API Endpoint to deactivate an athlete account."""
    admin_id = session.get('user_id')
    if user_id == admin_id:
        return jsonify({'status': 'error', 'message': 'You cannot deactivate your own account.'}), 400

    athlete = User.query.get(user_id)
    if not athlete:
        return jsonify({'status': 'error', 'message': 'Athlete user not found.'}), 404

    if athlete.role == 'admin':
        return jsonify({'status': 'error', 'message': 'Cannot deactivate administrator accounts.'}), 400

    try:
        athlete.account_status = 'inactive'
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': f"Athlete account for '{athlete.full_name}' has been deactivated successfully.",
            'athlete': athlete.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to deactivate account.'}), 500


# ==========================================
# ATHLETE NOTIFICATIONS APIs
# ==========================================

@app.route('/api/notifications', methods=['GET'])
@login_required
def get_athlete_notifications():
    """API Endpoint returning notifications for the logged-in athlete."""
    user_id = session.get('user_id')
    notifications = Notification.query.filter_by(athlete_id=user_id).order_by(Notification.created_at.desc()).all()
    unread_count = sum(1 for n in notifications if not n.is_read)

    return jsonify({
        'status': 'success',
        'unread_count': unread_count,
        'count': len(notifications),
        'notifications': [n.to_dict() for n in notifications]
    })


@app.route('/api/notifications/<int:notification_id>/read', methods=['PUT'])
@login_required
def mark_notification_read(notification_id):
    """API Endpoint to mark a single notification as read."""
    user_id = session.get('user_id')
    notif = Notification.query.filter_by(id=notification_id, athlete_id=user_id).first()
    if not notif:
        return jsonify({'status': 'error', 'message': 'Notification not found.'}), 404

    try:
        notif.is_read = True
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Notification marked as read.'})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update notification.'}), 500


@app.route('/api/notifications/read-all', methods=['PUT'])
@login_required
def mark_all_notifications_read():
    """API Endpoint to mark all notifications as read for current athlete."""
    user_id = session.get('user_id')
    try:
        Notification.query.filter_by(athlete_id=user_id, is_read=False).update({Notification.is_read: True})
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'All notifications marked as read.'})
    except Exception:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': 'Unable to update notifications.'}), 500


@app.route('/logout')
def logout():
    """Session logout handler with complete session clearing and anti-cache headers."""
    session.clear()
    flash("You have been signed out safely.", "info")
    response = app.make_response(redirect(url_for('login')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


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
        
    latest_rec = DailyHealthRecord.query.filter_by(user_id=user.id).order_by(
        DailyHealthRecord.record_date.desc(),
        DailyHealthRecord.id.desc()
    ).first()

    risk_info = {
        'score': round(latest_rec.risk_score, 1) if (latest_rec and latest_rec.risk_score is not None) else None,
        'label': latest_rec.risk_label if (latest_rec and latest_rec.risk_label) else 'Not Calculated'
    }

    # Calculate dynamic profile completion percentage
    fields_to_check = [user.full_name, user.age, user.gender, user.primary_sport, user.email, user.phone, user.height_cm, user.weight_kg, user.emergency_name, user.emergency_relationship, user.emergency_phone, user.profile_photo]
    completed_fields = sum(1 for f in fields_to_check if f is not None and str(f).strip() != '')
    completion_pct = int((completed_fields / len(fields_to_check)) * 100)

    return render_template('profile.html', user=user, risk_info=risk_info, completion_pct=completion_pct)


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
    date_of_birth = data.get('date_of_birth', '').strip() if data.get('date_of_birth') else None
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

    if gender and gender not in ['Male', 'Female']:
        return jsonify({'status': 'error', 'message': 'Gender must be either Male or Female.'}), 400

    dob_val = user.date_of_birth
    if date_of_birth:
        is_valid_dg, dg_err = validate_dob_and_gender(date_of_birth, gender or user.gender)
        if not is_valid_dg:
            return jsonify({'status': 'error', 'message': dg_err}), 400
        dob_val = datetime.strptime(date_of_birth, '%Y-%m-%d').date()

    height_val = None
    if height_cm is not None and str(height_cm).strip() != '':
        try:
            height_val = float(height_cm)
            if height_val <= 0 or height_val > 300:
                return jsonify({'status': 'error', 'message': 'Height must be a positive number.'}), 400
        except (ValueError, TypeError):
            return jsonify({'status': 'error', 'message': 'Height must be a valid number.'}), 400

    weight_val = None
    if weight_kg is not None and str(weight_kg).strip() != '':
        try:
            weight_val = float(weight_kg)
            if weight_val <= 0 or weight_val > 500:
                return jsonify({'status': 'error', 'message': 'Weight must be a positive number.'}), 400
        except (ValueError, TypeError):
            return jsonify({'status': 'error', 'message': 'Weight must be a valid number.'}), 400

    try:
        user.full_name = full_name
        user.email = email
        user.date_of_birth = dob_val
        user._legacy_age = calculate_age(dob_val) if dob_val else user._legacy_age
        user.gender = gender if gender else user.gender
        user.phone = phone if phone else None
        user.primary_sport = primary_sport if primary_sport else user.primary_sport
        user.height_cm = height_val
        user.weight_kg = weight_val
        user.emergency_name = emergency_name if emergency_name else None
        user.emergency_relationship = emergency_relationship if emergency_relationship else None
        user.emergency_phone = emergency_phone if emergency_phone else None

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
    """API Endpoint for uploading and persisting athlete profile photo with MIME/binary verification."""
    user = User.query.get(session.get('user_id'))
    if not user:
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

    filename_saved = None
    ext = 'jpg'

    if 'profile_photo' in request.files:
        file = request.files['profile_photo']
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file.'}), 400

        file_bytes = file.read()
        is_valid, err_msg, detected_ext = validate_image_file(file_bytes, file.filename)
        if not is_valid:
            return jsonify({'status': 'error', 'message': err_msg}), 400

        ext = detected_ext
        filename_saved = f"ath_{user.id:04d}.{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename_saved)
        
        with open(filepath, 'wb') as f:
            f.write(file_bytes)

    elif request.is_json and 'photo_base64' in request.json:
        base64_data = request.json['photo_base64']
        inferred_ext = 'jpg'
        if ',' in base64_data:
            header, base64_data = base64_data.split(',', 1)
            if 'png' in header:
                inferred_ext = 'png'
            elif 'webp' in header:
                inferred_ext = 'webp'

        try:
            image_bytes = base64.b64decode(base64_data)
            is_valid, err_msg, detected_ext = validate_image_file(image_bytes, f"profile.{inferred_ext}")
            if not is_valid:
                return jsonify({'status': 'error', 'message': err_msg}), 400

            ext = detected_ext
            filename_saved = f"ath_{user.id:04d}.{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename_saved)

            with open(filepath, 'wb') as f:
                f.write(image_bytes)
        except Exception as e:
            return jsonify({'status': 'error', 'message': 'Invalid base64 image data.'}), 400
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

        risk_lbl_lower = (prediction['risk_label'] or '').lower()
        if 'high' in risk_lbl_lower or 'medium' in risk_lbl_lower:
            if not record.review_status or record.review_status == 'No Action Required':
                record.review_status = 'Pending Review'
        else:
            if not record.review_status:
                record.review_status = 'No Action Required'

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


def calculate_period_summary(user_id, days_count, period_label):
    """
    Helper function to calculate period health averages, prediction counts,
    risk distributions, and trend data for the authenticated athlete.
    """
    today = datetime.utcnow().date()
    start_date = today - timedelta(days=days_count - 1)
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = today.strftime('%Y-%m-%d')

    # Query records within date range strictly for current athlete
    records = DailyHealthRecord.query.filter(
        DailyHealthRecord.user_id == user_id,
        DailyHealthRecord.record_date >= start_date_str,
        DailyHealthRecord.record_date <= end_date_str
    ).order_by(DailyHealthRecord.record_date.asc(), DailyHealthRecord.id.asc()).all()

    # Fallback to latest records if date range has no records but user has historical entries
    if not records:
        all_records = DailyHealthRecord.query.filter_by(user_id=user_id).order_by(
            DailyHealthRecord.record_date.desc(), DailyHealthRecord.id.desc()
        ).limit(days_count).all()
        if all_records:
            records = list(reversed(all_records))

    if not records:
        return {
            'status': 'success',
            'has_data': False,
            'period': period_label,
            'days_count': days_count,
            'message': f'No health data available for the selected {period_label} period.'
        }

    total_records = len(records)
    avg_sleep = round(sum(r.sleep_hours for r in records) / total_records, 1)
    avg_training = round(sum(r.training_hours for r in records) / total_records, 1)
    avg_rhr = round(sum(r.resting_heart_rate for r in records) / total_records, 1)
    avg_fatigue = round(sum(r.fatigue_level for r in records) / total_records, 1)
    avg_stress = round(sum(r.stress_level for r in records) / total_records, 1)

    pred_records = [r for r in records if r.risk_score is not None]
    prediction_count = len(pred_records)
    avg_risk_score = round(sum(r.risk_score for r in pred_records) / prediction_count, 1) if prediction_count > 0 else 0.0

    low_cnt = sum(1 for r in pred_records if (r.risk_label or '').lower() == 'low risk')
    med_cnt = sum(1 for r in pred_records if (r.risk_label or '').lower() == 'medium risk')
    high_cnt = sum(1 for r in pred_records if (r.risk_label or '').lower() == 'high risk')

    trend = []
    for r in records:
        if r.risk_score is not None:
            trend.append({
                'date': r.record_date,
                'risk_score': round(float(r.risk_score), 1),
                'risk_label': r.risk_label or 'Low Risk'
            })

    return {
        'status': 'success',
        'has_data': True,
        'period': period_label,
        'days_count': days_count,
        'total_records': total_records,
        'prediction_count': prediction_count,
        'averages': {
            'sleep_hours': avg_sleep,
            'training_hours': avg_training,
            'resting_heart_rate': avg_rhr,
            'fatigue_level': avg_fatigue,
            'stress_level': avg_stress,
            'risk_score': avg_risk_score
        },
        'risk_distribution': {
            'low': low_cnt,
            'medium': med_cnt,
            'high': high_cnt
        },
        'trend': trend
    }


@app.route('/api/weekly-summary')
@login_required
def get_weekly_summary_api():
    """REST API returning 7-day health summary and risk trends for authenticated athlete."""
    user_id = session.get('user_id')
    data = calculate_period_summary(user_id, days_count=7, period_label='weekly')
    return jsonify(data)


@app.route('/api/monthly-summary')
@login_required
def get_monthly_summary_api():
    """REST API returning 30-day health summary and risk trends for authenticated athlete."""
    user_id = session.get('user_id')
    data = calculate_period_summary(user_id, days_count=30, period_label='monthly')
    return jsonify(data)


@app.route('/api/dashboard-data')
@login_required
def get_dashboard_data():
    """API endpoint providing dynamic athlete dashboard statistics, trends, and risk distributions from MySQL."""
    user = User.query.get(session.get('user_id'))
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    records = DailyHealthRecord.query.filter_by(user_id=user.id).order_by(
        DailyHealthRecord.record_date.asc(),
        DailyHealthRecord.id.asc()
    ).all()

    if not records:
        return jsonify({
            'status': 'success',
            'has_predictions': False,
            'model_status': 'Random Forest Model Active',
            'user': {
                'id': user.id,
                'full_name': user.full_name,
                'primary_sport': user.primary_sport,
                'profile_photo': user.profile_photo
            }
        })

    latest_rec = records[-1]
    total_preds = len(records)
    avg_sleep = round(sum(r.sleep_hours for r in records) / total_preds, 1)
    avg_train = round(sum(r.training_hours for r in records) / total_preds, 1)

    latest_score = round(latest_rec.risk_score, 1) if latest_rec.risk_score is not None else 0.0
    latest_label = latest_rec.risk_label or 'Low Risk'

    badge_color = 'success'
    if latest_score > 65:
        badge_color = 'danger'
    elif latest_score > 30:
        badge_color = 'warning'

    # Risk Distribution Counts
    low_cnt = sum(1 for r in records if (r.risk_label or '').lower() == 'low risk')
    med_cnt = sum(1 for r in records if (r.risk_label or '').lower() == 'medium risk')
    high_cnt = sum(1 for r in records if (r.risk_label or '').lower() == 'high risk')

    # Health Trends (Last 7 Records)
    recent_7 = records[-7:]
    labels_7 = [r.record_date for r in recent_7]
    sleep_7 = [r.sleep_hours for r in recent_7]
    train_7 = [r.training_hours for r in recent_7]
    hr_7 = [r.resting_heart_rate for r in recent_7]

    # Health Trends (30 Days / All Records)
    recent_30 = records[-30:]
    labels_30 = [r.record_date for r in recent_30]
    sleep_30 = [r.sleep_hours for r in recent_30]
    train_30 = [r.training_hours for r in recent_30]
    hr_30 = [r.resting_heart_rate for r in recent_30]

    # Recent Predictions List
    rec_pred_list = []
    for r in list(reversed(records))[:5]:
        r_score = round(r.risk_score, 1) if r.risk_score is not None else 0.0
        r_label = r.risk_label or 'Low Risk'
        r_badge = 'success'
        if r_score > 65:
            r_badge = 'danger'
        elif r_score > 30:
            r_badge = 'warning'
        rec_pred_list.append({
            'date': r.record_date,
            'risk_level': r_label,
            'risk_percent': r_score,
            'status': 'Completed',
            'badge_class': r_badge
        })

    # Today's Record / Latest Record Overview
    today_str = datetime.utcnow().strftime('%Y-%m-%d')
    today_rec = next((r for r in records if r.record_date == today_str), latest_rec)

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
            'injury_risk_percent': latest_score,
            'risk_level': latest_label,
            'risk_badge_color': badge_color,
            'total_predictions': total_preds,
            'avg_sleep_hrs': avg_sleep,
            'avg_training_hrs': avg_train,
            'last_prediction_date': latest_rec.record_date
        },
        'risk_summary': {
            'risk_level': latest_label,
            'risk_percent': latest_score,
            'predicted_on': latest_rec.record_date
        },
        'health_trends': {
            '7_days': {
                'labels': labels_7,
                'sleep': sleep_7,
                'training': train_7,
                'resting_hr': hr_7
            },
            '30_days': {
                'labels': labels_30,
                'sleep': sleep_30,
                'training': train_30,
                'resting_hr': hr_30
            }
        },
        'risk_distribution': {
            'labels': ['Low Risk', 'Medium Risk', 'High Risk'],
            'counts': [low_cnt, med_cnt, high_cnt],
            'colors': ['#22c55e', '#f59e0b', '#ef4444']
        },
        'recent_predictions': rec_pred_list,
        'todays_health_overview': {
            'sleep_hrs': f"{today_rec.sleep_hours} hrs",
            'training_hrs': f"{today_rec.training_hours} hrs",
            'heart_rate': f"{today_rec.resting_heart_rate} bpm",
            'fatigue': f"Level {today_rec.fatigue_level}/10",
            'stress': f"Level {today_rec.stress_level}/10",
            'previous_injury': 'Yes' if today_rec.previous_injury else 'No',
            'has_today_data': True
        }
    }

    return jsonify(payload)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"AthleteGuard AI running on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
