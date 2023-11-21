from django.test import TestCase

from order.models import Order, OrderItem
from user_management.models import Customer


class TestOrder(TestCase):
    fixtures = ['user_management/fixtures/user_management.json', 'product/fixtures/product.json', 'order/fixtures/order.json']

    def test_total_price(self):
        order = Order.objects.get(pk=1)
        self.assertEqual(order.total_price, 61.96)

        OrderItem.objects.create(order=order, product_id=1, quantity=1)
        order.refresh_from_db()
        self.assertEqual(order.total_price, 72.95)


class TestOrderQueryset(TestCase):
    fixtures = ['user_management/fixtures/user_management.json', 'product/fixtures/product.json', 'order/fixtures/order.json']

    def test_total_price(self):
        total_price = Order.objects.total_price()
        self.assertEqual(total_price, 123.92)

    def test_total_price_by_customer(self):
        customer = Customer.objects.get(id=1)
        total_price = Order.objects.total_price_by_customer(customer)
        self.assertEqual(total_price, 123.92)

    def test_submitted_in_date(self):
        orders_list = list(Order.objects.submitted_in_date('2022-01-01').values_list('id', flat=True))
        self.assertEqual(orders_list, [1])

        non_existent_date = list(Order.objects.submitted_in_date('2022-01-02').values_list('id', flat=True))
        self.assertEqual(non_existent_date, [])
