from django.db.models import QuerySet, Count, Sum


class CustomerQuerySet(QuerySet):
    def annotate_with_total_spending(self):
        total_sp = self.annotate(total_spending=Sum('order__total_price'))
        return total_sp

    def annotate_with_order_count(self):
        orders_num = self.annotate(order_count=Count('order'))
        return orders_num
