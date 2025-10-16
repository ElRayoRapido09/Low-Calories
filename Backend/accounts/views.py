from django.shortcuts import render
from rest_framework import generics
from accounts.models import Account
from accounts.serializers import AccountSerializer

# Create your views here.


class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer