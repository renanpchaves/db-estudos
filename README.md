# Escola DB

Estudo de banco de dados com Python, FastAPI e PostgreSQL.

## Funcionalidades

- Cadastrar e listar estudantes
- Cadastrar e listar matrículas

## Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- psycopg2

## Configuração

### 1. PostgreSQL

Certifique que o PostgreSQL está rodando e configure user(caso não esteja), e a database:

```sql
CREATE USER admin WITH PASSWORD 'sua_senha';
CREATE DATABASE escola OWNER admin;
GRANT ALL PRIVILEGES ON DATABASE escola TO admin;
```

### 2. Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```
DATABASE_URL=postgresql+psycopg2://admin:sua_senha@localhost/escola
```

### 3. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 4. Rodar o servidor

```powershell
uvicorn main:app --reload
```

As tabelas são criadas automaticamente na primeira execução.

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/estudantes/` | Cadastrar estudante |
| GET | `/estudantes/` | Listar estudantes |
| POST | `/matriculas/` | Cadastrar matrícula |
| GET | `/matriculas/` | Listar matrículas |

A documentação interativa fica disponível em `http://localhost:8000/docs`.
