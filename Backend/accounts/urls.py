from django.urls import path
from accounts.views import AccountListAPIView

urlpatterns = [
    path('accounts/', AccountListAPIView.as_view())
]