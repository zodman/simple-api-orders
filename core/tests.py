from test_plus.test import TestCase
from django_seed import Seed
from django.contrib.auth.models import User
from .models import Line, Order
from .serializers import LineSerializer, OrderSerializer


class InitMixin:
    @classmethod
    def setUpTestData(cls):
        seed = Seed.seeder()
        cls.make_user("u1")
        cls.make_user("u2")
        seed.add_entity(Line, 10)
        seed.add_entity(Order, 2, {'user': lambda x: User.objects.all().order_by("?")[0]})
        seed.execute()


class TestFlow(InitMixin, TestCase):
    def test_serializer(self):
        orders = Order.objects.all()
        orders_ser = OrderSerializer(orders, many=True)
        self.assertTrue(orders_ser.data)

    def test_endpoint(self):
        self.get_check_200("/api/orders/")
