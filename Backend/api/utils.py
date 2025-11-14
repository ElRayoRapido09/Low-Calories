import requests
from django.conf import settings
from PIL import Image
import io


def recognize_food_caloriemama(image_path):
    """
    Reconoce comida usando la API de CalorieMama
    CalorieMama requiere: JPEG, 544x544px y YA incluye información nutricional
    
    Args:
        image_path: Ruta local del archivo de imagen
        
    Returns:
        dict: Información del alimento reconocido con datos nutricionales o error
    """
    api_key = settings.CALORIEMAMA_API_KEY
    url = "https://api-2445582032290.production.gw.apicast.io/v1/foodrecognition"
    
    try:
        # 1. Abrir y redimensionar la imagen a 544x544
        with Image.open(image_path) as img:
            # Convertir a RGB si es necesario
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Redimensionar manteniendo aspecto
            img.thumbnail((544, 544), Image.Resampling.LANCZOS)
            
            # Crear una imagen cuadrada de 544x544
            new_img = Image.new('RGB', (544, 544), (255, 255, 255))
            
            # Calcular posición para centrar la imagen
            offset = ((544 - img.size[0]) // 2, (544 - img.size[1]) // 2)
            new_img.paste(img, offset)
            
            # Guardar en memoria como JPEG
            img_byte_arr = io.BytesIO()
            new_img.save(img_byte_arr, format='JPEG', quality=95)
            img_byte_arr.seek(0)
            
            print(f"📐 Imagen procesada: 544x544px, formato JPEG")
            
            # 2. Enviar a CalorieMama
            files = {'media': ('food.jpg', img_byte_arr, 'image/jpeg')}
            params = {'user_key': api_key}
            
            print(f"🚀 Enviando a CalorieMama...")
            response = requests.post(url, files=files, params=params, timeout=30)
            
            print(f"📡 Respuesta de CalorieMama: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                
                # Extraer el primer resultado con mayor confianza
                if 'results' in data and len(data['results']) > 0:
                    best_result = data['results'][0]
                    
                    # CalorieMama devuelve 'items' con los alimentos detectados
                    items = best_result.get('items', [])
                    if items and len(items) > 0:
                        first_item = items[0]
                        
                        return {
                            'food_name': first_item.get('name', 'Unknown'),
                            'confidence': first_item.get('score', 0),
                            'nutrition': first_item.get('nutrition', {}),
                            'serving_sizes': first_item.get('servingSizes', []),
                            'food_id': first_item.get('food_id'),
                            'group': first_item.get('group', ''),
                            'full_response': data
                        }
                    else:
                        return {
                            'error': 'No se detectó comida en la imagen. Por favor, intenta con mejor iluminación.'
                        }
                else:
                    return {
                        'error': 'No se detectó comida en la imagen. Asegúrate que la comida sea visible.'
                    }
            elif response.status_code == 400:
                error_data = response.json() if response.content else {}
                print(f"❌ Error 400: {error_data}")
                return {
                    'error': 'Imagen no válida. Asegúrate de tomar una foto clara de la comida.'
                }
            elif response.status_code == 401:
                return {
                    'error': 'API Key inválida o expirada. Contacta al administrador.'
                }
            elif response.status_code == 429:
                return {
                    'error': 'Límite de API alcanzado. Intenta más tarde.'
                }
            else:
                error_text = response.text[:200]
                print(f"❌ Error {response.status_code}: {error_text}")
                return {
                    'error': f'Error al contactar CalorieMama: {response.status_code}'
                }
                
    except FileNotFoundError:
        return {'error': 'Archivo de imagen no encontrado'}
    except requests.exceptions.Timeout:
        return {'error': 'Tiempo de espera agotado. Verifica tu conexión.'}
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {str(e)}")
        return {'error': f'Error de conexión: {str(e)}'}
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        import traceback
        traceback.print_exc()
        return {'error': f'Error procesando imagen: {str(e)}'}