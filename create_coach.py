import argparse
import sys
from app import app, db
from models.user import User

def create_or_upgrade_coach(email, password, name, sport="General Sports"):
    """
    Controlled administrative utility to safely create or upgrade a Coach account.
    """
    with app.app_context():
        db.create_all()
        
        user = User.query.filter_by(email=email).first()
        if user:
            user.role = 'coach'
            user.set_password(password)
            user.full_name = name
            if sport:
                user.primary_sport = sport
            user.account_status = 'active'
            db.session.commit()
            print("==================================================")
            print("ATHLETEGUARD AI — COACH ACCOUNT SETUP")
            print("==================================================")
            print(f"[SUCCESS] Existing user account upgraded to Coach!")
            print(f" - ID: ATH-{user.id:04d}")
            print(f" - Name: {user.full_name}")
            print(f" - Email: {user.email}")
            print(f" - Sport: {user.primary_sport}")
            print(f" - Role: {user.role}")
            print("==================================================")
            return user
        else:
            coach_user = User(
                full_name=name,
                _legacy_age=35,
                gender='Male',
                primary_sport=sport,
                email=email,
                role='coach',
                account_status='active'
            )
            coach_user.set_password(password)
            db.session.add(coach_user)
            db.session.commit()
            print("==================================================")
            print("ATHLETEGUARD AI — COACH ACCOUNT SETUP")
            print("==================================================")
            print(f"[SUCCESS] New Coach account created successfully!")
            print(f" - ID: ATH-{coach_user.id:04d}")
            print(f" - Name: {coach_user.full_name}")
            print(f" - Email: {coach_user.email}")
            print(f" - Sport: {coach_user.primary_sport}")
            print(f" - Role: {coach_user.role}")
            print("==================================================")
            return coach_user

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create or upgrade a Coach account for AthleteGuard AI.")
    parser.add_argument('--email', default='coach@athleteguard.ai', help="Coach email address")
    parser.add_argument('--password', default='CoachPassword123!', help="Coach password")
    parser.add_argument('--name', default='Head Coach Marcus', help="Coach full name")
    parser.add_argument('--sport', default='Basketball', help="Coach primary sport")

    args = parser.parse_args()
    create_or_upgrade_coach(args.email, args.password, args.name, args.sport)
