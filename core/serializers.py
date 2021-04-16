from rest_framework import serializers
from .models import Line, Order


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"



