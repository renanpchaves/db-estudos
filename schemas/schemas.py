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


class Matricula(BaseModel):
    id: int
    estudante_id: int
    disciplina_id: int

    class Config:
        from_attributes = True


class MatriculaCreate(BaseModel):
    estudante_id: int
    disciplina_id: int


# ============================================================
# Disciplinas
# ============================================================


class Disciplina(BaseModel):
    id: int
    nome: str
    professor_id: int

    class Config:
        from_attributes = True


class DisciplinaCreate(BaseModel):
    nome: str
    professor_id: int


# ============================================================
# Professores
# ============================================================


class Professor(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True


class ProfessorCreate(BaseModel):
    nome: str
    email: int
