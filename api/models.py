from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4

# Tabela
class LivroBase(SQLModel):
    autor: str = Field(index=True)
    titulo: str = Field(index=True)
    editora: str = Field(index=True)
    ano: int = Field(index=True)


class Livro(LivroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uuid: UUID = Field(default_factory=uuid4, unique=True)


# Schemas de entrada
class LivroPayload(LivroBase):
    """Usado tanto para POST quanto para PUT (todos os campos obrigatórios)."""
    ...


class LivroPatch(SQLModel):
    """Usado para PATCH (todos os campos opcionais)."""
    autor: str | None = None
    titulo: str | None = None
    editora: str | None = None
    ano: int | None = None

# Schemas de saída
class LivroResposta(LivroBase):
    uuid: UUID

    model_config = {"from_attributes": True}


class ConfirmaDelete(BaseModel):
    mensagem: str
    uuid: UUID