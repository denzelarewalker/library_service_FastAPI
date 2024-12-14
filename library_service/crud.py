import library_service.schemas as schemas
from sqlalchemy import exists
from sqlalchemy.orm import Session
from datetime import date
from .models import Author, Book, Borrow


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Author).offset(skip).limit(limit).all()

def update_author(db: Session, author_id: int, author: schemas.AuthorUpdate):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if not db_author:
        return None

    # Обновляем только те поля, которые были предоставлены
    for key, value in author.dict(exclude_unset=True).items():
        setattr(db_author, key, value)
        
    db.commit()
    db.refresh(db_author)
    return db_author
    



def delete_author(db: Session, author_id: int):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
        return f'Author with {db_author.id} was deleted'
    else:
        return None
    
def create_book(db: Session, book: schemas.BookCreate):
    # Проверяем, существует ли книга с таким названием и автором
    exists_query = db.query(exists().where(
        (Book.title == book.title) & (Book.author_id == book.author_id)
    )).scalar()

    if exists_query:
        # Книга уже существует, увеличиваем количество копий
        db_book = db.query(Book).filter(
            Book.title == book.title, Book.author_id == book.author_id
        ).first()
        db_book.available_copies += book.available_copies # Увеличиваем кол-во копий
        db.commit()
        db.refresh(db_book)
        return db_book
    else:
        # Книга не существует, создаем новую
        db_book = Book(**book.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None

    # Обновляем только те поля, которые были предоставлены
    for key, value in book.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
        
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        if db_book.available_copies:
            db_book.available_copies -= 1
            db.commit()
            db.refresh(db_book)
            return True
        else:
            return False
    else:
        return False


def create_borrow(db: Session, borrow: schemas.BorrowCreate):
    db_book = db.query(Book).filter(Book.id == borrow.book_id).first()
    if db_book:
        if db_book.available_copies:
            db_book.available_copies -= 1
        else:
            return False
    else:
        return False
    db_borrow = Borrow(**borrow.dict())
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

def get_borrow(db: Session, borrow_id: int):
    return db.query(Borrow).filter(Borrow.id == borrow_id).first()

def get_borrows(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Borrow).offset(skip).limit(limit).all()

def return_borrow(db: Session, borrow_id: int):
    db_borrow = db.query(Borrow).filter(Borrow.id == borrow_id).first()
    if db_borrow:
        db_borrow.return_date = date.today()
        db_book = db.query(Book).filter(Book.id == db_borrow.book_id).first()
        db_book.available_copies += 1
        db.commit()
        db.refresh(db_borrow)
        db.refresh(db_book)
        return db_borrow
    else:
        return None
