from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    perfil = relationship(
        "Perfil",
        uselist=False,
        back_populates="estudante",
        cascade="all, delete-orphan",
    )


class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String(200))
    estudante_id = Column(Integer, ForeignKey("estudantes.id"), unique=True)
    estudante = relationship("Estudante", back_populates="perfil")


class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    disciplina = relationship("Disciplina", back_populates="matriculas")


class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    disciplinas = relationship("Disciplina", back_populates="professor")


class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.id"))
    professor = relationship("Professor", back_populates="disciplinas")
    matriculas = relationship(
        "Matricula", back_populates="disciplina", cascade="all, delete-orphan"
    )
