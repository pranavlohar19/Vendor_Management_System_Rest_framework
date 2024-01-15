import string
import random
from django.db.models import Avg,F, ExpressionWrapper, fields
from .models import PurchaseOrder

def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))





# on time delivery rate function
def on_time_delivery_rate(vendor):
    delivered_ontime_count = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed', delivery_date__gte=F('issue_date')
    ).count()
    completed_count = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed'
    ).count()
    if completed_count > 0:
        on_time_delivery_rate = delivered_ontime_count / completed_count
        return on_time_delivery_rate
    return 0.0

# quality rating average function
def quality_rating_avg(vendor):
    quality_rating_avg = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed'
    ).aggregate(Avg('quality_rating'))['quality_rating__avg']
    print(quality_rating_avg)
    if quality_rating_avg:
        return quality_rating_avg
    return 0.0  
 
def average_response_time(vendor):
    response_times = PurchaseOrder.objects.filter(
        vendor=vendor, status='acknowledged'
    ).annotate(
        response_time=ExpressionWrapper(
            F('acknowledgment_date') - F('issue_date'),
            output_field=fields.DurationField()
        )
    ).aggregate(Avg('response_time'))['response_time__avg']
    average_response_time = response_times.total_seconds() / 3600 if response_times else 0.0
    return average_response_time
    
def fulfilment_rate(vendor):
    fulfilled_count = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed'
    ).count()
    total_count = PurchaseOrder.objects.filter(
        vendor=vendor
    ).count()
    if total_count > 0:
        fulfillment_rate = fulfilled_count / total_count
        return fulfillment_rate
    return 0.0
    