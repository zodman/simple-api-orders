from .serializers import LineSerializer, OrderSerializer
from .models import Order, Line
from rest_framework import viewsets



class LineViewSet(viewsets.ModelViewSet):
    serializer_class = LineSerializer

    def get_queryset(self):
        # TODO: filter by order
        queryset = Line.objects.all()
        return queryset


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer


    def get_queryset(self):
        qs = Order.objects.all()
        return qs
