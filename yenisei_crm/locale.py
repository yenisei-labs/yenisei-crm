import os
from django.utils.translation import gettext_lazy as _


def get_language_code() -> str:
    """Get the current locale code."""
    code = os.environ.get('Y_CRM_LOCALE', None)

    if code is not None:
        return code

    return 'en'


def get_languages() -> tuple:
    """Get a list of supported locales."""
    return (
        ('ru', _('Russian')),
        ('en', _('English')),
    )
