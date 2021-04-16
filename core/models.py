from django.db import models
from django.contrib.auth.models import User
# signals
from .signals import create_auth_token 


class Line(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lines = models.ManyToManyField(Line)
