from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
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
@router.post("/estudantes/", response_model=schemas.EstudanteResponse)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(**estudante.model_dump())
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante


@router.get("/estudantes/", response_model=List[schemas.EstudanteResponse])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).all()
    return estudantes


# ====================================================================
# Matriculas
# ====================================================================
@router.post("/matriculas/", response_model=schemas.MatriculaResponse)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula


@router.get("/matriculas/", response_model=List[schemas.MatriculaResponse])
def listar_matriculas(db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).all()
    return matriculas
