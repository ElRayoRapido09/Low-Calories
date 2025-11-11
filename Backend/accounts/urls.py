from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    # Agrega otras URLs según sea necesario
]