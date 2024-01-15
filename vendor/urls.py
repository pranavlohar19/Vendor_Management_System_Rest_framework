from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet, HistoricalPerformanceViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchaseorders', PurchaseOrderViewSet)
router.register(r'historicalperformances', HistoricalPerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]