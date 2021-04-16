from django.db import models
from django.contrib.auth.models import User
# signals
from .signals import create_auth_token


class Line(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Line {self.id}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lines = models.ManyToManyField(Line, through="Row")

    def __str__(self):
        return f'Order {self.id}'


class Row(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'Row {self.id}'
