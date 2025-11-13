from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/foods/', include('foods.urls')),
    path('api/chatbot/', include('chatbot.urls')),  # URLs del chatbot con IA
]
