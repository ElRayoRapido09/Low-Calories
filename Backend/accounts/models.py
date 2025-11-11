from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class Entrenamiento(models.TextChoices):
    MUY_ACTIVO = 'Muy activo', 'Muy activo'
    ACTIVO = 'Activo', 'Activo'
    MODERADO = 'Moderado', 'Moderado'
    SEDENTARIO = 'Sedentario', 'Sedentario'

class AccountManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo es obligatorio')
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)  # Hashea automáticamente
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo, password, **extra_fields)

# Create your models here.
class Account(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    peso = models.FloatField(models.DecimalField(("Peso"), max_digits=5, decimal_places=2))
    altura = models.FloatField(models.DecimalField(("Altura"), max_digits=5, decimal_places=2))
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    fech_cumpleanos = models.DateField()
    entrenamiento = models.CharField(
        max_length=20,
        choices=Entrenamiento.choices,
    )

    objects = AccountManager()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    # Sobrescribe save para hashear si es necesario
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre