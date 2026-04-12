# Escola DB

Estudo de banco de dados com Python, FastAPI e PostgreSQL.

## Funcionalidades

- Cadastrar e listar estudantes (com perfil opcional)
- Cadastrar e listar matrículas (com validação de estudante existente)
- Cadastrar disciplinas vinculadas a um professor
- Cadastrar e listar professores

## Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- psycopg2

## Estrutura do projeto

```
postgres-studies/
├── database/
│   └── database.py       # Conexão e sessão com o banco
├── models/
│   └── models.py         # Modelos SQLAlchemy
├── schemas/
│   └── schemas.py        # Schemas Pydantic
├── routes/
│   └── routes.py         # Endpoints da API
└── main.py               # Entrypoint da aplicação
```

## Configuração

### 1. PostgreSQL

Certifique que o PostgreSQL está rodando, configure user (caso não esteja configurado) e a database:

```sql
CREATE USER admin WITH PASSWORD 'sua_senha';
CREATE DATABASE escola OWNER admin;
GRANT ALL PRIVILEGES ON DATABASE escola TO admin;
```

### 2. Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost/escola
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o servidor

```bash
uvicorn main:app --reload
```

As tabelas são criadas automaticamente na primeira execução.

## Endpoints

A documentação interativa fica disponível em `http://localhost:8000/docs`.
