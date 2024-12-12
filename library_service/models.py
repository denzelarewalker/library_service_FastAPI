import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    #first_name = Column(String, index=True)
    surname = Column(String(50), nullable=False)
    #last_name = Column(String, index=True)
    birthdate = Column(Date)
    #books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    #title = Column(String, index=True)
    description = Column(Text)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    available_copies = Column(Integer, nullable=False, default=1)
    #available_copies = Column(Integer)
    borrows = relationship("Borrow", back_populates="book")


class Borrow(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="borrows")
    #book = relationship("Book")
    reader_name = Column(String(100), nullable=False)
    #reader_name = Column(String)
    borrow_date = Column(Date, default=datetime.date.today())
    #borrow_date = Column(Date)
    return_date = Column(Date)
    #return_date = Column(Date, nullable=True)

    