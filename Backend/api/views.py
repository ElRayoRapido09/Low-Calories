from django.conf import settings
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import HistorialModel
from .utils import recognize_food_caloriemama
from django.contrib.auth import get_user_model
import os

User = get_user_model()


def add_cors_headers(response):
    """Agrega headers CORS a la respuesta"""
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response["Access-Control-Max-Age"] = "3600"
    return response


class ScanFoodView(APIView):
    """
    Vista para escanear comida usando CalorieMama que ya incluye información nutricional
    """
    permission_classes = [AllowAny]

    def options(self, request, *args, **kwargs):
        """Maneja las peticiones OPTIONS para CORS preflight"""
        response = Response()
        return add_cors_headers(response)

    def post(self, request, *args, **kwargs):
        print("📸 Solicitud recibida en ScanFoodView")
        
        image_file = request.FILES.get('image')
        
        if not image_file:
            print("❌ No se proporcionó imagen")
            response = Response({
                "success": False,
                "error": "No se proporcionó ninguna imagen."
            }, status=status.HTTP_400_BAD_REQUEST)
            return add_cors_headers(response)

        print(f"✅ Imagen recibida: {image_file.name}, tamaño: {image_file.size} bytes")

        # 1. Guardar la imagen temporalmente
        try:
            file_name = default_storage.save(f'escaneos/{image_file.name}', image_file)
            file_path = default_storage.path(file_name)
            print(f"💾 Imagen guardada en: {file_path}")
        except Exception as e:
            print(f"❌ Error guardando imagen: {str(e)}")
            response = Response({
                "success": False,
                "error": f"Error al guardar la imagen: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return add_cors_headers(response)

        try:
            # 2. Llamar a CalorieMama para reconocer la comida
            print("🔍 Llamando a CalorieMama...")
            recognition_result = recognize_food_caloriemama(file_path)
            
            print(f"📊 Resultado de CalorieMama: {recognition_result}")
            
            if "error" in recognition_result:
                # Si CalorieMama falla, eliminar la imagen y devolver error
                default_storage.delete(file_name)
                print(f"❌ Error en CalorieMama: {recognition_result['error']}")
                response = Response({
                    "success": False,
                    "error": recognition_result["error"],
                    "manual_capture": True
                }, status=status.HTTP_404_NOT_FOUND)
                return add_cors_headers(response)
            
            # 3. Extraer datos nutricionales de CalorieMama
            recognized_food_name = recognition_result.get('food_name')
            confidence = recognition_result.get('confidence', 0)
            nutrition = recognition_result.get('nutrition', {})
            serving_sizes = recognition_result.get('serving_sizes', [])
            
            print(f"✅ Comida reconocida: {recognized_food_name} (confianza: {confidence})")
            print(f"📊 Datos nutricionales crudos: {nutrition}")
            
            # CalorieMama devuelve valores por kg (en decimal)
            # Convertir a valores por 100g
            calories = round(nutrition.get('calories', 0) / 10, 1) if nutrition.get('calories') else None
            protein = round(nutrition.get('protein', 0) * 100, 2) if nutrition.get('protein') else None
            carbohydrates = round(nutrition.get('totalCarbs', 0) * 100, 2) if nutrition.get('totalCarbs') else None
            fat = round(nutrition.get('totalFat', 0) * 100, 2) if nutrition.get('totalFat') else None
            
            # Obtener el tamaño de porción más común (usualmente el primero)
            serving_size = None
            if serving_sizes and len(serving_sizes) > 0:
                first_serving = serving_sizes[0]
                serving_size = first_serving.get('unit', 'Por 100g')
            else:
                serving_size = 'Por 100g'
            
            print(f"\n{'='*60}")
            print(f"📊 INFORMACIÓN NUTRICIONAL PROCESADA:")
            print(f"{'='*60}")
            print(f"   🍽️  Alimento: {recognized_food_name}")
            print(f"   📏 Porción: {serving_size}")
            print(f"   🔥 Calorías: {calories} kcal")
            print(f"   🥩 Proteínas: {protein}g")
            print(f"   🍞 Carbohidratos: {carbohydrates}g")
            print(f"   🥑 Grasas: {fat}g")
            print(f"   ✨ Confianza: {confidence}%")
            print(f"{'='*60}\n")
            
            # 4. Obtener o crear usuario
            if request.user.is_authenticated:
                user = request.user
            else:
                # Crear o usar usuario "sistema" para usuarios no autenticados
                user, created = User.objects.get_or_create(
                    username='sistema_escaneo',
                    defaults={
                        'email': 'sistema@lowcalories.com',
                        'first_name': 'Sistema',
                        'last_name': 'Escaneo'
                    }
                )
                if created:
                    user.set_unusable_password()
                    user.save()
                    print("👤 Usuario 'sistema_escaneo' creado")
            
            # 5. Guardar en el historial
            historial_entry = HistorialModel.objects.create(
                user=user,
                nombre_alimento=recognized_food_name,
                calorias=calories,
                proteinas=protein,
                carbohidratos=carbohydrates,
                grasas=fat,
                img=file_name,
                cantidad_consumida=None,
                metodo_registro='ESCANEADO'
            )
            
            print(f"💾 Registro guardado en historial con ID: {historial_entry.id}")
            print(f"   - Nombre: {historial_entry.nombre_alimento}")
            print(f"   - Calorías: {historial_entry.calorias}")
            print(f"   - Proteínas: {historial_entry.proteinas}")
            print(f"   - Carbohidratos: {historial_entry.carbohidratos}")
            print(f"   - Grasas: {historial_entry.grasas}")
            
            # 6. Preparar respuesta
            response = Response({
                "success": True,
                "historial_id": historial_entry.id,
                "message": "Comida reconocida exitosamente",
                "data": {
                    "food_name": recognized_food_name,
                    "calories": calories,
                    "protein": protein,
                    "carbohydrates": carbohydrates,
                    "fat": fat,
                    "serving_size": serving_size,
                    "confidence": confidence,
                    "image_url": request.build_absolute_uri(settings.MEDIA_URL + file_name),
                    "serving_options": serving_sizes[:5]  # Primeras 5 opciones de porción
                }
            }, status=status.HTTP_201_CREATED)
            return add_cors_headers(response)
        
        except Exception as e:
            print(f"❌ Error inesperado: {str(e)}")
            import traceback
            traceback.print_exc()
            
            # Eliminar la imagen en caso de error
            if default_storage.exists(file_name):
                default_storage.delete(file_name)
            
            response = Response({
                "success": False,
                "error": f"Error procesando la imagen: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return add_cors_headers(response)


class FoodHistoryView(APIView):
    """
    Vista para obtener el historial de comidas escaneadas
    """
    permission_classes = [AllowAny]
    
    def options(self, request, *args, **kwargs):
        """Maneja las peticiones OPTIONS para CORS preflight"""
        response = Response()
        return add_cors_headers(response)

    def get(self, request, *args, **kwargs):
        try:
            # Si hay usuario autenticado, filtrar por usuario
            if request.user.is_authenticated:
                historial = HistorialModel.objects.filter(user=request.user).order_by('-fecha')
            else:
                # Si no hay usuario, devolver todos (para testing)
                historial = HistorialModel.objects.all().order_by('-fecha')
            
            data = []
            for item in historial:
                data.append({
                    'id': item.id,
                    'nombre_alimento': item.nombre_alimento,
                    'calorias': item.calorias,
                    'proteinas': item.proteinas,
                    'carbohidratos': item.carbohidratos,
                    'grasas': item.grasas,
                    'cantidad_consumida': item.cantidad_consumida,
                    'fecha': item.fecha,
                    'metodo_registro': item.metodo_registro,
                    'tipo_comida': item.tipo_comida,
                    'image_url': request.build_absolute_uri(settings.MEDIA_URL + item.img.name) if item.img else None
                })
            
            response = Response(data, status=status.HTTP_200_OK)
            return add_cors_headers(response)
            
        except Exception as e:
            print(f"Error obteniendo historial: {str(e)}")
            response = Response({
                "error": f"Error obteniendo historial: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return add_cors_headers(response)