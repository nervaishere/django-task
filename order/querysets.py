from django.db.models import QuerySet
from django.db.models import Sum


class OrderQuerySet(QuerySet):
    def by_customer(self, customer):
        return self.filter(customer=customer)

    def total_price(self):
        return self.aggregate(tp=Sum('total_price')).get('tp')

    def total_price_by_customer(self, customer):
        query = self.filter(customer=customer).aggregate(tp=Sum('total_price')).get('tp')
        return query

    def submitted_in_date(self, date_value):
        return self.filter(date=date_value)
