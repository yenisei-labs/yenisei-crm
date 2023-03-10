# Yenisei CRM

Just CRM, nothing more.

## Getting started

Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start dev server:
```bash
python manage.py migrate
python manage.py compilemessages
python manage.py runserver
```

## Environment variables

- `Y_CRM_ENV` - must be set to `production`, unless you are a developer.
- `Y_CRM_SECRET_KEY` - random and secret used in authentication.
- `Y_CRM_HOST` - your domain.
- `Y_CRM_LOCALE` - language code, possible values: `ru`, `en`.
- `Y_CRM_DB_ENGINE` - database engine ([django docs](https://docs.djangoproject.com/en/4.1/ref/databases/)). Default: `django.db.backends.postgresql` in production environment and `django.db.backends.sqlite3` in debug.
- `Y_CRM_DB_HOST` - database host.
- `Y_CRM_DB_NAME` - name of the database. Default: `yenisei`.
- `Y_CRM_DB_USER` - database user. Default: `yenisei`.
- `Y_CRM_DB_PASSWORD` - database password.

## Docker-compose
```yml
services:
  yenisei-crm-db:
    image: postgres
    environment:
      - POSTGRES_PASSWORD=secret-pass
      - POSTGRES_USER=yenisei
      - POSTGRES_DB=yenisei
    volumes:
      - crm-db:/var/lib/postgresql/data
    restart: unless-stopped

  yenisei-crm:
    image: ghcr.io/yenisei-labs/yenisei-crm
    environment:
      - Y_CRM_SECRET_KEY=another-secret-pass
      - Y_CRM_HOST=yenisei-crm.com
      - Y_CRM_DB_HOST=yenisei-crm-db
      - Y_CRM_DB_PASSWORD=secret-pass
      - Y_CRM_LOCALE=en
    depends_on:
      - yenisei-crm-db

volumes:
  crm-db:
```

## Linters
To run all configured linters, you can type the command:
```bash
make lint
```

## Icons

Icons were borrowed from [Font Awesome](https://fontawesome.com).
The [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/) applies to their svg files.
