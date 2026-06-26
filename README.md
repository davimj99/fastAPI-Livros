# 📚 FastAPI Livros — API REST de Gerenciamento de Livros

Projeto desenvolvido durante os estudos de FastAPI, com foco na criação de APIs REST modernas utilizando Python, FastAPI e SQLModel. O projeto evoluiu para uma arquitetura modular com separação de responsabilidades entre routers, services, schemas e banco de dados.

---

## 🚀 Tecnologias Utilizadas

- Python 3.13
- FastAPI
- SQLModel
- Começou em SQLite foi migrado pra PostgreSQL
- Uvicorn
- Pydantic
- UUID

---

## 📂 Estrutura do Projeto

```bash
FASTAPI-LIVROS/
│
├── api/
│   ├── core/                  # Configurações centrais da aplicação
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py        # Configuração e sessão do banco de dados
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── livros_router.py   # Endpoints de livros
│   │
│   ├── services/              # Regras de negócio / lógica de serviço
│   │
│   ├── __init__.py
│   ├── main.py                # Ponto de entrada da aplicação
│   ├── models.py              # Modelos do banco de dados (SQLModel)
│   └── schemas.py             # Schemas de entrada e saída (Pydantic)
│
├── client/                    # Cliente HTTP para teste manual
│
├── notas/                     # Anotações e rascunhos de estudo
│
├── venv/                      # Ambiente virtual (não versionado)
│
├── .env                       # Variáveis de ambiente
├── .gitignore
├── livros.csv                 # Dataset de livros para importação
├── requirements.txt
└── README.md
```

---

## ⚙️ Funcionalidades

### Livros

- ✅ Listar livros (com paginação)
- ✅ Buscar livro por ID
- ✅ Cadastrar livro
- ✅ Atualizar livro completo (PUT)
- ✅ Atualizar livro parcialmente (PATCH)
- ✅ Excluir livro

---

## 🔗 Endpoints

### Listar Livros

```http
GET /livros?page=1
```

---

### Buscar Livro

```http
GET /livros/{livro_id}
```

---

### Cadastrar Livro

```http
POST /livros
```

```json
{
  "autor": "Machado de Assis",
  "titulo": "Dom Casmurro",
  "editora": "Ática",
  "ano": 1899
}
```

---

### Atualizar Livro (completo)

```http
PUT /livros/{livro_id}
```

```json
{
  "autor": "Machado de Assis",
  "titulo": "Dom Casmurro",
  "editora": "Editora Atualizada",
  "ano": 1900
}
```

---

### Atualização Parcial

```http
PATCH /livros/{livro_id}
```

```json
{
  "titulo": "Dom Casmurro - Edição Especial"
}
```

---

### Excluir Livro

```http
DELETE /livros/{livro_id}
```

---

## 🗄️ Banco de Dados

O projeto utiliza **SQLite** para persistência dos dados, configurado em `api/database/database.py`.

Modelagem principal (`api/models.py`):

```
Livro
├── uuid      (chave primária)
├── autor
├── titulo
├── editora
└── ano
```

---

## 📖 Documentação Automática

Com a aplicação rodando, acesse:

| Interface | URL |
|-----------|-----|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

## ▶️ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/fastapi-livros.git
cd fastapi-livros
```

### 2. Criar e ativar o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Renomeie o arquivo `.env.example` para `.env` (se houver) ou edite o `.env` existente com suas configurações.

### 5. Executar a API

```bash
fastapi dev api/main.py
```

### 6. Executar o cliente de teste (opcional)

```bash
python client/cliente.py
```

---

## 🧠 Conceitos Aplicados

- API REST com FastAPI
- CRUD completo
- Arquitetura modular (routers / services / schemas / models)
- SQLModel + SQLite
- UUID como chave primária
- Paginação de resultados
- Validação de dados com Pydantic / Schemas
- Dependency Injection
- Tratamento de exceções HTTP
- Variáveis de ambiente com `.env`

---

## 🎯 Objetivo do Projeto

Projeto desenvolvido para praticar a criação de APIs modernas com FastAPI, aplicando boas práticas de organização de código, separação de responsabilidades e persistência de dados com SQLModel.

---

## 👨‍💻 Autor

**David Luiz Souza Nascimento**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-David%20Souza-blue?logo=linkedin)](https://www.linkedin.com/in/davisouza99)

Habilidades: Python · FastAPI · SQL · Git/GitHub