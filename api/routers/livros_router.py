from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response
from sqlmodel import Session

from api.database import get_session
from api.models import ConfirmaDelete, LivroPayload, LivroPatch, LivroResposta
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


@router.get("/", response_model=list[LivroResposta])
async def listar(
    session: SessionDep,
    response: Response,
    page: int = Query(1, ge=1),
) -> list[LivroResposta]:
    livros, total_items, total_pages = listar_livros(session, page)
    response.headers["X-Total-Pages"] = str(total_pages)
    response.headers["X-Total-Items"] = str(total_items)
    return livros


@router.get(
    "/{livro_id}",
    response_model=LivroResposta,
    responses={404: {"description": "Livro não encontrado."}},
)
async def obter(livro_id: UUID, session: SessionDep) -> LivroResposta:
    return obter_livro(livro_id, session)


@router.post("/", response_model=LivroResposta, status_code=201)
async def criar(payload: LivroPayload, session: SessionDep) -> LivroResposta:
    return criar_livro(payload, session)


@router.put(
    "/{livro_id}",
    response_model=LivroResposta,
    responses={404: {"description": "Livro não encontrado."}},
)
async def substituir(
    livro_id: UUID, payload: LivroPayload, session: SessionDep
) -> LivroResposta:
    return substituir_livro(livro_id, payload, session)


@router.patch(
    "/{livro_id}",
    response_model=LivroResposta,
    responses={
        400: {"description": "Nenhum dado válido enviado para atualização."},
        404: {"description": "Livro não encontrado."},
    },
)
async def atualizar(
    livro_id: UUID, patch: LivroPatch, session: SessionDep
) -> LivroResposta:
    return atualizar_livro(livro_id, patch, session)


@router.delete(
    "/{livro_id}",           
    response_model=ConfirmaDelete,
    responses={404: {"description": "Livro não encontrado."}},
)
async def deletar(livro_id: UUID, session: SessionDep) -> ConfirmaDelete:
    return deletar_livro(livro_id, session)