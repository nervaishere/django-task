from django.db.models import QuerySet


class OrderQuerySet(QuerySet):
    def by_customer(self, customer):
        return self

    def total_price(self):
        return self

    def total_price_by_customer(self, customer):
        return self

    def submitted_in_date(self, date_value):
        return self
