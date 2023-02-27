import os
from pathlib import Path
from .env import is_production


def get_database():
    """Get database settings.

    In a dev environment, it's just a sqlite3 database.
    In a production server, settings are retrieved from environment variables.
    """
    if is_production():
        return {
            'ENGINE': os.environ.get('Y_CRM_DB_ENGINE', 'django.db.backends.postgresql'),
            'HOST': os.environ['Y_CRM_DB_HOST'],
            'NAME': os.environ.get('Y_CRM_DB_NAME', 'yenisei'),
            'USER': os.environ.get('Y_CRM_DB_USER', 'yenisei'),
            'PASSWORD': os.environ['Y_CRM_DB_PASSWORD'],
        }
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    return {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
