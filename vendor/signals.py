from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Vendor, PurchaseOrder
import uuid

@receiver(pre_save, sender=Vendor)
def add_vendor_code(sender, instance, *args, **kwargs):
    if not instance.vendor_code:
        instance.vendor_code = str(uuid.uuid4())[:8]  

@receiver(pre_save, sender=PurchaseOrder)
def add_po_number(sender, instance, *args, **kwargs):
    if not instance.po_number:
        instance.po_number = str(uuid.uuid4())[:8]  
        
        
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, Count, Q, F, ExpressionWrapper, fields
from .models import PurchaseOrder, Vendor
from django.utils import timezone
from .utils import *

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, **kwargs):
    vendor = instance.vendor

    # On-Time Delivery Rate
    if instance.status == 'completed':
        vendor.on_time_delivery_rate = on_time_delivery_rate(vendor)

    # Quality Rating Average
    if instance.status == 'completed' and instance.quality_rating is not None:
        vendor.quality_rating_avg = quality_rating_avg(vendor)

    # Average Response Time
    if instance.status == 'acknowledged' and instance.acknowledgment_date is not None:
        vendor.average_response_time = average_response_time(vendor)
    # Fulfilment Rate
    vendor.fulfillment_rate = fulfilment_rate(vendor)
    
    vendor.save()