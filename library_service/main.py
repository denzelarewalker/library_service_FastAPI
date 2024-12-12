import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Path, Query
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

@app.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, author: schemas.AuthorBase, db: Session = Depends(get_db)):
    db_author = crud.update_author(db, author_id=author_id, author=author)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@app.delete("/authors/{author_id}", response_model=schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.delete_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


