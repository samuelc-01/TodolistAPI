
# TodolistAPI 📝

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/seu-usuario/TodolistAPI/actions)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Coverage Status](https://img.shields.io/badge/coverage-85%25-yellowgreen)](https://github.com/seu-usuario/TodolistAPI)
[![Made with Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)

---

## Descrição

TodolistAPI é uma API RESTful simples e eficiente para gerenciamento de listas de tarefas (To-Do lists).  
Projetada para ser leve, escalável e fácil de integrar em sistemas existentes, com foco em segurança e boas práticas.

---

## Funcionalidades principais

- CRUD completo para tarefas: criação, leitura, atualização e remoção
- Suporte a autenticação JWT para proteção das rotas
- Filtros por status, prioridade e datas
- Paginação e ordenação de resultados
- Documentação interativa via Swagger / OpenAPI
- Validação e tratamento de erros consistente
- Estrutura modular para fácil manutenção e extensibilidade

---

## Tecnologias utilizadas

| Tecnologia       | Versão   | Link                         |
|------------------|----------|------------------------------|
| Python           | 3.10+    | [python.org](https://python.org) |
| FastAPI          | 0.95+    | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| SQLAlchemy       | 1.4+     | [sqlalchemy.org](https://www.sqlalchemy.org) |
| PostgreSQL       | 14+      | [postgresql.org](https://www.postgresql.org) |
| Docker           | 23+      | [docker.com](https://www.docker.com) |
| Pytest           | 7+       | [pytest.org](https://docs.pytest.org) |

---

## Como usar

### Pré-requisitos

- Python 3.10+
- Docker (opcional, mas recomendado)
- PostgreSQL instalado ou container rodando

### Instalação local

```bash
git clone https://github.com/seu-usuario/TodolistAPI.git
cd TodolistAPI
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
