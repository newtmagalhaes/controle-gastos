# Controle de Gastos

[![coverage_badge]][coverage_branch]

- - -

APP para registrar e analisar despesas

## Setup

```bash
# ambiente virtual com venv
python3 -m venv .venv

# ativar o ambiente no terminal (linux)
source .venv/bin/activate

# instalar dependências
pip install -r src/backend/requirements.txt

# aplicar migrações
python src/backend/manage.py migrate

# crie seu admin local
python src/backend/manage.py createsuperuser

# executar em modo de desenvolvimento
python src/backend/manage.py runserver
```
<!-- Links -->

[coverage_badge]: https://raw.githubusercontent.com/newtmagalhaes/controle-gastos/ci/actions/py-coverage/badge.svg
[coverage_branch]: https://github.com/newtmagalhaes/controle-gastos/tree/ci/actions/py-coverage
