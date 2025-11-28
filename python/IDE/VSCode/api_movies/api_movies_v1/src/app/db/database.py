"""
Database configuration and session management for the Movies API.
"""
import os
from sqlmodel import Session, SQLModel, create_engine

# Database URL
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:password@db:5432/moviesdb"
)

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Get session dependency
def get_session():
    with Session(engine) as session:
        yield session

# Create tables
def create_tables():
    SQLModel.metadata.create_all(engine)

# Test connection
def test_connection():
    try:
        with engine.connect() as connection:
            connection.exec_driver_sql("SELECT 1")
            return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
