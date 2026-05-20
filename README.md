# Django + UV

Projeto Django utilizando:

- Python
- Django
- UV
- Estrutura `src/`

---

# Requisitos

Antes de começar instale:

- Git
- Python 3.12+
- UV

---

# Instalar Python

Download oficial:

- https://www.python.org/downloads/

Verifique instalação:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

# Instalar UV

Documentação oficial:

- https://docs.astral.sh/uv/

---

## Linux/macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Windows (PowerShell)

```powershell id="k6t91d"
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

# Clonar o projeto

```bash
git clone URL_DO_REPOSITORIO
```

Entrar na pasta:

```bash
cd NOME_DO_PROJETO
```

---

# Estrutura do projeto

```text
projeto/
├── src/
│   ├── apps/
│   ├── config/
│   ├── templates/
│   └── static/
│
├── manage.py
├── pyproject.toml
├── uv.lock
└── .gitignore
```

---

# Criar ambiente virtual

```bash
uv venv
```

Isso cria:

```text
.venv/
```

---

# Ativar ambiente virtual

## Linux/macOS

```bash
source .venv/bin/activate
```

---

## Windows

```powershell id="2icowd"
.venv\Scripts\activate
```

---

# Instalar dependências

```bash
uv sync
```

O UV irá instalar automaticamente todas as dependências do projeto usando:

```text
pyproject.toml
uv.lock
```

---

# Rodar migrations

```bash
uv run manage.py migrate
```

---

# Executar servidor Django

```bash
uv run manage.py runserver
```

---

# Abrir projeto

Acesse:

```text
http://127.0.0.1:8000
```

---

# Criar super usuário

```bash
uv run manage.py createsuperuser
```

Painel admin:

```text
http://127.0.0.1:8000/admin/
```

---

# Comandos úteis

## Rodar servidor

```bash
uv run manage.py runserver
```

---

## Criar migrations

```bash
uv run manage.py makemigrations
```

---

## Aplicar migrations

```bash
uv run manage.py migrate
```

---

## Criar app

```bash
uv run manage.py startapp nome_app
```

---

# Estrutura Recomendada

```text
src/
├── apps/
├── config/
├── templates/
└── static/
```

---

# Git Ignore

O projeto já possui `.gitignore` configurado para ignorar:

- ambiente virtual
- cache Python
- variáveis de ambiente
- SQLite
- arquivos temporários

---

# Tecnologias

- Python
- Django
- UV

---

# Links úteis

- Django: https://www.djangoproject.com/
- Django Docs: https://docs.djangoproject.com/
- UV Docs: https://docs.astral.sh/uv/