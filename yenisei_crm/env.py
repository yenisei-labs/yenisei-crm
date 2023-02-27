import os

def is_production() -> bool:
    """Find out if the current environment is production."""
    environment = os.environ.get('Y_CRM_ENV', 'debug')
    return environment == 'production'
