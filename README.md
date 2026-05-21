# 🧬 Sistema de Busca e Persistência de Proteínas — Integração com RCSB Protein Data Bank

Este projeto foi desenvolvido utilizando [Django](https://www.djangoproject.com/?utm_source=chatgpt.com) e integração com a API oficial do [RCSB Protein Data Bank (PDB)](https://www.rcsb.org/?utm_source=chatgpt.com).

A proposta do sistema é permitir que usuários realizem buscas científicas de proteínas diretamente no RCSB, visualizem detalhes estruturais, exportem arquivos `.pdb` e mantenham um histórico persistido de pesquisas e estruturas salvas localmente.

O projeto também serve como base educacional para aprendizado de:

* Django
* Arquitetura MVC/MVT
* Consumo de APIs REST
* Persistência de dados
* Modelagem relacional
* Templates HTML
* Paginação
* Integração científica com bioinformática

---

# 🚀 Tecnologias utilizadas

* Python 3.12
* Django 6
* SQLite
* HTML/CSS
* JavaScript
* UV (gerenciador de ambiente Python)
* API REST do RCSB

---

# 📁 Estrutura do projeto

```text
src/
├── apps/
│   ├── core/
│   └── users/
│
├── templates/
│   ├── core/
│   └── users/
│
├── config/
│
manage.py
pyproject.toml
uv.lock
```

---

# ⚙️ Como executar o projeto localmente

## 1. Instalar o UV

O projeto utiliza o [UV](https://github.com/astral-sh/uv?utm_source=chatgpt.com) como gerenciador de dependências e ambiente virtual.

### Linux / WSL

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Verificar instalação

```bash
uv --version
```

---

# 2. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

Entrar na pasta:

```bash
cd nome-do-projeto
```

---

# 3. Instalar dependências

```bash
uv sync
```

---

# 4. Aplicar migrations

```bash
uv run manage.py migrate
```

---

# 5. Criar super usuário

```bash
uv run manage.py createsuperuser
```

---

# 6. Executar o servidor

```bash
uv run manage.py runserver
```

---

# 🌐 Acessando a aplicação

Após iniciar o servidor:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Fluxo da aplicação

A aplicação possui autenticação de usuários.

Fluxo principal:

```text
Home
    ↓
Cadastro
    ↓
Login
    ↓
Dashboard científico
    ↓
Busca de proteínas
    ↓
Persistência local
    ↓
Histórico de buscas
```

---

# 👤 Cadastro de usuário

Endpoint:

```text
/users/
```

O usuário pode:

* criar conta
* acessar login
* navegar pelo sistema autenticado

Os dados são persistidos no banco SQLite utilizando o sistema nativo de autenticação do Django.

---

# 🔑 Login

Endpoint:

```text
/login/
```

Funcionalidades:

* autenticação
* logout
* redirecionamento seguro
* proteção de rotas com `login_required`

---

# 🧬 Dashboard de busca de proteínas

Endpoint:

```text
/dashboard/
```

Esta é a principal funcionalidade do projeto.

O dashboard permite:

✅ buscar proteínas no RCSB

✅ visualizar detalhes científicos

✅ abrir estrutura diretamente no site oficial

✅ exportar arquivos `.pdb`

✅ salvar resultados localmente

✅ paginação de resultados

✅ feedback visual de exportação

---

# 🔎 Busca de proteínas

Ao realizar uma busca:

```text
Hemoglobin
```

o sistema envia uma requisição REST para:

```text
https://search.rcsb.org/
```

Os resultados retornam:

* protein_id
* score
* URLs da estrutura
* metadados científicos

---

# 📖 Detalhamento científico

Ao clicar em:

```text
Descrição
```

o sistema busca dinamicamente:

* título completo da proteína
* classificação
* organismo
* sistema de expressão

Esses dados são persistidos localmente no banco.

---

# 💾 Exportação de arquivos PDB

Ao clicar em:

```text
Exportar PDB
```

o sistema:

```text
RCSB
    ↓
download do .pdb
    ↓
persistência no banco
```

O conteúdo completo do `.pdb` é salvo no SQLite.

---

# 📚 Histórico de buscas

Endpoint:

```text
/dashboard/proteins/
```

A página de histórico permite:

✅ visualizar proteínas persistidas

✅ visualizar descrições científicas

✅ visualizar buscas realizadas

✅ verificar status do PDB salvo

✅ exportar novamente

✅ pesquisar histórico completo

---

# 🔎 Busca inteligente no histórico

O filtro da página busca por:

* protein_id
* texto pesquisado
* descrição científica (`full_title`)

Exemplo:

```text
hemoglobin
```

ou:

```text
6G11
```

ou:

```text
Magnaporthe
```

---

# 🗃️ Persistência local

O sistema persiste:

## ProteinSearch

Histórico das buscas realizadas.

---

## Protein

Informações básicas da proteína.

---

## ProteinDetail

Detalhamento científico completo.

---

## ProteinPDBFile

Conteúdo integral do arquivo `.pdb`.

---

# 🧠 Arquitetura utilizada

O projeto segue o padrão MVT do Django:

```text
Model
View
Template
```

Também foi aplicada separação de responsabilidades:

```text
views.py
    ↓
services.py
    ↓
API externa / banco
```

A lógica de integração com o RCSB foi centralizada em `services.py`.

---

# 🔗 Principais endpoints

| Endpoint                         | Descrição            |
| -------------------------------- | -------------------- |
| `/`                              | Home                 |
| `/users/`                        | Cadastro             |
| `/login/`                        | Login                |
| `/dashboard/`                    | Dashboard principal  |
| `/dashboard/proteins/`           | Histórico de buscas  |
| `/protein-details/<protein_id>/` | Detalhamento via API |
| `/export/<protein_id>/`          | Exportação do PDB    |

---

# 🎯 Objetivos educacionais do projeto

Este projeto foi construído com foco em aprendizado prático de:

* Django
* APIs REST
* Persistência de dados
* Paginação
* Modelagem relacional
* Frontend básico
* Integração científica
* Arquitetura web

---

# 📌 Possíveis melhorias futuras

* Docker
* PostgreSQL
* Celery
* Cache Redis
* Download real do `.pdb`
* Visualização 3D molecular
* Busca avançada
* Testes automatizados
* Deploy em nuvem
* API própria com Django REST Framework

---

# 👨‍💻 Considerações finais

O sistema demonstra uma integração completa entre:

* backend Django
* persistência local
* autenticação
* APIs científicas externas
* renderização dinâmica
* experiência visual moderna

Além do aspecto educacional, o projeto já apresenta uma estrutura sólida para evolução futura em aplicações científicas reais.

---

Na pasta `validation_database` temos um script de listagem das tabelas e `SELECT` para validação dos valores. Seguem anexos também três csv de exemplos.