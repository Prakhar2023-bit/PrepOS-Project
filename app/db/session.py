from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 1. Create the Database Engine
# (The 'check_same_thread' argument is only needed for SQLite, we will remove it when we switch to Postgres)
engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# 2. Create a Session Factory
# Each time a web request comes in, we spawn a new session to talk to the DB, then close it.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create a Base Class
# All of our database models (like Users, Roadmaps) will inherit from this class
Base = declarative_base()

# 4. Dependency Injection
# This function hands a database connection to FastAPI, and safely closes it when the request is done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()