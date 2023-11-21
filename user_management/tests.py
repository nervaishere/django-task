from django.test import TestCase

from user_management.models import Customer


class TestOrder(TestCase):
    fixtures = ['user_management/fixtures/user_management.json', 'product/fixtures/product.json', 'order/fixtures/order.json']

    def test_annotate_with_total_spending(self):
        customers = list(Customer.objects.annotate_with_total_spending().values('id', 'total_spending'))
        self.assertEqual(customers, [{'id': 1, 'total_spending': 123.92}, {'id': 2, 'total_spending': None}])

    def test_annotate_with_order_count(self):
        customers = list(Customer.objects.annotate_with_order_count().values('id', 'order_count'))
        self.assertEqual(customers, [{'id': 1, 'order_count': 2}, {'id': 2, 'order_count': 0}])