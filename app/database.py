###################################################
#Purpose: Handles the database connection and session management.
#How it works:
#   Creates a session with the database using SQLAlchemy.
#   Defines functions for connecting to the database and managing sessions.
#   Provides the base class for SQLAlchemy models.
###################################################


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:Sairock123$@localhost:3306/demo"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
