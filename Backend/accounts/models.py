from django.db import models

class Entrenamiento(models.TextChoices):
    MUY_ACTIVO = 'Muy activo', 'Muy activo'
    ACTIVO = 'Activo', 'Activo'
    MODERADO = 'Moderado', 'Moderado'
    SEDENTARIO = 'Sedentario', 'Sedentario'

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

    def __str__(self):
        return self.nombre