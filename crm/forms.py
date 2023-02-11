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
        empty_value=None,
    )
    goods = forms.CharField(
        label='Товар',
        max_length=256,
        required=False, empty_value=None,
    )

    # Money
    income = forms.IntegerField(
        label='Доход',
        required=False,
    )
    goods_cost = forms.IntegerField(
        label='Стоимость товара',
        required=False,
    )
    loading_cost = forms.IntegerField(
        label='Стоимость погрузки',
        required=False,
    )
    delivery_cost = forms.IntegerField(
        label='Стоимость доставки',
        required=False,
    )
    other_expenses = forms.IntegerField(
        label='Прочие расходы',
        required=False,
    )
    tax = forms.IntegerField(
        label='Налог',
        required=False,
    )

    # Delivery
    delivery_date = forms.DateTimeField(
        label='Дата доставки',
        required=False,
        initial=datetime.datetime.now,
        input_formats=['%H:%M %d.%m.%Y'],
        widget=forms.DateTimeInput(format='%H:%M %d.%m.%Y'),
    )
    delivery_address = forms.CharField(
        label='Адрес доставкик',
        max_length=256,
        required=False, empty_value=None,
    )
    loading_address = forms.CharField(
        label='Адрес погрузки',
        max_length=256,
        required=False, empty_value=None,
    )

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


class DealOrderForm(forms.Form):
    # Required fields
    list = forms.ModelChoiceField(DealList.objects.all())
    order = forms.IntegerField()
