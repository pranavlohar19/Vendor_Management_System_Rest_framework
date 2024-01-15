from .models import Vendor, HistoricalPerformance
from .utils import *
from django.utils import timezone


def calculate_historical_performance():
    vendors = Vendor.objects.all()
    for vendor in vendors:
        HistoricalPerformance.objects.create(
            vendor=vendor,
            date = timezone.now(),
            on_time_delivery_rate = vendor.on_time_delivery_rate,
            quality_rating_avg = vendor.quality_rating_avg,
            average_response_time = vendor.average_response_time,
            fulfillment_rate = vendor.fulfillment_rate
        )