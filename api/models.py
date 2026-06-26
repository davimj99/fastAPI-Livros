from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel


class LivroBase(SQLModel):
    autor: str = Field(index=True, min_length=1, max_length=200)
    titulo: str = Field(index=True, min_length=1, max_length=300)
    editora: str = Field(index=True, min_length=1, max_length=200)
    ano: int = Field(index=True, ge=1000, le=2100)


class Livro(LivroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uuid: UUID = Field(default_factory=uuid4, unique=True, index=True)