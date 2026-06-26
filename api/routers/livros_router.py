from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response
from sqlmodel import Session

from api.database.database import get_session
from api.schemas import ConfirmaDelete, LivroPayload, LivroPatch, LivroResposta
from api.services.livros_service import (
    listar_livros,
    obter_livro,
    criar_livro,
    substituir_livro,
    atualizar_livro,
    deletar_livro,
)

router = APIRouter(prefix="/livros", tags=["livros"])

SessionDep = Annotated[Session, Depends(get_session)]

# Parâmetros de paginação reutilizáveis
PaginaDep = Annotated[int, Query(ge=1, description="Número da página")]
TamanhoDep = Annotated[int, Query(ge=1, le=100, description="Itens por página")]


@router.get("/", response_model=list[LivroResposta], summary="Listar livros")
def listar(  # ← def, não async def (service é síncrono)
    session: SessionDep,
    response: Response,
    page: PaginaDep = 1,
    page_size: TamanhoDep = 20,
    autor: str | None = Query(default=None, description="Filtrar por autor"),
    titulo: str | None = Query(default=None, description="Filtrar por título"),
    editora: str | None = Query(default=None, description="Filtrar por editora"),
) -> list[LivroResposta]:
    livros, total_items, total_pages = listar_livros(
        session, page, page_size, autor, titulo, editora
    )
    response.headers["X-Total-Pages"] = str(total_pages)
    response.headers["X-Total-Items"] = str(total_items)
    response.headers["X-Current-Page"] = str(page)
    response.headers["X-Page-Size"] = str(page_size)
    return livros


@router.get(
    "/{livro_id}",
    response_model=LivroResposta,
    summary="Obter livro por UUID",
    responses={404: {"description": "Livro não encontrado."}},
)
def obter(livro_id: UUID, session: SessionDep) -> LivroResposta:
    return obter_livro(livro_id, session)


@router.post(
    "/",
    response_model=LivroResposta,
    status_code=201,
    summary="Cadastrar novo livro",
)
def criar(payload: LivroPayload, session: SessionDep) -> LivroResposta:
    return criar_livro(payload, session)


@router.put(
    "/{livro_id}",
    response_model=LivroResposta,
    summary="Substituir livro completo",
    responses={404: {"description": "Livro não encontrado."}},
)
def substituir_todo_livro(
    livro_id: UUID, payload: LivroPayload, session: SessionDep
) -> LivroResposta:
    return substituir_livro(livro_id, payload, session)


@router.patch(
    "/{livro_id}",
    response_model=LivroResposta,
    summary="Atualizar campos específicos do livro",
    responses={
        400: {"description": "Nenhum dado válido enviado para atualização."},
        404: {"description": "Livro não encontrado."},
    },
)
def atualizar_por_partes(
    livro_id: UUID, patch: LivroPatch, session: SessionDep
) -> LivroResposta:
    return atualizar_livro(livro_id, patch, session)


@router.delete(
    "/{livro_id}",
    response_model=ConfirmaDelete,
    summary="Deletar livro",
    responses={404: {"description": "Livro não encontrado."}},
)
def deletar(livro_id: UUID, session: SessionDep) -> ConfirmaDelete:
    return deletar_livro(livro_id, session)