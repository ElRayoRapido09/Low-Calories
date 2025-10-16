from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'nombre', 'apellido', 'peso', 'altura', 'correo', 'telefono', 'password', 'fech_cumpleanos', 'entrenamiento')