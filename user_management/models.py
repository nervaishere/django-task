from django.db import models

from user_management.querysets import CustomerQuerySet


class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    objects = CustomerQuerySet.as_manager()

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username