from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db import models as m
from .models import Row
from .models import Order, Line
from .serializers import LineSerializer, OrderSerializer



class LinesViewSet(viewsets.ModelViewSet):
    serializer_class = LineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Line.objects.all()
        return queryset


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Order.objects.all()
        return qs


class ReportView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        s = (Row.objects.all()
             # filters
            .select_related("line")
            .extra(select={'total':'core_line.price*core_line.quantity'})
            .values("line__product_name", 'line__price', 'line__quantity','total')
        )


        
