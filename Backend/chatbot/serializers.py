from rest_framework import serializers
from .models import Conversation, Message, UserContext


class MessageSerializer(serializers.ModelSerializer):
    """Serializador para mensajes"""
    
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']


class ConversationSerializer(serializers.ModelSerializer):
    """Serializador para conversaciones"""
    messages = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Conversation
        fields = ['id', 'session_id', 'created_at', 'updated_at', 'messages']


class UserContextSerializer(serializers.ModelSerializer):
    """Serializador para contexto de usuario"""
    
    class Meta:
        model = UserContext
        fields = [
            'objetivo_calorias_diarias',
            'objetivo_peso', 
            'objetivo_tipo',
            'restricciones_alimentarias',
            'preferencias_dieta',
            'created_at',
            'updated_at'
        ]