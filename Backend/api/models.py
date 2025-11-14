from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class HistorialModel(models.Model):
    # Mapeo de la tabla SQL a un modelo de Django
    TIPO_COMIDA_CHOICES = [
        ('DESAYUNO', 'Desayuno'),
        ('ALMUERZO', 'Almuerzo'),
        ('CENA', 'Cena'),
        ('SNACK', 'Snack'),
    ]
    METODO_REGISTRO_CHOICES = [
        ('ESCANEADO', 'Escaneado'),
        ('MANUAL', 'Manual'),
        ('PLAN', 'Plan'),
    ]

    #Por el momento para al API
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null=True,  # ✅ Permitir NULL
        blank=True  # ✅ Permitir vacío en formularios
    )
    fecha = models.DateTimeField(auto_now_add=True)
    calorias = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    proteinas = models.FloatField(null=True, blank=True, help_text="Proteínas en gramos")
    carbohidratos = models.FloatField(null=True, blank=True, help_text="Carbohidratos en gramos")
    grasas = models.FloatField(null=True, blank=True, help_text="Grasas en gramos")
    img = models.ImageField(upload_to='historial_comidas/', max_length=500, null=True, blank=True)
    nombre_alimento = models.CharField(max_length=255)
    # Asumimos que no tienes un modelo Alimentos aún, así que usamos un campo de texto.
    # id_alimento = models.ForeignKey('Alimentos', on_delete=models.SET_NULL, null=True) 
    cantidad_consumida = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    tipo_comida = models.CharField(max_length=10, choices=TIPO_COMIDA_CHOICES, null=True, blank=True)
    metodo_registro = models.CharField(max_length=10, choices=METODO_REGISTRO_CHOICES)

    class Meta:
        db_table = 'historial'
        ordering = ['-fecha']
        verbose_name = 'Historial de Comida'
        verbose_name_plural = 'Historial de Comidas'

    def __str__(self):
        return f"{self.user.username} - {self.nombre_alimento} ({self.fecha.strftime('%Y-%m-%d')})"
