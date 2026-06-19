from uuid import UUID
from sqlmodel import create_engine, Session, SQLModel, select
from pathlib import Path
from api.models import Livro

DATABASE_PATH = Path("database.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
CONNECT_ARGS = {"check_same_thread": False} #sqlite

engine = create_engine(DATABASE_URL, connect_args=CONNECT_ARGS)

def criar_db_tabelas():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

