###################################################
#Purpose: Contains the CRUD operations for interacting with the database.
#How it works:
#   Defines functions that execute database operations (e.g., create, read, update, delete).
#   These functions interact with the database models and perform the operations requested by the API endpoints.
###################################################


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.auth import oauth2_scheme

book_router = APIRouter()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    # Token verification can be expanded here
    return db.query(models.User).first()

@book_router.post("/books", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db), user=Depends(get_current_user)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@book_router.get("/books", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(database.get_db), user=Depends(get_current_user)):
    return db.query(models.Book).all()

@book_router.put("/books/{id}", response_model=schemas.BookResponse)
def update_book(id: int, book: schemas.BookCreate, db: Session = Depends(database.get_db), user=Depends(get_current_user)):
    db_book = db.query(models.Book).filter(models.Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@book_router.delete("/books/{id}")
def delete_book(id: int, db: Session = Depends(database.get_db), user=Depends(get_current_user)):
    db_book = db.query(models.Book).filter(models.Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted"}
