import csv
import logging
from pathlib import Path
from sqlmodel import create_engine, Session, SQLModel, select
from api.core.config import get_settings
from api.models import Livro

logger = logging.getLogger(__name__)

settings = get_settings()
engine = create_engine(settings.database_url, echo=settings.db_echo)


def criar_db_tabelas() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def popular_banco_com_csv(caminho_csv: Path | None = None) -> None:
    if caminho_csv is None:
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

        session.add_all(livros)
        session.commit()
        logger.info(f"{len(livros)} livros importados com sucesso.")