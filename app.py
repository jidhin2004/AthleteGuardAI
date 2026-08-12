import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from sqlalchemy import create_engine
from models import db
from models.user import User

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "athleteguard_ai_secret_key_mca_2026")

# MySQL Configuration with SQLite Fallback
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "athleteguard_db")

USE_MYSQL = os.environ.get("USE_MYSQL", "true").lower() == "true"
MYSQL_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLITE_URI = "sqlite:///athleteguard_dev.db"

# Select DB URI safely
selected_uri = SQLITE_URI
if USE_MYSQL:
    try:
        engine = create_engine(MYSQL_URI, connect_args={"connect_timeout": 3})
        with engine.connect() as conn:
            pass
        selected_uri = MYSQL_URI
        print("Successfully connected to MySQL database.")
    except Exception as e:
        print(f"MySQL connection test failed ({e}). Falling back to SQLite database.")

app.config['SQLALCHEMY_DATABASE_URI'] = selected_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


def login_required(f):
    """Decorator to require login for protected routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in to access your AthleteGuard AI Dashboard.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    """Public Landing Page route."""
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login handler with password verification and session management."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        remember = request.form.get('remember')

        if not email or not password:
            flash("Please enter both Athlete ID/Email and password.", "danger")
            return render_template('login.html')

        # Find user by email
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # Login success -> establish session
            session.permanent = True if remember else False
            session['user_id'] = user.id
            session['user_name'] = user.full_name
            session['user_email'] = user.email
            session['user_sport'] = user.primary_sport

            flash(f"Welcome back, {user.full_name}!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid Athlete ID/Email or password. Please try again.", "danger")
            return render_template('login.html', error_msg="Invalid credentials. Please check your email and password.")

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration handler with password hashing and database storage."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        age = request.form.get('age', '').strip()
        gender = request.form.get('gender', '').strip()
        primary_sport = request.form.get('primary_sport', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()
        terms = request.form.get('terms')

        # Server-side validation checks
        if not all([full_name, age, gender, primary_sport, email, password]):
            flash("All fields are required for registration.", "danger")
            return render_template('register.html')

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('register.html')

        # Check if email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("An account with this email address already exists.", "warning")
            return render_template('register.html', error_msg="Email already registered. Try logging in instead.")

        try:
            # Create user and hash password
            new_user = User(
                full_name=full_name,
                age=int(age),
                gender=gender,
                primary_sport=primary_sport,
                email=email
            )
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()

            # Auto-login after registration
            session['user_id'] = new_user.id
            session['user_name'] = new_user.full_name
            session['user_email'] = new_user.email
            session['user_sport'] = new_user.primary_sport

            flash("Athlete Account created successfully! Welcome to your Dashboard.", "success")
            return redirect(url_for('dashboard'))

        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred during registration: {str(e)}", "danger")
            return render_template('register.html')

    return render_template('register.html')


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

    # Explainable AI & Biometric Metrics for the Athlete
    dashboard_data = {
        'injury_risk_percent': 12,
        'risk_level': 'Low Risk',
        'risk_badge_color': 'success',
        'readiness_score': 94,
        'fatigue_index': 18,
        'heart_rate': 68,
        'vo2_max': 58.4,
        'stride_length': 1.24,
        'ground_contact': 208,
        'weekly_distance_km': 42.5,
        'risk_factors': [
            {'name': 'Hamstring Strain Risk', 'percentage': 14, 'status': 'Optimal'},
            {'name': 'ACL Stress Index', 'percentage': 8, 'status': 'Safe'},
            {'name': 'Workload Spike Factor', 'percentage': 18, 'status': 'Moderate'},
            {'name': 'Asymmetry Index', 'percentage': 5, 'status': 'Optimal'}
        ],
        'ai_recommendations': [
            {'title': 'Optimal Load Limit', 'desc': 'Keep intense sprint training capped at 45 mins today to maintain low hamstring risk.', 'tag': 'AI Insight', 'type': 'info'},
            {'title': 'Hydration & Recovery', 'desc': 'Neuromuscular readiness is at 94%. Recommended post-workout mobility routine attached.', 'tag': 'Recovery', 'type': 'success'}
        ],
        'recent_sessions': [
            {'date': 'Today, 08:30 AM', 'type': 'High Intensity Sprint', 'duration': '45 min', 'distance': '8.2 km', 'risk': '12% Low'},
            {'date': 'Yesterday', 'type': 'Tempo Endurance Run', 'duration': '60 min', 'distance': '12.5 km', 'risk': '15% Low'},
            {'date': '05 Aug 2026', 'type': 'Recovery & Mobility', 'duration': '30 min', 'distance': '3.0 km', 'risk': '5% Low'}
        ]
    }

    return render_template('dashboard.html', user=user, data=dashboard_data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"AthleteGuard AI running on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
