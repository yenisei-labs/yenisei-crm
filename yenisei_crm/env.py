import os

def is_production() -> bool:
    environment = os.environ.get('Y_CRM_ENV', 'debug')
    return environment == 'production'
