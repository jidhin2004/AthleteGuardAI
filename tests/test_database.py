import unittest
from sqlalchemy import inspect, text
from app import app, db, User, DailyHealthRecord

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_mysql_connection_and_tables_exist(self):
        """Verify active MySQL connection and existence of all required tables."""
        inspector = inspect(db.engine)
        existing_tables = set(inspector.get_table_names())
        required_tables = {
            'users', 'daily_health_records', 'injuries',
            'medical_conditions', 'allergies', 'medications',
            'surgeries', 'admin_notes', 'notifications'
        }
        missing = required_tables - existing_tables
        self.assertEqual(len(missing), 0, f"Missing MySQL tables: {missing}")

    def test_user_foreign_key_cascade_or_integrity(self):
        """Verify database integrity and column constraints on users table."""
        inspector = inspect(db.engine)
        columns = [c['name'] for c in inspector.get_columns('users')]
        self.assertIn('role', columns)
        self.assertIn('account_status', columns)
        self.assertIn('gender', columns)
        self.assertIn('date_of_birth', columns)

if __name__ == '__main__':
    unittest.main()
