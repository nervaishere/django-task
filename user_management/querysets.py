from django.db.models import QuerySet


class CustomerQuerySet(QuerySet):
    def annotate_with_total_spending(self):
        return self

    def annotate_with_order_count(self):
        return self