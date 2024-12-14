from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# DATABASE_URL = "sqlite:///./library.db" # Замените на вашу базу данных
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db:5432/db_name"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

