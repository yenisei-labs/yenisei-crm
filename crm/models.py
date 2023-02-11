from django.db import models


class Person(models.Model):
    # Required fields
    first_name = models.CharField(max_length=32)

    # Optional fields
    last_name = models.CharField(max_length=32, null=True, default=None)
    company = models.CharField(max_length=64, null=True, default=None)
    email = models.EmailField(null=True, default=None)
    phone = models.CharField(max_length=20, null=True, default=None)
    delivery_address = models.CharField(max_length=256, null=True, default=None)

    def __str__(self):
        return self.first_name


class DealList(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Deal(models.Model):
    # Required fields
    title = models.CharField(max_length=128)
    
    # Optional fields
    note = models.TextField(null=True, default=None)
    goods = models.CharField(max_length=256, null=True, default=None)

    # Money
    income = models.PositiveIntegerField(
        null=True, default=None,
        help_text="The total amount to be paid by the buyer",
    )
    goods_cost = models.PositiveIntegerField(
        null=True, default=None,
        help_text="The cost of goods (not including shipping)",
    )
    loading_cost = models.PositiveIntegerField(
        null=True, default=None,
        help_text="The cost of transferring the goods to delivery",
    )
    delivery_cost = models.PositiveIntegerField(null=True, default=None)
    other_expenses = models.IntegerField(
        null=True, default=None,
        help_text="Other expenses (not including the cost of goods and delivery)",
    )
    tax = models.PositiveIntegerField(
        null=True, default=None,
        help_text="The amount of money to be paid in taxes",
    )

    # Delivery
    delivery_date = models.DateTimeField(null=True, default=None)
    delivery_address = models.CharField(max_length=256, null=True, default=None)
    loading_address = models.CharField(
        max_length=256,
        null=True, default=None,
        help_text="The place where the product will be handed over for delivery",
    )

    buyer = models.ForeignKey(
        Person,
        related_name='purchases',
        null=True, default=None,
        on_delete=models.SET_NULL,
    )
    list = models.ForeignKey(
        DealList,
        related_name='deals',
        null=True, default=None,
        on_delete=models.SET_NULL,
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
