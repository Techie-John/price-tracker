from django.shortcuts import render
from .models import Location, PricePoint, FoodItem, Subscription
from .serializers import LocationSerializer, PricePointSerializer, FoodItemSerializer, SubscriptionSerializer
from rest_framework import viewsets, permissions

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

class PricePointViewSet(viewsets.ModelViewSet):
    queryset = PricePoint.objects.all()
    serializer_class = PricePointSerializer
    permission_classes = [permissions.IsAuthenticated]

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# Create your views here.
