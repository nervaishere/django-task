from utils.sms import SMS
from .models import Manager
from product.models import Product
from order.models import Order
from celery import shared_task
from datetime import date


@shared_task()
def send_sms(self):
    todays_date = date.today()
    restocks = list(Product.objects.needs_restock().values_list('name', flat=True))
    total_sale = Order.objects.submitted_in_date(todays_date).total_price()
    msg = F"""{todays_date} 
                these products need to be restocked: {restocks}.
                today's total sale is: {total_sale}."""

    managers = Manager.objects.values_list('phone', flat=True)
    for manager in managers:
        SMS(manager, msg)
        SMS.send()
