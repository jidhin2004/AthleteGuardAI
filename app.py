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

    # Initial context for template rendering
    dashboard_data = {
        'injury_risk_percent': 18,
        'risk_level': 'Low Risk',
        'risk_badge_color': 'success',
        'last_prediction_date': '12 August 2026',
        'total_predictions': 12,
        'avg_sleep': 7.4,
        'avg_training': 3.2,
        'has_predictions': True
    }

    return render_template('dashboard.html', user=user, data=dashboard_data)


# ==========================================
# SEMESTER 3 MODULE ROUTES (PROTECTED)
# ==========================================

@app.route('/profile')
@login_required
def profile():
    """Athlete Profile Management Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('profile.html', user=user)


@app.route('/medical-history')
@login_required
def medical_history():
    """Medical History Management Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('medical_history.html', user=user)


@app.route('/daily-monitoring')
@login_required
def daily_monitoring():
    """Daily Health Monitoring Form Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('daily_monitoring.html', user=user)


@app.route('/prediction-history')
@login_required
def prediction_history():
    """Prediction History Page."""
    user = User.query.get(session.get('user_id'))
    return render_template('prediction_history.html', user=user)


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


# ==========================================
# DECOUPLED API LAYER FOR DASHBOARD DATA
# ==========================================

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
        'user': {
            'id': user.id,
            'full_name': user.full_name,
            'primary_sport': user.primary_sport
        },
        'stats': {
            'injury_risk_percent': 18,
            'risk_level': 'LOW',
            'risk_badge_color': 'success',
            'total_predictions': 12,
            'avg_sleep_hrs': 7.4,
            'avg_training_hrs': 3.2,
            'last_prediction_date': '12 Aug 2026'
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
            {'date': '12 Aug 2026', 'risk_level': 'Low', 'risk_percent': 18, 'status': 'Completed', 'badge_class': 'success'},
            {'date': '10 Aug 2026', 'risk_level': 'Medium', 'risk_percent': 54, 'status': 'Completed', 'badge_class': 'warning'},
            {'date': '07 Aug 2026', 'risk_level': 'Low', 'risk_percent': 21, 'status': 'Completed', 'badge_class': 'success'}
        ],
        'todays_health_overview': {
            'sleep_hrs': '7.2 hrs',
            'training_hrs': '3.5 hrs',
            'heart_rate': '72 bpm',
            'fatigue': 'Low',
            'stress': 'Moderate',
            'previous_injury': 'No'
        }
    }

    return jsonify(payload)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"AthleteGuard AI running on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
