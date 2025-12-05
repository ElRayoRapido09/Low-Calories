import requests
import json
import os
import traceback
from django.conf import settings
from typing import List, Dict
from accounts.models import Account
from .models import UserContext


class GeminiService:
    """Servicio para manejar las interacciones con Google Gemini AI usando API REST"""
    
    def __init__(self):
        # 🔑 Tu API Key de Gemini
        self.api_key = 'AIzaSyD5pvAcMBdrYD8E9xaV7I9dnywuIawudIw'
        
        # URL de la API de Gemini
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        
        # Headers para las peticiones
        self.headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': self.api_key
        }
        
    def get_user_nutrition_prompt(self, user_data: Dict = None, user_context: UserContext = None) -> str:
        """Genera el prompt base con información nutricional del usuario"""
        base_prompt = """
        Eres un asistente nutricional especializado en ayudar a las personas con su alimentación y conteo de calorías. 
        Siempre respondes de manera amigable, profesional y enfocado en la salud.
        
        REGLAS IMPORTANTES:
        - Solo hablas sobre nutrición, alimentación, calorías, ejercicio y salud
        - Todas las medidas deben ser en sistema métrico (kg, cm, gramos, ml)
        - Siempre menciona calorías cuando sea relevante
        - No das consejos médicos específicos, solo nutricionales generales
        - Recomiendas consultar con profesionales para casos específicos
        - Respondes siempre en español
        - Sé conciso pero informativo
        - Usa emojis apropiados para hacer la conversación más amigable
        
        """
        
        if user_data:
            peso = user_data.get('peso')
            altura = user_data.get('altura') 
            edad = user_data.get('edad', 'no especificada')
            entrenamiento = user_data.get('entrenamiento', 'no especificado')
            
            user_info = f"""
            INFORMACIÓN DEL USUARIO:
            - Peso actual: {peso} kg
            - Altura: {altura} cm  
            - Edad: {edad} años
            - Nivel de entrenamiento: {entrenamiento}
            """
            
            if user_context:
                if user_context.objetivo_calorias_diarias:
                    user_info += f"\n- Objetivo calórico diario: {user_context.objetivo_calorias_diarias} calorías"
                if user_context.objetivo_peso:
                    user_info += f"\n- Peso objetivo: {user_context.objetivo_peso} kg"
                if user_context.objetivo_tipo:
                    user_info += f"\n- Objetivo: {user_context.get_objetivo_tipo_display()}"
                if user_context.preferencias_dieta:
                    user_info += f"\n- Tipo de dieta: {user_context.get_preferencias_dieta_display()}"
                if user_context.restricciones_alimentarias:
                    user_info += f"\n- Restricciones: {user_context.restricciones_alimentarias}"
            
            base_prompt += user_info + "\n"
            
        base_prompt += """
        Usa esta información para dar consejos personalizados. Si no tienes información del usuario, 
        puedes preguntar por datos relevantes para dar mejores recomendaciones.
        
        Ejemplos de respuestas apropiadas:
        - Información nutricional de alimentos (con calorías por 100g)
        - Planes de comidas personalizados
        - Consejos para ganar/perder/mantener peso
        - Recomendaciones de ejercicio relacionadas con la nutrición
        - Cálculos de necesidades calóricas
        """
        
        return base_prompt
    
    def generate_response(self, user_message: str, conversation_history: List[Dict] = None, 
                         user_data: Dict = None, user_context: UserContext = None) -> str:
        """Genera una respuesta usando Google Gemini API REST"""
        
        try:
            # Preparar el prompt completo
            system_prompt = self.get_user_nutrition_prompt(user_data, user_context)
            
            # Construir contexto de conversación
            full_prompt = system_prompt + "\n\n"
            
            # Agregar historial de conversación reciente (últimos 6 mensajes)
            if conversation_history:
                full_prompt += "HISTORIAL DE CONVERSACIÓN RECIENTE:\n"
                # Obtener últimos 6 mensajes sin usar indexing negativo
                recent_messages = conversation_history
                if len(recent_messages) > 6:
                    recent_messages = recent_messages[len(recent_messages)-6:]
                
                for msg in recent_messages:
                    role = "Usuario" if msg.get('sender') == 'user' else "Asistente"
                    content = msg.get('content', '')
                    full_prompt += f"{role}: {content}\n"
                full_prompt += "\n"
            
            # Agregar mensaje actual
            full_prompt += f"Usuario: {user_message}\nAsistente:"
            
            # Preparar el payload para la API REST
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": full_prompt
                            }
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.7,
                    "topP": 0.8,
                    "topK": 40,
                    "maxOutputTokens": 500
                }
            }
            
            # Realizar petición a la API
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            # Verificar si la petición fue exitosa
            if response.status_code == 200:
                result = response.json()
                
                # Debug: imprimir respuesta completa
                print(f"DEBUG - Respuesta de Gemini API: {json.dumps(result, indent=2)}")
                
                # Extraer el texto de la respuesta
                if 'candidates' in result and len(result['candidates']) > 0:
                    candidate = result['candidates'][0]
                    if 'content' in candidate and 'parts' in candidate['content']:
                        parts = candidate['content']['parts']
                        if len(parts) > 0:
                            text = parts[0].get('text', '')
                            if text:
                                print(f"DEBUG - Texto extraído exitosamente: {text[:100]}...")
                                return text.strip()
                            else:
                                print("DEBUG - El campo 'text' está vacío")
                        else:
                            print("DEBUG - No hay partes en la respuesta")
                    else:
                        print(f"DEBUG - Estructura inesperada en candidate: {candidate}")
                else:
                    print(f"DEBUG - No hay candidatos válidos en la respuesta")
                
                # Usar respuesta de respaldo si Gemini no devuelve texto
                print("DEBUG - Usando respuesta de respaldo")
                return self._get_fallback_nutrition_response(user_message, user_data, user_context)
            
            elif response.status_code == 400:
                print(f"DEBUG - Error 400 de Gemini API: {response.text}")
                return self._get_fallback_nutrition_response(user_message, user_data, user_context)
            
            elif response.status_code == 403:
                print("DEBUG - Error 403 de autenticación con Gemini API")
                return self._get_fallback_nutrition_response(user_message, user_data, user_context)
            
            elif response.status_code == 429:
                print("DEBUG - Rate limit alcanzado en Gemini API")
                return "⚠️ He alcanzado el límite de uso por hoy. Intenta nuevamente más tarde."
            
            else:
                print(f"DEBUG - Error {response.status_code} de Gemini API: {response.text}")
                return self._get_fallback_nutrition_response(user_message, user_data, user_context)
            
        except requests.exceptions.Timeout:
            print("DEBUG - Timeout en petición a Gemini API")
            return self._get_fallback_nutrition_response(user_message, user_data, user_context)
        
        except requests.exceptions.ConnectionError:
            print("DEBUG - Error de conexión con Gemini API")
            return self._get_fallback_nutrition_response(user_message, user_data, user_context)
        
        except Exception as e:
            print(f"DEBUG - Error inesperado: {str(e)}")
            import traceback
            traceback.print_exc()
            return self._get_fallback_nutrition_response(user_message, user_data, user_context)
    
    def calculate_daily_calories(self, peso: float, altura: float, edad: int, 
                               sexo: str, nivel_actividad: str) -> int:
        """Calcula las calorías diarias recomendadas usando la fórmula Harris-Benedict"""
        
        # Calcular TMB (Tasa Metabólica Basal)
        if sexo.lower() in ['hombre', 'masculino', 'male']:
            tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
        else:  # mujer
            tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
        
        # Factores de actividad
        factores_actividad = {
            'sedentario': 1.2,
            'moderado': 1.55,
            'activo': 1.725,
            'muy_activo': 1.9,
            'muy activo': 1.9
        }
        
        factor = factores_actividad.get(nivel_actividad.lower(), 1.55)
        calorias_diarias = int(tmb * factor)
        
        return calorias_diarias
    
    def get_nutrition_analysis(self, food_description: str) -> str:
        """Analiza información nutricional de alimentos usando Gemini API REST"""
        
        prompt = f"""
        Analiza la siguiente descripción de alimento o comida: "{food_description}"
        
        Proporciona información nutricional detallada incluyendo:
        1. Calorías aproximadas por 100g o por porción típica
        2. Macronutrientes principales (carbohidratos, proteínas, grasas)
        3. Micronutrientes importantes (vitaminas, minerales)
        4. Beneficios para la salud
        5. Recomendaciones de consumo
        
        Responde en español, de forma concisa y práctica.
        """
        
        try:
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and len(result['candidates']) > 0:
                    candidate = result['candidates'][0]
                    if 'content' in candidate and 'parts' in candidate['content']:
                        text = candidate['content']['parts'][0].get('text', '')
                        if text:
                            return text.strip()
            
            return "No pude obtener información nutricional para ese alimento."
            
        except Exception:
            return "Error al analizar la información nutricional."
    
    def get_meal_plan_suggestion(self, calories_target: int, diet_type: str = "normal", 
                               meals_count: int = 3) -> str:
        """Genera sugerencia de plan de comidas usando Gemini API REST"""
        
        prompt = f"""
        Crea un plan de comidas para un día con las siguientes especificaciones:
        - Calorías objetivo: {calories_target} calorías
        - Tipo de dieta: {diet_type}
        - Número de comidas: {meals_count}
        
        Incluye:
        1. Distribución de calorías por comida
        2. Alimentos específicos con cantidades en gramos
        3. Métodos de preparación simples
        4. Alternativas saludables
        
        Responde en español, de forma clara y práctica.
        """
        
        try:
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and len(result['candidates']) > 0:
                    candidate = result['candidates'][0]
                    if 'content' in candidate and 'parts' in candidate['content']:
                        text = candidate['content']['parts'][0].get('text', '')
                        if text:
                            return text.strip()
            
            return "No pude generar un plan de comidas personalizado."
            
        except Exception:
            return "Error al generar el plan de comidas."
    
    def _get_fallback_nutrition_response(self, user_message: str, user_data: Dict = None, user_context: UserContext = None) -> str:
        """Genera respuestas de respaldo usando lógica local cuando Gemini no está disponible"""
        
        message_lower = user_message.lower()
        
        # Respuestas para cálculos de calorías
        if any(word in message_lower for word in ['calorias', 'calorías', 'necesito', 'diario', 'día']):
            if user_data:
                peso = user_data.get('peso', 70)
                altura = user_data.get('altura', 170)
                edad = user_data.get('edad', 30)
                calorias = self.calculate_daily_calories(peso, altura, edad, 'mujer', 'moderado')
                return f"🔢 Basándome en tus datos (peso: {peso}kg, altura: {altura}cm), necesitas aproximadamente **{calorias} calorías** al día.\n\n📝 Esta es una estimación general. Para un plan personalizado, consulta con un nutricionista."
            else:
                return "🔢 Para calcular tus calorías diarias necesito conocer tu peso, altura, edad y nivel de actividad.\n\n📊 En promedio, una persona adulta necesita entre 1800-2500 calorías al día."
        
        # Respuestas sobre alimentos específicos
        elif any(word in message_lower for word in ['pollo', 'carne', 'proteína', 'proteina']):
            return "🍗 **Pollo (100g pechuga sin piel):**\n• Calorías: ~165 kcal\n• Proteínas: 31g\n• Grasas: 3.6g\n• Carbohidratos: 0g\n\n💪 Es una excelente fuente de proteína magra, ideal para ganar músculo y perder grasa."
        
        elif any(word in message_lower for word in ['pescado', 'salmón', 'salmon', 'atún', 'atun']):
            return "🐟 **Salmón (100g):**\n• Calorías: ~200 kcal\n• Proteínas: 22g\n• Grasas: 12g (Omega-3)\n• Carbohidratos: 0g\n\n🧠 Rico en Omega-3, excelente para la salud cardiovascular y cerebral."
        
        elif any(word in message_lower for word in ['huevo', 'huevos']):
            return "🥚 **Huevo (1 unidad mediana):**\n• Calorías: ~70 kcal\n• Proteínas: 6g\n• Grasas: 5g\n• Carbohidratos: 0.5g\n\n⭐ Proteína completa con todos los aminoácidos esenciales."
        
        elif any(word in message_lower for word in ['arroz', 'carbohidratos', 'carbohidrato']):
            return "🍚 **Arroz blanco cocido (100g):**\n• Calorías: ~130 kcal\n• Proteínas: 2.7g\n• Grasas: 0.3g\n• Carbohidratos: 28g\n\n⚡ Fuente rápida de energía, ideal post-entrenamiento."
        
        # Respuestas sobre planes de alimentación
        elif any(word in message_lower for word in ['plan', 'comidas', 'dieta', 'menú', 'menu']):
            return "🍽️ **Plan básico de 3 comidas:**\n\n🌅 **Desayuno:**\n• 2 huevos + 1 tostada integral\n• 1 fruta + yogur natural\n\n🌞 **Almuerzo:**\n• 150g proteína (pollo/pescado)\n• 100g carbohidratos (arroz/pasta)\n• Ensalada mixta\n\n🌙 **Cena:**\n• Proteína magra + vegetales\n• Ensalada o verduras al vapor\n\n💡 Ajusta las porciones según tus objetivos calóricos."
        
        # Respuestas sobre pérdida de peso
        elif any(word in message_lower for word in ['perder', 'bajar', 'peso', 'adelgazar', 'quemar']):
            return "📉 **Para perder peso:**\n\n🔥 **Déficit calórico:** Consume 300-500 calorías menos de tu gasto diario\n\n🥗 **Alimentos recomendados:**\n• Proteínas magras (pollo, pescado, huevos)\n• Vegetales de hoja verde\n• Frutas con fibra\n• Granos integrales (moderadamente)\n\n⚠️ Nunca bajes de 1200 kcal/día. Consulta un profesional para un plan personalizado."
        
        # Respuestas sobre ganar peso/músculo
        elif any(word in message_lower for word in ['ganar', 'aumentar', 'músculo', 'musculo', 'masa']):
            return "💪 **Para ganar músculo:**\n\n📈 **Superávit calórico:** Consume 300-500 calorías extra\n\n🍖 **Enfoque en proteínas:**\n• 1.6-2.2g por kg de peso corporal\n• Distribuye en 4-6 comidas\n\n🏋️ **Combina con ejercicio de resistencia**\n\n🥛 **Post-entrenamiento:** Proteína + carbohidratos en 30-60 min"
        
        # Respuesta general
        else:
            return f"🤖 Hola! Soy tu asistente nutricional. Aunque tengo problemas técnicos temporales, puedo ayudarte con:\n\n• 📊 Cálculos de calorías diarias\n• 🍎 Información nutricional básica\n• 🏃‍♀️ Consejos para tus objetivos\n• 🥗 Recomendaciones de alimentación\n\n💬 Pregúntame algo específico como: '¿Cuántas calorías tiene el pollo?' o '¿Cómo ganar músculo?'"