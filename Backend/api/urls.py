from django.urls import path
from .views import ScanFoodView, FoodHistoryView

urlpatterns = [
    path('scan-food/', ScanFoodView.as_view(), name='scan-food'),
    path('food-history/', FoodHistoryView.as_view(), name='food-history'),
]