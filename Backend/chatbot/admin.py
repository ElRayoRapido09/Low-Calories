from django.contrib import admin
from .models import Conversation, Message, UserContext


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'session_id', 'created_at', 'message_count']
    list_filter = ['created_at', 'user']
    search_fields = ['session_id', 'user__nombre', 'user__correo']
    readonly_fields = ['created_at', 'updated_at']
    
    def message_count(self, obj):
        return obj.messages.count()
    message_count.short_description = 'Número de mensajes'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'conversation', 'sender', 'content_preview', 'timestamp']
    list_filter = ['sender', 'timestamp']
    search_fields = ['content', 'conversation__session_id']
    readonly_fields = ['timestamp']
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Vista previa del mensaje'


@admin.register(UserContext)
class UserContextAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'session_id', 'objetivo_tipo', 'objetivo_calorias_diarias', 'preferencias_dieta']
    list_filter = ['objetivo_tipo', 'preferencias_dieta', 'created_at']
    search_fields = ['user__nombre', 'session_id']
    readonly_fields = ['created_at', 'updated_at']