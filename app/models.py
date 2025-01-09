####################################################
#Purpose: Contains SQLAlchemy ORM models (or other ORM tools) that define the database tables and their relationships.
#How it works:
#   Defines tables and their columns (e.g., users, books).
#   Includes relationships between tables using  relationship, etc.
#####################################################


from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(300))

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    author = Column(String(50), index=True)
    description = Column(String(100))
