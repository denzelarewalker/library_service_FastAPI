from typing import Optional
from pydantic import BaseModel
from datetime import date

class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

#---------------------------------

class BookBase(BaseModel):
    title: str
    description: str
    author_id: int
    available_copies: int = 0

class BookCreate(BookBase):
    available_copies: int =+ 1

class Book(BookBase):
    id: int
    
    class Config:
        orm_mode = True

class BookUpdate(BookBase):
    title: Optional[str] = None
    description: Optional[str] = None
    author_id: Optional[int] = None
# # ... аналогичные схемы для Book и Borrow ...

class BorrowBase(BaseModel):
    book_id: int
    reader_name: str
    borrow_date: date = date.today()
    return_date: Optional[date] = None

class BorrowCreate(BorrowBase):
    pass


class BorrowReturn(BorrowBase):
    return_date: date = date.today()


class Borrow(BorrowBase):
    id: int

    class Config:
        orm_mode = True

