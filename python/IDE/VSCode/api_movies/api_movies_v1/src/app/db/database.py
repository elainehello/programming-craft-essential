"""
Database configuration and session management for the Movies API.
Configured to work with Docker Compose PostgreSQL container.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Database connection configuration
# These should match your .env file variables used in docker-compose.yml
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:password@db:5432/moviesdb"
)

# Alternative way to build URL from individual components
# DATABASE_USER = os.getenv("POSTGRES_USER", "postgres")
# DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password") 
# DATABASE_HOST = os.getenv("DATABASE_HOST", "db")  # Docker service name
# DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
# DATABASE_NAME = os.getenv("POSTGRES_DB", "moviesdb")
# DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    pool_pre_ping=True,  # Validates connections before use
    pool_recycle=300,  # Recreate connections after 5 minutes
)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

# Base class for our models
class Base(DeclarativeBase):
    pass

# Dependency for FastAPI to get database session
def get_db():
    """
    Dependency that provides a database session.
    Use this in FastAPI endpoints to get a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create all tables
def create_tables():
    """
    Create all tables in the database.
    Call this at application startup.
    """
    Base.metadata.create_all(bind=engine)

# Function to test database connection
def test_connection():
    """
    Test the database connection.
    Returns True if successful, False otherwise.
    """
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
