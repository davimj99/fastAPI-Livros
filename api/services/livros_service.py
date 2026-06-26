from uuid import UUID, uuid4

from fastapi import HTTPException
from sqlmodel import Session, col, func, select

from api.models import ConfirmaDelete, Livro, LivroPayload, LivroPatch, LivroResposta


def _get_or_404(livro_id: UUID, session: Session) -> Livro:
    livro = session.exec(select(Livro).where(Livro.uuid == livro_id)).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro


def listar_livros(
    session: Session,
    page: int,
    page_size: int,
    autor: str | None = None,
    titulo: str | None = None,
    editora: str | None = None,
) -> tuple[list[LivroResposta], int, int]:

    query = select(Livro)

    if autor:
        query = query.where(col(Livro.autor).ilike(f"%{autor}%"))
    if titulo:
        query = query.where(col(Livro.titulo).ilike(f"%{titulo}%"))
    if editora:
        query = query.where(col(Livro.editora).ilike(f"%{editora}%"))

    total_items: int = session.exec(
        select(func.count()).select_from(query.subquery())
    ).one()

    total_pages = max(1, (total_items + page_size - 1) // page_size)
    page = min(page, total_pages)
    offset = (page - 1) * page_size

    livros = session.exec(query.offset(offset).limit(page_size)).all()
    return [LivroResposta.model_validate(l) for l in livros], total_items, total_pages


def obter_livro(livro_id: UUID, session: Session) -> LivroResposta:
    livro = _get_or_404(livro_id, session)
    return LivroResposta.model_validate(livro)


def criar_livro(payload: LivroPayload, session: Session) -> LivroResposta:
    livro = Livro(uuid=uuid4(), **payload.model_dump())
    session.add(livro)
    session.commit()
    session.refresh(livro)
    return LivroResposta.model_validate(livro)


def substituir_livro(livro_id: UUID, payload: LivroPayload, session: Session) -> LivroResposta:
    livro = _get_or_404(livro_id, session)

    for key, value in payload.model_dump().items():
        setattr(livro, key, value)

    session.add(livro)
    session.commit()
    session.refresh(livro)
    return LivroResposta.model_validate(livro)


def atualizar_livro(livro_id: UUID, patch: LivroPatch, session: Session) -> LivroResposta:
    update_data = patch.model_dump(exclude_unset=True, exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="Nenhum dado válido enviado para atualização.")

    livro = _get_or_404(livro_id, session)

    for key, value in update_data.items():
        setattr(livro, key, value)

    session.add(livro)
    session.commit()
    session.refresh(livro)
    return LivroResposta.model_validate(livro)


def deletar_livro(livro_id: UUID, session: Session) -> ConfirmaDelete:
    livro = _get_or_404(livro_id, session)
    titulo = livro.titulo
    session.delete(livro)
    session.commit()
    return ConfirmaDelete(mensagem=f"Livro '{titulo}' deletado.", uuid=livro_id)