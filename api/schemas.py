from pydantic import BaseModel, field_validator
from sqlmodel import Field, SQLModel
from uuid import UUID


# --- Schemas de entrada ---

class LivroPayload(SQLModel):
    """Usado tanto para POST quanto para PUT (todos os campos obrigatórios)."""
    autor: str = Field(min_length=1, max_length=200)
    titulo: str = Field(min_length=1, max_length=300)
    editora: str = Field(min_length=1, max_length=200)
    ano: int = Field(ge=1000, le=2100)

    @field_validator("autor", "titulo", "editora", mode="before")
    @classmethod
    def strip_strings(cls, v: str) -> str:
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

class LivroResposta(SQLModel):
    id: int
    uuid: UUID
    autor: str
    titulo: str
    editora: str
    ano: int

    model_config = {"from_attributes": True}


class ConfirmaDelete(BaseModel):
    mensagem: str
    uuid: UUID