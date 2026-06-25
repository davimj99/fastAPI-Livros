import os
import csv
from sqlmodel import create_engine, Session, SQLModel, select
from dotenv import load_dotenv

# Importação correta do seu modelo Livro
from api.models import Livro 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Verificação de segurança da URL
if not DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não foi encontrada!")

engine = create_engine(DATABASE_URL, echo=True)

def criar_db_tabelas():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def popular_banco_com_csv():
    with Session(engine) as session:
        # Verifica se o banco já tem livros para não duplicar os dados
        livro_existente = session.exec(select(Livro)).first()
        if livro_existente:
            print("O banco já possui dados. Pulando a importação do CSV.")
            return

        print("Lendo o arquivo CSV e importando dados...")
        
        try:
            with open("livros.csv", mode="r", encoding="utf-8") as arquivo:
                leitor_csv = csv.DictReader(arquivo, delimiter=';')
                
                for linha in leitor_csv:
                    novo_livro = Livro(
                        titulo=linha["titulo"],
                        autor=linha["autor"],
                        editora=linha["editora"],
                        ano=int(linha["ano"]) 
                    )
                    session.add(novo_livro)
                
                session.commit()
                print("✅ Todos os dados do CSV foram salvos com sucesso!")
                
        except FileNotFoundError:
            print("❌ Arquivo livros.csv não encontrado!")