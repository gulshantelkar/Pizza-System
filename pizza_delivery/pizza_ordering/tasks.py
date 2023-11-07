# tasks.py

from celery import shared_task,current_task
from django.utils import timezone
from .models import Order

import logging

@shared_task
def update_order_status(order_id):
    try:
        order = Order.objects.get(pk=order_id)
        now = timezone.now()
        time_difference = now - order.order_date
        logging.info(f"Updated order {order_id} time_difference{time_difference} ")

        if time_difference.total_seconds() < 60:
            order.status = 'Accepted'
        elif time_difference.total_seconds() < 180:
            order.status = 'Preparing'
        elif time_difference.total_seconds() < 300:
            order.status = 'Dispatched'
        elif time_difference.total_seconds() < 350:
            order.status = 'Delivered'
        else:
            return
        
        order.save()
        update_order_status.apply_async(args=(order.id,), countdown=30, expires=70)
    except Order.DoesNotExist:
        pass 
    

    logging.info(f"Updated order {order_id} status to {order.status}")

