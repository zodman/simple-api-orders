from .serializers import LineSerializer, OrderSerializer
from .models import Order, Line
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



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

class ReportViewSet(viewsets.GenericViewSet):
    pass

