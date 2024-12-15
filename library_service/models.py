import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    birth_date = Column(Date)
    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(Text)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    available_copies = Column(Integer, default=1)
    borrows = relationship("Borrow", back_populates="book")


class Borrow(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="borrows")
    reader_name = Column(String(100), nullable=False)
    borrow_date = Column(Date, default=datetime.date.today())
    return_date = Column(Date, default=None)

    