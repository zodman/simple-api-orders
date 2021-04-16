from test_plus.test import TestCase
from django_seed import Seed
from django.contrib.auth.models import User
from .models import Line, Order
from .serializers import LineSerializer, OrderSerializer


FOOD_LIST = [
            'Cheese Pizza', 'Hamburger', 'Cheeseburger', 'Bacon Burger', 'Bacon Cheeseburger',
            'Little Hamburger', 'Little Cheeseburger', 'Little Bacon Burger', 'Little Bacon Cheeseburger',
            'Veggie Sandwich', 'Cheese Veggie Sandwich', 'Grilled Cheese',
            'Cheese Dog', 'Bacon Dog', 'Bacon Cheese Dog', 'Pasta'
]


class InitMixin:
    @classmethod
    def setUpTestData(cls):
        seed = Seed.seeder()
        self.u1 = cls.make_user("u1")
        self.u2 = cls.make_user("u2")
        seed.add_entity(Line, 10)
        seed.add_entity(Order, 2, {'user': lambda x: User.objects.all().order_by("?")[0]})
        seed.execute()
        self.seed = seed


class TestFlow(InitMixin, TestCase):
    def test_serializer(self):
        orders = Order.objects.all()
        orders_ser = OrderSerializer(orders, many=True)
        self.assertTrue(orders_ser.data)

    def test_endpoint(self):
        self.get_check_200("/api/orders/")
        
        data = {
            'user': self.u1.id
            'lines': [
                {
                'product_name':     self.seed.faker.random_choice(FOOD_LIST, 1)
                }
            ]
        }
        assert False, data

        self.post("/api/orders/", data=data)


