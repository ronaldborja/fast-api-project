from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/sistemabancario"
read_engine = create_engine(DATABASE_URL)
ReadSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=read_engine)

DATABASE_URL = ""
write_engine = create_engine(DATABASE_URL)
WriteSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=write_engine)

Base = declarative_base()

def get_read_db() -> Generator:
    db = ReadSessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_write_db() -> Generator:
    db = WriteSessionLocal()
    try:
        yield db
    finally:
        db.close()