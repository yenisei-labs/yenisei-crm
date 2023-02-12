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
python manage.py runserver
```

## Environment variables

- `Y_CRM_ENV` - must be set to `production`, unless you are a developer.
- `Y_CRM_SECRET_KEY` - random and secret used in authentication.
- `Y_CRM_HOST` - your domain.

- `Y_CRM_DB_ENGINE` - database engine ([django docs](https://docs.djangoproject.com/en/4.1/ref/databases/)). Default: `django.db.backends.postgresql` in production environment and `django.db.backends.sqlite3` in debug.
- `Y_CRM_DB_HOST` - database host.
- `Y_CRM_DB_NAME` - name of the database. Default: `yenisei`.
- `Y_CRM_DB_USER` - database user. Default: `yenisei`.
- `Y_CRM_DB_PASSWORD` - database password.
