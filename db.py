import sqlite3


def conectar():
    conn = sqlite3.connect("escola.db")
    return conn


def tabela_estudante():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS estudante(
                   id INTEGER PRIMARY KEY,
                   nome TEXT,
                   idade INTEGER)    
    """
    )
    conn.commit()
    conn.close()


def tabela_matricula():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS matricula(
                   id INTEGER PRIMARY KEY,
                   nome_disciplina TEXT,
                   id_estudante INTEGER REFERENCES estudante(id))
        """
    )

    conn.commit()
    conn.close()


def criar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO estudante (nome,idade)
            VALUES (?,?)  
        """,
        (nome, idade),
    )
    conn.commit()
    conn.close()


def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM estudante""")
    estudantes = cursor.fetchall()

    for i in estudantes:
        print(i)
    conn.commit()
    conn.close()


def criar_matricula(id_estudante, nome_disciplina):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO matricula (id_estudante, nome_disciplina)
        VALUES (?,?)
        """,
        (id_estudante, nome_disciplina),
    )
    conn.commit()
    conn.close()


def listar_matriculas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT matricula.id, estudante.nome, matricula.nome_disciplina FROM matricula
        JOIN estudante ON matricula.id_estudante = estudante.id"""
    )
    matriculas = cursor.fetchall()

    for i in matriculas:
        print(i)
    conn.commit()
    conn.close()
