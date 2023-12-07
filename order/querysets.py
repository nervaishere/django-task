from django.db.models import QuerySet
from django.db.models import *


class OrderQuerySet(QuerySet):
    def by_customer(self, customer):
        return self.filter(customer=customer)

    def total_price(self):
        price = list(map(float, self.values_list('total_price', flat=True)))
        return sum(price)

    def total_price_by_customer(self, customer):
        price = list(map(float, self.filter(customer=customer).values_list('total_price', flat=True)))
        return sum(price)

    def submitted_in_date(self, date_value):
        return self.filter(date=date_value)
