from pydantic import BaseModel
from typing import List, Optional


# ============================================================
# Perfis
# ============================================================


class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes = True


class PerfilCreate(BaseModel):
    idade: int
    endereco: str


# ============================================================
# Estudantes
# ============================================================


class Estudante(BaseModel):
    id: int
    nome: str
    email: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True


class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: Optional[PerfilCreate] = None


# ============================================================
# Matriculas
# ============================================================


class MatriculaBase(BaseModel):
    estudante_id: int
    nome_disciplina: str


class MatriculaCreate(MatriculaBase):
    pass


class MatriculaResponse(MatriculaBase):
    id: int

    class Config:
        from_attributes = True