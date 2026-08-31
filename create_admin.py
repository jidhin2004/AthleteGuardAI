import argparse
from app import app, db
from models.user import User

def create_or_upgrade_admin(email, password, name):
    with app.app_context():
        # Ensure schema table & role column exist
        db.create_all()
        
        user = User.query.filter_by(email=email).first()
        if user:
            user.role = 'admin'
            user.set_password(password)
            user.full_name = name
            db.session.commit()
            print("==================================================")
            print("ATHLETEGUARD AI — ADMIN ACCOUNT SETUP")
            print("==================================================")
            print(f"[SUCCESS] Existing user upgraded to Admin!")
            print(f" - ID: ATH-{user.id:04d}")
            print(f" - Name: {user.full_name}")
            print(f" - Email: {user.email}")
            print(f" - Role: {user.role}")
            print("==================================================")
        else:
            admin_user = User(
                full_name=name,
                age=35,
                gender='Other',
                primary_sport='Administration',
                email=email,
                role='admin'
            )
            admin_user.set_password(password)
            db.session.add(admin_user)
            db.session.commit()
            print("==================================================")
            print("ATHLETEGUARD AI — ADMIN ACCOUNT SETUP")
            print("==================================================")
            print(f"[SUCCESS] New Admin account created successfully!")
            print(f" - ID: ATH-{admin_user.id:04d}")
            print(f" - Name: {admin_user.full_name}")
            print(f" - Email: {admin_user.email}")
            print(f" - Role: {admin_user.role}")
            print("==================================================")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create or upgrade an Admin account for AthleteGuard AI.")
    parser.add_argument('--email', default='admin@athleteguard.ai', help="Admin email address")
    parser.add_argument('--password', default='AdminPassword123!', help="Admin password")
    parser.add_argument('--name', default='System Administrator', help="Admin full name")

    args = parser.parse_args()
    create_or_upgrade_admin(args.email, args.password, args.name)
