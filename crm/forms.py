from django import forms
from .models import DealList


class DealListForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
