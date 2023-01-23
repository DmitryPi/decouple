from django.conf import settings
from django.db import models


class Invoice(models.Model):
    class State(models.TextChoices):
        PAID = "PAID"
        UNPAID = "UNPAID"
        CANCELLED = "CANCELLED"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date = models.DateTimeField()
    due_date = models.DateTimeField()
    state = models.CharField(max_length=15, choices=State.choices, default=State.UNPAID)


class ItemLine(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    taxed = models.BooleanField()
