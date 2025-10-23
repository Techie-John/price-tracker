from .views import PricePointViewSet, LocationViewSet, FoodItemViewSet, SubscriptionViewSet
from django.urls import path

urlpatterns = [
    path('pricetracker/', PricePointViewSet.as_view({'get': 'list'}), name='pricetracker-list'),
    path('locations/', LocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='location-list'),
    path('fooditems/', FoodItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='fooditem-list'),
    path('subscriptions/', SubscriptionViewSet.as_view({'get': 'list', 'post': 'create'}), name='subscription-list'),
]
