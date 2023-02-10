import datetime
from django import forms
from .models import DealList, Person


class DealListForm(forms.Form):
    title = forms.CharField(label='Title', max_length=128)

class DealForm(forms.Form):
    # Required fields
    title = forms.CharField(max_length=128)
    
    # Optional fields
    note = forms.CharField(required=False, widget=forms.Textarea)
    goods = forms.CharField(max_length=256, required=False)

    # Money
    income = forms.IntegerField(required=False)
    goods_cost = forms.IntegerField(required=False)
    loading_cost = forms.IntegerField(required=False)
    delivery_cost = forms.IntegerField(required=False)
    other_expenses = forms.IntegerField(required=False)
    tax = forms.IntegerField(required=False)

    # Delivery
    delivery_date = forms.DateTimeField(required=False)
    delivery_address = forms.CharField(max_length=256, required=False)
    loading_address = forms.CharField(max_length=256, required=False)

    buyer = forms.ModelChoiceField(
        Person.objects.all(),
        required=False,
    )
    list = forms.ModelChoiceField(
        DealList.objects.all(),
        required=False,
    )
