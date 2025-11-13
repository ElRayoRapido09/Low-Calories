from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import json
import uuid
from datetime import datetime, timedelta
from accounts.models import Account
from .models import Conversation, Message, UserContext
from .gemini_service import GeminiService
from .serializers import MessageSerializer, ConversationSerializer


@csrf_exempt
@require_http_methods(["POST"])
def chat_message(request):
    """Endpoint principal para enviar mensajes al chatbot"""
    
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id')
        user_id = data.get('user_id')  # Opcional, para usuarios autenticados
        
        if not user_message:
            return JsonResponse({'error': 'Mensaje vacío'}, status=400)
        
        # Generar session_id si no existe
        if not session_id:
            session_id = str(uuid.uuid4())
        
        # Obtener o crear conversación
        conversation = get_or_create_conversation(user_id, session_id)
        
        # Guardar mensaje del usuario
        user_msg = Message.objects.create(
            conversation=conversation,
            sender='user',
            content=user_message
        )
        
        # Obtener datos del usuario si está autenticado
        user_data = None
        user_context = None
        
        if user_id:
            try:
                user = Account.objects.get(id=user_id)
                user_data = {
                    'peso': user.peso,
                    'altura': user.altura,
                    'entrenamiento': user.entrenamiento,
                    'edad': calculate_age(user.fech_cumpleanos)
                }
                user_context = UserContext.objects.filter(user=user).first()
            except Account.DoesNotExist:
                pass
        else:
            # Para usuarios anónimos, intentar obtener contexto por session_id
            user_context = UserContext.objects.filter(session_id=session_id).first()
        
        # Obtener historial de conversación
        conversation_history = list(conversation.messages.order_by('timestamp').values(
            'sender', 'content', 'timestamp'
        ))
        
        # Limitar a los últimos 10 mensajes
        if len(conversation_history) > 10:
            conversation_history = conversation_history[len(conversation_history)-10:]
        
        # Generar respuesta con Gemini AI
        gemini_service = GeminiService()
        bot_response = gemini_service.generate_response(
            user_message=user_message,
            conversation_history=conversation_history,
            user_data=user_data,
            user_context=user_context
        )
        
        # Guardar respuesta del bot
        bot_msg = Message.objects.create(
            conversation=conversation,
            sender='bot',
            content=bot_response
        )
        
        return JsonResponse({
            'success': True,
            'session_id': session_id,
            'user_message': {
                'id': user_msg.id,
                'content': user_msg.content,
                'timestamp': user_msg.timestamp.isoformat(),
                'sender': 'user'
            },
            'bot_response': {
                'id': bot_msg.id,
                'content': bot_msg.content,
                'timestamp': bot_msg.timestamp.isoformat(),
                'sender': 'bot'
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error interno: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["GET"])
def get_conversation_history(request):
    """Obtener historial de conversación"""
    
    session_id = request.GET.get('session_id')
    user_id = request.GET.get('user_id')
    
    if not session_id and not user_id:
        return JsonResponse({'error': 'Se requiere session_id o user_id'}, status=400)
    
    try:
        # Buscar conversación
        conversation = None
        
        if user_id:
            conversation = Conversation.objects.filter(
                user_id=user_id
            ).order_by('-created_at').first()
        elif session_id:
            conversation = Conversation.objects.filter(
                session_id=session_id
            ).order_by('-created_at').first()
        
        if not conversation:
            return JsonResponse({
                'success': True,
                'messages': [],
                'session_id': session_id
            })
        
        # Obtener mensajes
        messages = conversation.messages.all().order_by('timestamp')
        messages_data = []
        
        for msg in messages:
            messages_data.append({
                'id': msg.id,
                'content': msg.content,
                'sender': msg.sender,
                'timestamp': msg.timestamp.isoformat()
            })
        
        return JsonResponse({
            'success': True,
            'messages': messages_data,
            'session_id': conversation.session_id
        })
        
    except Exception as e:
        return JsonResponse({'error': f'Error al obtener historial: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def set_user_nutrition_goals(request):
    """Establecer objetivos nutricionales del usuario"""
    
    try:
        data = json.loads(request.body)
        user_id = data.get('user_id')
        session_id = data.get('session_id')
        
        if not user_id and not session_id:
            return JsonResponse({'error': 'Se requiere user_id o session_id'}, status=400)
        
        # Obtener o crear contexto de usuario
        user_context = None
        
        if user_id:
            user = Account.objects.get(id=user_id)
            user_context, created = UserContext.objects.get_or_create(
                user=user,
                defaults={'session_id': session_id if session_id else str(uuid.uuid4())}
            )
        else:
            user_context, created = UserContext.objects.get_or_create(
                session_id=session_id
            )
        
        # Actualizar datos
        if 'objetivo_calorias_diarias' in data:
            user_context.objetivo_calorias_diarias = data['objetivo_calorias_diarias']
        if 'objetivo_peso' in data:
            user_context.objetivo_peso = data['objetivo_peso']
        if 'objetivo_tipo' in data:
            user_context.objetivo_tipo = data['objetivo_tipo']
        if 'restricciones_alimentarias' in data:
            user_context.restricciones_alimentarias = data['restricciones_alimentarias']
        if 'preferencias_dieta' in data:
            user_context.preferencias_dieta = data['preferencias_dieta']
        
        user_context.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Objetivos nutricionales actualizados correctamente'
        })
        
    except Account.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error al guardar objetivos: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"]) 
def calculate_calories(request):
    """Calcular calorías diarias recomendadas"""
    
    try:
        data = json.loads(request.body)
        peso = float(data.get('peso', 0))
        altura = float(data.get('altura', 0))
        edad = int(data.get('edad', 0))
        sexo = data.get('sexo', 'mujer')
        nivel_actividad = data.get('nivel_actividad', 'moderado')
        
        if peso <= 0 or altura <= 0 or edad <= 0:
            return JsonResponse({'error': 'Datos inválidos para el cálculo'}, status=400)
        
        gemini_service = GeminiService()
        calorias_recomendadas = gemini_service.calculate_daily_calories(
            peso, altura, edad, sexo, nivel_actividad
        )
        
        return JsonResponse({
            'success': True,
            'calorias_diarias_recomendadas': calorias_recomendadas,
            'datos_utilizados': {
                'peso': peso,
                'altura': altura,
                'edad': edad,
                'sexo': sexo,
                'nivel_actividad': nivel_actividad
            }
        })
        
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Datos numéricos inválidos'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error en el cálculo: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def analyze_food(request):
    """Analizar información nutricional de alimentos usando Gemini"""
    
    try:
        data = json.loads(request.body)
        food_description = data.get('food_description', '').strip()
        
        if not food_description:
            return JsonResponse({'error': 'Descripción del alimento requerida'}, status=400)
        
        gemini_service = GeminiService()
        nutrition_analysis = gemini_service.get_nutrition_analysis(food_description)
        
        return JsonResponse({
            'success': True,
            'food_description': food_description,
            'nutrition_analysis': nutrition_analysis
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error al analizar el alimento: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def generate_meal_plan(request):
    """Generar plan de comidas personalizado usando Gemini"""
    
    try:
        data = json.loads(request.body)
        calories_target = int(data.get('calories_target', 2000))
        diet_type = data.get('diet_type', 'normal')
        meals_count = int(data.get('meals_count', 3))
        
        if calories_target <= 0 or calories_target > 5000:
            return JsonResponse({'error': 'Objetivo calórico inválido (debe estar entre 1 y 5000)'}, status=400)
        
        if meals_count < 1 or meals_count > 6:
            return JsonResponse({'error': 'Número de comidas inválido (debe estar entre 1 y 6)'}, status=400)
        
        gemini_service = GeminiService()
        meal_plan = gemini_service.get_meal_plan_suggestion(
            calories_target, diet_type, meals_count
        )
        
        return JsonResponse({
            'success': True,
            'calories_target': calories_target,
            'diet_type': diet_type,
            'meals_count': meals_count,
            'meal_plan': meal_plan
        })
        
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Datos numéricos inválidos'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error al generar plan de comidas: {str(e)}'}, status=500)


def get_or_create_conversation(user_id, session_id):
    """Obtiene o crea una conversación"""
    
    if user_id:
        try:
            user = Account.objects.get(id=user_id)
            # Buscar conversación reciente (último día)
            recent_conversation = Conversation.objects.filter(
                user=user,
                created_at__gte=datetime.now() - timedelta(days=1)
            ).first()
            
            if recent_conversation:
                return recent_conversation
            
            # Crear nueva conversación
            return Conversation.objects.create(
                user=user,
                session_id=session_id
            )
        except Account.DoesNotExist:
            pass
    
    # Para usuarios anónimos o si no se encuentra el usuario
    conversation, created = Conversation.objects.get_or_create(
        session_id=session_id,
        defaults={'created_at': datetime.now()}
    )
    
    return conversation


def calculate_age(birth_date):
    """Calcula la edad basada en la fecha de nacimiento"""
    today = datetime.now().date()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))