from rest_framework import serializers
from .models import Subscription, Location, PricePoint, FoodItem

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PricePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePoint
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'