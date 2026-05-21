"""
Migration script to add phone column to users table
"""
import sqlite3
import os

def migrate():
    """Add phone column to users table"""
    db_path = os.path.join(os.path.dirname(__file__), 'galaxium_travels.db')
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        print("Please run the application first to create the database.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if column already exists
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'phone' in columns:
            print("✓ Phone column already exists in users table")
        else:
            # Add phone column
            cursor.execute("ALTER TABLE users ADD COLUMN phone VARCHAR(20)")
            conn.commit()
            print("✓ Successfully added phone column to users table")
        
    except Exception as e:
        print(f"✗ Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()

# Made with Bob
