from django import forms
from django.utils.translation import gettext as _
from .models import User


class LogInForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=100)
    password = forms.CharField(
        label=_('Password'),
        max_length=100,
        widget=forms.PasswordInput
    )
