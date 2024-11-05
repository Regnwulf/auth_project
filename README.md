# Auth Project

Este projeto é uma API simples de autenticação usando FastAPI e PostgreSQL. Ele implementa autenticação com JWT e fornece rotas protegidas para diferentes papéis de usuários.

## Estrutura do Projeto

```
auth_project/
├── app/
│   ├── main.py              # Ponto de entrada da aplicação FastAPI
│   ├── database/            # Configuração do banco de dados
│   │   └── db.py            # Conexão e gerenciamento do banco de dados
│   ├── models/              # Modelos de dados
│   │   └── user.py          # Modelo de dados para o usuário
│   ├── routes/              # Rotas da API
│   │   └── auth_routes.py   # Rotas relacionadas à autenticação
│   └── services/            # Lógica de negócios e autenticação
│       └── auth_service.py  # Lógica de autenticação e geração de tokens
└── insert_users.py          # Script para inserir usuários fictícios no banco de dados
```

## Requisitos

- Python 3.7 ou superior
- PostgreSQL
- Bibliotecas Python: FastAPI, Psycopg2, Python-Jose

## Configuração

### 1. Clone o Repositório

```bash
git clone git@github.com:Regnwulf/auth_project.git
cd auth_project
```

### 2. Variáveis de Ambiente
```bash
DATABASE_URL=<postgresql://user:password@localhost/auth_api>
SECRET_KEY=<sua_chave_secreta>
ALGORITHM=<HS256>
ACCESS_TOKEN_EXPIRE_MINUTES=<30>
```

### 3. Crie e Ative um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Para Windows use: venv\Scripts\activate
```

### 4. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 5. Configure o Banco de Dados

Certifique-se de que o PostgreSQL está em execução e crie um banco de dados chamado `auth_api`. Você pode usar o seguinte comando no PostgreSQL:

```sql
CREATE DATABASE auth_api;
```

### 6. Insira Usuários Fictícios

Execute o script para inserir usuários fictícios no banco de dados:

```bash
python insert_users.py
```

### 7. Execute a Aplicação

Para iniciar o servidor, execute o seguinte comando:

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Endpoints

### 1. Obter Token

**POST** `/token`

- **Corpo da Requisição**:
    ```json
    {
        "username": "user",
        "password": "L0XuwPOdS5U"
    }
    ```

- **Resposta**:
    ```json
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "bearer"
    }
    ```

### 2. Rota Protegida para Usuários

**GET** `/user`

- **Cabeçalho**:
    ```
    Authorization: Bearer <token>
    ```

- **Resposta**:
    ```json
    {
        "msg": "Você está acessando a rota do usuário!"
    }
    ```

### 3. Rota Protegida para Administradores

**GET** `/admin`

- **Cabeçalho**:
    ```
    Authorization: Bearer <token>
    ```

- **Resposta**:
    ```json
    {
        "msg": "Você está acessando a rota do administrador!"
    }
    ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull.
