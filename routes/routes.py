from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from typing import List
import schemas
import models

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def read_root():
    return {"API Status": "Ok"}


# ====================================================================
# Estudantes
# ====================================================================
@router.post("/estudantes/", response_model=schemas.Estudante)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(
        nome=estudante.nome,
        email=estudante.email,
        perfil=(
            models.Perfil(**estudante.perfil.model_dump()) if estudante.perfil else None
        ),
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante


@router.get("/estudantes/", response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = (
        db.query(models.Estudante).options(joinedload(models.Estudante.perfil)).all()
    )
    return estudantes


# ====================================================================
# Matriculas
# ====================================================================
@router.post("/matriculas/", response_model=schemas.Matricula)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    estudante = (
        db.query(models.Estudante)
        .filter(models.Estudante.id == matricula.estudante_id)
        .first()
    )
    if not estudante:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula


@router.get("/matriculas/", response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).all()
    return matriculas


# ====================================================================
# Disciplinas
# ====================================================================


@router.post("/disciplinas/", response_model=schemas.Disciplina)
def criar_disciplina(
    disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)
):
    db_disciplina = models.Disciplina(**disciplina.model_dump())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina


# ====================================================================
# Professores
# ====================================================================


@router.post("/professores/", response_model=schemas.Professor)
def criar_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_professor = models.Professor(**professor.model_dump())
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor
