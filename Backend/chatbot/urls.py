from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_message, name='chat_message'),
    path('history/', views.get_conversation_history, name='conversation_history'),
    path('goals/', views.set_user_nutrition_goals, name='set_nutrition_goals'),
    path('calculate-calories/', views.calculate_calories, name='calculate_calories'),
    path('analyze-food/', views.analyze_food, name='analyze_food'),
    path('generate-meal-plan/', views.generate_meal_plan, name='generate_meal_plan'),
]