from django.db import models
from order.enums import OrderStatus
from order.querysets import OrderQuerySet
from django.db.models import Sum, F


class Order(models.Model):
    customer = models.ForeignKey('user_management.Customer', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default=OrderStatus.PENDING, choices=OrderStatus.choices)
    total_price = models.FloatField(default=0)

    objects = OrderQuerySet.as_manager()

    def calculate_total_price(self):
        product_price = round(list(self.orderitem_set.aggregate(total=Sum(F('quantity')*F('product__price'))).values())[0],2)
        return product_price

    def accept(self):
        self.status = OrderStatus.ACCEPTED
        self.save()

    def reject(self):
        self.status = OrderStatus.REJECTED
        self.save()

    def deliver(self):
        self.status = OrderStatus.DELIVERED
        self.save()

    def cancel(self):
        self.status = OrderStatus.CANCELLED
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.order.customer.user.username} - {self.product.name}'

    def save(self, *args, **kwargs):
        """You can not modify this method"""
        super().save(*args, **kwargs)
        self.order.total_price = self.order.calculate_total_price()
        self.order.save()

