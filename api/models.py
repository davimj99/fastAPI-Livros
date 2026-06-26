from pydantic import BaseModel, field_validator
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4


class LivroBase(SQLModel):
    autor: str = Field(index=True, min_length=1, max_length=200)
    titulo: str = Field(index=True, min_length=1, max_length=300)
    editora: str = Field(index=True, min_length=1, max_length=200)
    ano: int = Field(index=True, ge=1000, le=2100)  # validação de range


class Livro(LivroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uuid: UUID = Field(default_factory=uuid4, unique=True, index=True)


# --- Schemas de entrada ---

class LivroPayload(LivroBase):
    """Usado tanto para POST quanto para PUT (todos os campos obrigatórios)."""

    @field_validator("autor", "titulo", "editora", mode="before")
    @classmethod
    def strip_strings(cls, v: str) -> str:
        """Remove espaços acidentais nas bordas."""
        return v.strip()


class LivroPatch(SQLModel):
    """Usado para PATCH (todos os campos opcionais)."""
    autor: str | None = Field(default=None, min_length=1, max_length=200)
    titulo: str | None = Field(default=None, min_length=1, max_length=300)
    editora: str | None = Field(default=None, min_length=1, max_length=200)
    ano: int | None = Field(default=None, ge=1000, le=2100)

    @field_validator("autor", "titulo", "editora", mode="before")
    @classmethod
    def strip_strings(cls, v: str | None) -> str | None:
        return v.strip() if v else v


# --- Schemas de saída ---

class LivroResposta(LivroBase):
    id: int  # útil para paginação e referências
    uuid: UUID

    model_config = {"from_attributes": True}


class ConfirmaDelete(BaseModel):
    mensagem: str
    uuid: UUID