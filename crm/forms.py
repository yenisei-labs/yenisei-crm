import datetime
from django import forms
from django.utils.translation import gettext as _
from .models import DealList, Person


class DealListForm(forms.Form):
    title = forms.CharField(label=_('Title'), max_length=128)


class DealForm(forms.Form):
    # Required fields
    title = forms.CharField(label=_('Title *'), max_length=128)
    
    # Optional fields
    note = forms.CharField(
        label=_('Notes'),
        required=False,
        widget=forms.Textarea,
        empty_value=None,
    )
    goods = forms.CharField(
        label=_('Goods'),
        max_length=256,
        required=False, empty_value=None,
    )

    # Money
    income = forms.IntegerField(
        label=_('Income'),
        required=False,
    )
    goods_cost = forms.IntegerField(
        label=_('Goods cost'),
        required=False,
    )
    loading_cost = forms.IntegerField(
        label=_('Loading cost'),
        required=False,
    )
    delivery_cost = forms.IntegerField(
        label=_('Delivery cost'),
        required=False,
    )
    other_expenses = forms.IntegerField(
        label=_('Other expenses'),
        required=False,
    )
    tax = forms.IntegerField(
        label=_('Tax'),
        required=False,
    )

    # Delivery
    delivery_date = forms.DateTimeField(
        label=_('Delivery date'),
        required=False,
        initial=datetime.datetime.now,
        input_formats=['%H:%M %d.%m.%Y'],
        widget=forms.DateTimeInput(format='%H:%M %d.%m.%Y'),
    )
    delivery_address = forms.CharField(
        label=_('Delivery address'),
        max_length=256,
        required=False, empty_value=None,
    )
    loading_address = forms.CharField(
        label=_('Loading address'),
        max_length=256,
        required=False, empty_value=None,
    )

    buyer = forms.ModelChoiceField(
        Person.objects.all(),
        label=_('Buyer'),
        required=False,
    )
    list = forms.ModelChoiceField(
        DealList.objects.all(),
        label=_('List of deals'),
        required=False,
    )


class DealOrderForm(forms.Form):
    # Required fields
    list = forms.ModelChoiceField(DealList.objects.all())
    order = forms.IntegerField()
