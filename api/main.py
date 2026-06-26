import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.core.config import get_settings
from api.database.database import criar_db_tabelas, popular_banco_com_csv
from api.routers import livros_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_db_tabelas()
    popular_banco_com_csv()
    yield


settings = get_settings()

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(livros_router.router)