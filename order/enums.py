from django.db.models import TextChoices


class OrderStatus(TextChoices):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'