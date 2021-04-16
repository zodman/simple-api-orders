from test_plus.test import APITestCase as TestCase
from django_seed import Seed
from django.contrib.auth.models import User
from django.db import models as m
from .models import Line, Order
from .serializers import LineSerializer, OrderSerializer
from .models import Row

FOOD_LIST = [
    'Cheese Pizza', 'Hamburger', 'Cheeseburger', 'Bacon Burger',
    'Bacon Cheeseburger', 'Little Hamburger', 'Little Cheeseburger',
    'Little Bacon Burger', 'Little Bacon Cheeseburger', 'Veggie Sandwich',
    'Cheese Veggie Sandwich', 'Grilled Cheese', 'Cheese Dog', 'Bacon Dog',
    'Bacon Cheese Dog', 'Pasta'
]


class InitMixin:
    def setUp(self):
        seed = Seed.seeder()
        self.u1 = self.make_user("u1")
        self.u2 = self.make_user("u2")
        seed.add_entity(
            Line, 10, {
                'product_name': lambda x: seed.faker.random_element(FOOD_LIST),
            })
        seed.add_entity(
            Order, 2, {'user': lambda x: User.objects.all().order_by("?")[0]})
        seed.execute()
        for i in Order.objects.all():
            lines = Line.objects.all().values_list('id', flat=True)
            i.lines.add(*lines)
        self.seed = seed


class TestFlow(InitMixin, TestCase):
    def test_check_token(self):
        self.assertTrue(self.u1.auth_token)

    def test_serializer(self):
        orders = Order.objects.all()
        orders_ser = OrderSerializer(orders, many=True)
        self.assertTrue(orders_ser.data)

    def test_auth(self):
        resp = self.get("/api/orders/")
        self.response_403(resp)

    def test_endpoint(self):
        with self.login(username="u1"):
            self.get_check_200("/api/orders/")
            faker = self.seed.faker
            line_data = {
                'product_name':
                faker.random_element(FOOD_LIST),
                'price':
                faker.pydecimal(min_value=1, max_value=100, right_digits=2),
                'quantity':
                faker.pyint(min_value=1, max_value=20)
            }
            resp = self.post("/api/lines/",
                             data=line_data,
                             extra={'format': 'json'})
            self.response_201(resp)
            result = resp.data
            data = {'user': self.u1.id, 'lines': [result.get("id")]}
            self.post("/api/orders/", data=data)
            self.response_201()

    def test_aggregate(self):
        s = (Row.objects.all()
             # filters
            .select_related("line")
            .extra(select={'total':'core_line.price*core_line.quantity'})
            .values("line__product_name", 'line__price', 'line__quantity','total')
        )
        self.assertTrue('total' in s[0])
