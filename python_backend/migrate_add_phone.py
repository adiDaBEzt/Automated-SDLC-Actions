"""
Migration script to add phone column to users table
Run this script to update existing databases with the new phone field
"""
import sqlite3
import sys
from pathlib import Path

def migrate_database(db_path: str = "galaxium_travels.db"):
    """Add phone column to users table"""
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if phone column already exists
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'phone' in columns:
            print("✓ Phone column already exists in users table")
            conn.close()
            return True
        
        # Add phone column with a default value for existing records
        print("Adding phone column to users table...")
        cursor.execute("""
            ALTER TABLE users 
            ADD COLUMN phone TEXT NOT NULL DEFAULT ''
        """)
        
        conn.commit()
        print("✓ Successfully added phone column to users table")
        
        # Verify the change
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        print(f"✓ Current columns in users table: {', '.join(columns)}")
        
        conn.close()
        return True
        
    except sqlite3.Error as e:
        print(f"✗ Database error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    # Get database path from command line or use default
    db_path = sys.argv[1] if len(sys.argv) > 1 else "galaxium_travels.db"
    
    # Check if database exists
    if not Path(db_path).exists():
        print(f"✗ Database file not found: {db_path}")
        print("Please run the application first to create the database, or specify the correct path")
        sys.exit(1)
    
    print(f"Migrating database: {db_path}")
    success = migrate_database(db_path)
    
    if success:
        print("\n✓ Migration completed successfully!")
        sys.exit(0)
    else:
        print("\n✗ Migration failed!")
        sys.exit(1)

# Made with Bob
