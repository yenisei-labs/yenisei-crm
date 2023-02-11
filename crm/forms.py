import datetime
from django import forms
from .models import DealList, Person


class DealListForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=128)


class DealForm(forms.Form):
    # Required fields
    title = forms.CharField(label='Заголовок *', max_length=128)
    
    # Optional fields
    note = forms.CharField(
        label='Заметки',
        required=False,
        widget=forms.Textarea,
    )
    goods = forms.CharField(
        label='Товар',
        max_length=256,
        required=False,
    )

    # Money
    income = forms.IntegerField(label='Доход', required=False)
    goods_cost = forms.IntegerField(label='Стоимость товара', required=False)
    loading_cost = forms.IntegerField(label='Стоимость погрузки', required=False)
    delivery_cost = forms.IntegerField(label='Стоимость доставки', required=False)
    other_expenses = forms.IntegerField(label='Прочие расходы', required=False)
    tax = forms.IntegerField(label='Налог', required=False)

    # Delivery
    delivery_date = forms.DateTimeField(label='Дата доставки', required=False)
    delivery_address = forms.CharField(label='Адрес доставкик', max_length=256, required=False)
    loading_address = forms.CharField(label='Адрес погрузки', max_length=256, required=False)

    buyer = forms.ModelChoiceField(
        Person.objects.all(),
        label='Покупатель',
        required=False,
    )
    list = forms.ModelChoiceField(
        DealList.objects.all(),
        label='Список',
        required=False,
    )
