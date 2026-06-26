import os
import csv
import logging
from pathlib import Path  # ← Path resolve o problema do caminho relativo
from sqlmodel import create_engine, Session, SQLModel, select
from dotenv import load_dotenv
from api.models import Livro

load_dotenv()
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL não encontrada no ambiente!")

engine = create_engine(DATABASE_URL, echo=False)  # echo=True só em dev


def criar_db_tabelas() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def popular_banco_com_csv(caminho_csv: Path | None = None) -> None:
    """
    Importa livros do CSV para o banco.
    Usa o arquivo `livros.csv` na raiz do projeto por padrão.
    """
    if caminho_csv is None:
        # __file__ = api/database/database.py → .parent.parent.parent = raiz
        caminho_csv = Path(__file__).parent.parent.parent / "livros.csv"

    with Session(engine) as session:
        if session.exec(select(Livro)).first():
            logger.info("Banco já populado. Pulando importação.")
            return

        if not caminho_csv.exists():
            logger.error(f"Arquivo não encontrado: {caminho_csv}")
            return

        livros: list[Livro] = []

        with open(caminho_csv, encoding="utf-8") as f:
            for i, linha in enumerate(csv.DictReader(f, delimiter=";"), start=1):
                try:
                    livros.append(Livro(
                        titulo=linha["titulo"].strip(),
                        autor=linha["autor"].strip(),
                        editora=linha["editora"].strip(),
                        ano=int(linha["ano"]),
                    ))
                except (KeyError, ValueError) as e:
                    logger.warning(f"Linha {i} ignorada — erro: {e}")

        session.add_all(livros)  # add_all é mais eficiente que add em loop
        session.commit()
        logger.info(f"{len(livros)} livros importados com sucesso.")