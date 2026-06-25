from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.database.database import criar_db_tabelas, popular_banco_com_csv
from api.routers import livros_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Cria as tabelas
    criar_db_tabelas()

    # 2. CHAMA A FUNÇÃO AQUI
    popular_banco_com_csv() 
    
    yield

app = FastAPI(title="API de livros", lifespan=lifespan)
app.include_router(livros_router.router)