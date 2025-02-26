from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

# Database URL format: postgresql://username:password@host:port/dbname
DATABASE_URL = "postgresql://postgres:password@localhost:5432/mobileappdb"

try:
    # Test connection immediately
    print("Attempting to connect to database...")
    engine = create_engine(DATABASE_URL, echo=True)
    
    # Trying to establish connection
    with engine.connect() as conn:
        print(f"Successfully connected to PostgreSQL")

except Exception as e:
    print(f"Error connecting to database: {e}")
    print("\nPlease check the following:")
    print("1. Ensure PostgreSQL is running.")
    print("2. Ensure the database 'mobileappdb' exists.")
    print("3. Check the username and password in the DATABASE_URL.")
    print("4. Ensure PostgreSQL is accepting connections on port 5432.")
    sys.exit(1)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for declarative models
Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_tables():
    """Check which tables exist in the database"""
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    print("\nExisting tables:")
    for table in existing_tables:
        print(f"- {table}")
        # Optional: Print columns for each table
        columns = inspector.get_columns(table)
        for column in columns:
            print(f"  • {column['name']}: {column['type']}")
