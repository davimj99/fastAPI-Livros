# 📚 FastAPI Curso - API de Livros

Projeto desenvolvido durante os estudos de FastAPI, com foco na criação de APIs REST modernas utilizando Python, FastAPI e SQLModel.

## 🚀 Tecnologias Utilizadas

- Python 3.13
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Pydantic
- UUID

---

## 📂 Estrutura do Projeto

```bash
FASTAPICURSO/
│
├── api/
│   ├── routers/
│   │   └── livros_router.py
│   │
│   ├── database.py
│   ├── main.py
│   └── models.py
│
├── client/
│   ├── __init__.py
│   └── cliente.py
│
├── database.db
├── livros.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Funcionalidades

### Livros

- ✅ Listar livros
- ✅ Buscar livro por ID
- ✅ Cadastrar livro
- ✅ Atualizar livro completo (PUT)
- ✅ Atualizar livro parcialmente (PATCH)
- ✅ Excluir livro
- ✅ Paginação de resultados

---

## 🔗 Endpoints

### Listar Livros

```http
GET /livros
```

Parâmetros:

```http
?page=1
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

Exemplo:

```json
{
  "autor": "Machado de Assis",
  "titulo": "Dom Casmurro",
  "editora": "Ática",
  "ano": 1899
}
```

---

### Atualizar Livro

```http
PUT /livros/{livro_id}
```

Exemplo:

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

Exemplo:

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

O projeto utiliza SQLite para persistência dos dados.

Arquivo:

```bash
database.db
```

Modelagem principal:

```python
Livro
├── uuid
├── autor
├── titulo
├── editora
└── ano
```

---

## 📖 Documentação Automática

Após iniciar a aplicação:

### Swagger UI

```bash
http://localhost:8000/docs
```

### ReDoc

```bash
http://localhost:8000/redoc
```

---

## ▶️ Como Executar

### 1 - Clonar o projeto

```bash
git clone https://github.com/seu-usuario/fastapi-curso.git
```

### 2 - Entrar na pasta

```bash
cd fastapi-curso
```

### 3 - Criar ambiente virtual

Windows:

```bash
python -m venv venv
```

### 4 - Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 5 - Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 6 - Executar a API

```bash
uvicorn api.main:app --reload
```

Saída esperada:

```bash
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## 🧠 Conceitos Aplicados

- API REST
- CRUD
- FastAPI
- SQLModel
- SQLite
- UUID
- Paginação
- Validação de Dados
- Dependency Injection
- Pydantic
- Tratamento de Exceções HTTP
- Arquitetura Modular

---

## 🎯 Objetivo do Projeto

Projeto desenvolvido para praticar a criação de APIs modernas com FastAPI, aplicando conceitos fundamentais de desenvolvimento backend, persistência de dados e boas práticas de organização de código.

---

## 👨‍💻 Autor

**David Luiz Souza Nascimento**

- Python
- FastAPI
- SQL
- Git/GitHub

LinkedIn:
www.linkedin.com/in/davisouza99
