import os
from .env import is_production


def get_secret_key() -> str:
    if is_production():
        return os.environ['Y_CRM_SECRET_KEY']
    return 'django-insecure-z@5mw=u+k6#!xk1!-$2dn9f9n_7hsrg4h&rmw$pqbmol10tsgg'
