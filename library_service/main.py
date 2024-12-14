from datetime import date
from typing import Optional
import uvicorn
from fastapi import Body, Depends, FastAPI, HTTPException, Path, Query
from sqlalchemy.orm import Session
from . import models, schemas, database, crud


# Создание всех таблиц
models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"start_page": "library_service"}


@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)

@app.get("/authors/", response_model=list[schemas.Author])
#def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return authors

@app.get("/authors/{author_id}", response_model=schemas.Author)
#def read_author(author_id: int = Path(..., gt=0), db: Session = Depends(get_db)):  
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@app.put("/authors/{author_id}")
def update_author(
    author_id: int,
    author: schemas.AuthorUpdate,  # Используем AuthorUpdate для проверки входных данных
    db: Session = Depends(get_db),
):
    db_author = crud.update_author(db, author_id=author_id, author=author)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author



@app.delete("/authors/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.delete_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    book: schemas.BookUpdate,  # Используем BookUpdate для проверки входных данных
    db: Session = Depends(get_db),
):
    db_book = crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.post("/borrows/", response_model=schemas.Borrow)
def create_borrow(borrow: schemas.BorrowCreate, db: Session = Depends(get_db)):
    return crud.create_borrow(db=db, borrow=borrow)


@app.get("/borrows/", response_model=list[schemas.Borrow])
def read_borrows(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    borrows = crud.get_borrows(db, skip=skip, limit=limit)
    return borrows


@app.get("/borrows/{borrow_id}", response_model=schemas.Borrow)
def read_borrow(borrow_id: int, db: Session = Depends(get_db)):
    db_borrow = crud.get_borrow(db, borrow_id=borrow_id)
    if db_borrow is None:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return db_borrow

@app.patch("/borrows/{borrow_id}/return")
def return_borrow(borrow_id: int, 
                  return_date: Optional[schemas.BorrowReturn] = None,
                  db: Session = Depends(get_db)):
    # Если return_date не передан, устанавливаем текущую дату
    if return_date is None:
        return_date = date.today()
    else:
        return_date = return_date.return_date  # Берем дату из схемы
    try:
        crud.return_borrow(db, borrow_id=borrow_id, return_date = return_date)
        return {"message": f"Borrow ID {borrow_id} returned"}
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


