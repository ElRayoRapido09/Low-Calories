from django.db import models
from accounts.models import Account


class Conversation(models.Model):
    """Modelo para guardar las conversaciones del chatbot"""
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=255, help_text="ID único de sesión para usuarios anónimos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        if self.user:
            return f"Conversación de {self.user.nombre} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
        return f"Conversación anónima {self.session_id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Message(models.Model):
    """Modelo para guardar los mensajes individuales"""
    SENDER_CHOICES = [
        ('user', 'Usuario'),
        ('bot', 'Bot'),
    ]
    
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"{self.get_sender_display()}: {self.content[:50]}..."


class UserContext(models.Model):
    """Modelo para guardar el contexto nutricional del usuario"""
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=255, null=True, blank=True, help_text="Para usuarios anónimos")
    
    # Objetivos nutricionales
    objetivo_calorias_diarias = models.IntegerField(null=True, blank=True, help_text="Calorías objetivo por día")
    objetivo_peso = models.FloatField(null=True, blank=True, help_text="Peso objetivo en kg")
    objetivo_tipo = models.CharField(max_length=20, choices=[
        ('perder', 'Perder peso'),
        ('mantener', 'Mantener peso'),
        ('ganar', 'Ganar peso'),
    ], null=True, blank=True)
    
    # Preferencias alimentarias
    restricciones_alimentarias = models.TextField(null=True, blank=True, help_text="Alergias, intolerancias, etc.")
    preferencias_dieta = models.CharField(max_length=30, choices=[
        ('normal', 'Normal'),
        ('vegetariana', 'Vegetariana'),
        ('vegana', 'Vegana'),
        ('keto', 'Cetogénica'),
        ('mediterranea', 'Mediterránea'),
    ], default='normal')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.user:
            return f"Contexto de {self.user.nombre}"
        return f"Contexto anónimo {self.session_id}"