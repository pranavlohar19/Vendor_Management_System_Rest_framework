from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *
from .utils import random_string_generator
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = (IsAuthenticated,)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticated,)

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = (IsAuthenticated,)

