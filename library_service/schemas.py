from typing import Optional
from pydantic import BaseModel
import datetime

class AuthorCreate(BaseModel):
    #pass
    name: str
    surname: str
    birthdate: Optional[datetime.date]


class AuthorUpdate(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    birthdate: Optional[datetime.date]


# class Author(BaseModel):
#     id: int
#     name: str
#     surname: str
#     birthdate: Optional[datetime.date]

#     class Config:
#         orm_mode = True


# # ... аналогичные схемы для Book и Borrow ...

# class BorrowCreate(BaseModel):
#     #pass
#     book_id: int
#     reader_name: str


# class BorrowUpdate(BaseModel):
#     return_date: Optional[datetime.date]


# class Borrow(BaseModel):
#     id: int
#     book_id: int
#     reader_name: str
#     borrow_date: datetime.date
#     return_date: Optional[datetime.date]

#     class Config:
#         orm_mode = True


from datetime import date


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date



class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

# class BookBase(BaseModel):
#     title: str
#     description: str
#     author_id: int
#     available_copies: int

# class BookCreate(BookBase):
#     pass

# class Book(BookBase):
#     id: int

#     class Config:
#         orm_mode = True

# class BorrowBase(BaseModel):
#     book_id: int
#     reader_name: str
#     borrow_date: date

# class BorrowCreate(BorrowBase):
#     pass

# class Borrow(BorrowBase):
#     id: int
#     return_date: Optional[date]

#     class Config:
#         orm_mode = True