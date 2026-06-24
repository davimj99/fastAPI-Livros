from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.database import criar_db_tabelas
from api.routers import livros_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_db_tabelas()
    yield
    #depois da api executar

app = FastAPI(title="API de livros", lifespan=lifespan)
app.include_router(livros_router.router)


