from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import get_settings

# Load settings
settings = get_settings()

# Base class for all models
Base = declarative_base()

# Database Engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    echo=True,  # Optional: shows SQL queries in terminal
)

# Session Factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()