import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.database.database import criar_db_tabelas, popular_banco_com_csv
from api.routers import livros_router

# Configuração de log centralizada
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_db_tabelas()
    popular_banco_com_csv()
    yield

app = FastAPI(
    title="API de Livros",
    description="CRUD de livros com FastAPI + SQLModel",
    version="1.0.0",
)

app.include_router(livros_router.router)