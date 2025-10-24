from django.urls import path
from .views import FoodSearchAPIView

urlpatterns = [
    path('food-search/', FoodSearchAPIView.as_view()),
]