<script>
  import { onMount } from 'svelte';
  import { _ } from 'svelte-i18n';

  // Estado del chat
  let messages = $state([
    {
      id: 1,
      content: `${$_('chatbot.welcome')}\n\n${$_('chatbot.howCanHelp')}\n\n🍎 **${$_('chatbot.specialties')}**\n• ${$_('chatbot.nutritionAnalysis')}\n• ${$_('chatbot.calorieCalculation')}\n• ${$_('chatbot.customMealPlans')}\n• ${$_('chatbot.healthyEating')}\n• ${$_('chatbot.macroMicro')}\n\n💬 **${$_('chatbot.exampleQuestions')}**\n• "${$_('chatbot.question1')}"\n• "${$_('chatbot.question2')}"\n• "${$_('chatbot.question3')}"\n• "${$_('chatbot.question4')}"`,
      sender: 'bot',
      timestamp: new Date().toLocaleTimeString()
    }
  ]);

  let newMessage = $state('');
  let chatContainer = $state(null);
  let isTyping = $state(false);
  let sessionId = $state('');
  let userId = $state(null); // Se puede obtener del login si está implementado

  // Configuración de la API
  const API_BASE_URL = 'http://127.0.0.1:8000/api/chatbot';

  // Función para enviar mensaje
  async function sendMessage() {
    if (newMessage.trim() === '' || isTyping) return;

    const userMessage = newMessage.trim();
    newMessage = '';

    // Agregar mensaje del usuario a la UI
    const userMsg = {
      id: messages.length + 1,
      content: userMessage,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString()
    };
    messages.push(userMsg);

    // Mostrar indicador de "escribiendo..."
    isTyping = true;
    scrollToBottom();

    try {
      // Enviar mensaje a la API
      const response = await fetch(`${API_BASE_URL}/chat/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: userMessage,
          session_id: sessionId,
          user_id: userId
        })
      });

      const data = await response.json();

      if (response.ok && data.success) {
        // Actualizar session_id si es nuevo
        if (data.session_id && !sessionId) {
          sessionId = data.session_id;
          if (typeof localStorage !== 'undefined') {
            localStorage.setItem('chatbot_session_id', sessionId);
          }
        }

        // Agregar respuesta del bot
        const botMsg = {
          id: messages.length + 1,
          content: data.bot_response.content,
          sender: 'bot',
          timestamp: new Date(data.bot_response.timestamp).toLocaleTimeString()
        };
        messages.push(botMsg);

      } else {
        // Manejar errores de la API
        const errorMsg = {
          id: messages.length + 1,
          content: data.error || $_('chatbot.serverError'),
          sender: 'bot',
          timestamp: new Date().toLocaleTimeString()
        };
        messages.push(errorMsg);
      }

    } catch (error) {
      console.error('Error al enviar mensaje:', error);
      
      // Mensaje de error para el usuario
      const errorMsg = {
        id: messages.length + 1,
        content: $_('chatbot.connectionError'),
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      };
      messages.push(errorMsg);
    } finally {
      isTyping = false;
      scrollToBottom();
    }
  }

  // Cargar historial de conversación al inicio
  async function loadConversationHistory() {
    if (!sessionId) return;

    try {
      const response = await fetch(`${API_BASE_URL}/history/?session_id=${sessionId}`);
      const data = await response.json();

      if (response.ok && data.success && data.messages.length > 0) {
        // Limpiar mensaje de bienvenida y cargar historial
        messages = data.messages.map((msg, index) => ({
          id: index + 1,
          content: msg.content,
          sender: msg.sender,
          timestamp: new Date(msg.timestamp).toLocaleTimeString()
        }));
      }
    } catch (error) {
      console.error('Error al cargar historial:', error);
    }
  }

  function scrollToBottom() {
    setTimeout(() => {
      if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      }
    }, 100);
  }

  function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  }

  // Función para analizar un alimento específico
  async function analyzeFood(foodDescription) {
    try {
      const response = await fetch(`${API_BASE_URL}/analyze-food/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          food_description: foodDescription
        })
      });

      const data = await response.json();
      if (response.ok && data.success) {
        return data.nutrition_analysis;
      }
      return null;
    } catch (error) {
      console.error('Error al analizar alimento:', error);
      return null;
    }
  }

  // Función para generar un plan de comidas
  async function generateMealPlan(caloriesTarget = 2000, dietType = 'normal', mealsCount = 3) {
    try {
      const response = await fetch(`${API_BASE_URL}/generate-meal-plan/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          calories_target: caloriesTarget,
          diet_type: dietType,
          meals_count: mealsCount
        })
      });

      const data = await response.json();
      if (response.ok && data.success) {
        return data.meal_plan;
      }
      return null;
    } catch (error) {
      console.error('Error al generar plan de comidas:', error);
      return null;
    }
  }

  // Función para establecer objetivos nutricionales
  async function setNutritionGoals() {
    if (!sessionId) return;

    try {
      const response = await fetch(`${API_BASE_URL}/goals/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          session_id: sessionId,
          user_id: userId,
          objetivo_calorias_diarias: 2000,
          objetivo_peso: 70,
          objetivo_tipo: 'mantener',
          preferencias_dieta: 'normal'
        })
      });
      
      if (response.ok) {
        console.log('Objetivos nutricionales establecidos');
      }
    } catch (error) {
      console.error('Error al establecer objetivos:', error);
    }
  }

  onMount(() => {
    // Recuperar session_id del localStorage
    if (typeof localStorage !== 'undefined') {
      const savedSessionId = localStorage.getItem('chatbot_session_id');
      if (savedSessionId) {
        sessionId = savedSessionId;
        loadConversationHistory();
      }
    }
    
    scrollToBottom();
  });
</script>

<main class="chat-main">

    <header class="chat-header">
        <a href="/" class="back-btn" aria-label={$_('common.back')}>‹</a>
        <div class="header-content">
            <h1>{$_('chatbot.title')}</h1>
            <p>{$_('chatbot.poweredBy')}</p>
        </div>
    </header>

  <!-- aqui van los mensajes -->
  <div class="chat-container" bind:this={chatContainer}>
    {#each messages as message}
      <div class="message {message.sender}">
        <div class="message-avatar">
          {#if message.sender === 'bot'}
            🤖 <!--avatar de la IA-->
          {:else}
            👤  <!--avatar del usuario-->
          {/if}
        </div>
        <div class="message-content">
          <p class="message-text">{@html message.content.replace(/\n/g, '<br>')}</p>
          <span class="message-time">{message.timestamp}</span>
        </div>
      </div>
    {/each}

    <!-- Indicador de "escribiendo..." -->
    {#if isTyping}
      <div class="message bot typing-indicator">
        <div class="message-avatar">🤖</div>
        <div class="message-content">
          <div class="typing-dots">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <span class="message-time">{$_('chatbot.typing')}</span>
        </div>
      </div>
    {/if}
  </div>

  <!-- Input para escribir mensajes -->
  <div class="chat-input-container">
    <textarea
      bind:value={newMessage}
      onkeydown={handleKeyPress}
      placeholder={$_('chatbot.placeholder')}
      class="chat-input"
      rows="1"
      disabled={isTyping}
    ></textarea>
    <button 
      onclick={sendMessage} 
      class="send-button" 
      disabled={!newMessage.trim() || isTyping}
      title={$_('chatbot.send')}
    >
      {#if isTyping}
        ⏳
      {:else}
        📤
      {/if}
    </button>
  </div>
</main>

<style>
  .chat-main {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background: #ffffff;
    font-family: inherit;
  }

 .chat-header {
    background: #f5f5f5;
    padding: 1rem;
    border-bottom: 1px solid #e0e0e0;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.header-content {
    flex: 1;
    text-align: center;
}

.chat-header h1 {
    margin: 0;
    font-size: 1.5rem;
    color: #005bb5;
    font-weight: 700;
}

.chat-header p {
    margin: 0.5rem 0 0 0;
    color: #666;
    font-size: 0.9rem;
}

  .chat-container {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .message {
    display: flex;
    gap: 0.5rem;
    max-width: 80%;
  }

  .message.bot {
    align-self: flex-start;
  }

  .message.user {
    align-self: flex-end;
    flex-direction: row-reverse;
  }

  .message-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #f5f5f5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
  }

  .message-content {
    background: #f5f5f5;
    padding: 0.75rem 1rem;
    border-radius: 18px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .message.user .message-content {
    background: #005bb5;
    color: #fff;
  }

  .message-text {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.4;
  }

  .message-time {
    display: block;
    font-size: 0.75rem;
    color: #999;
    margin-top: 0.25rem;
  }

  .message.user .message-time {
    color: rgba(255, 255, 255, 0.7);
  }

  .chat-input-container {
    display: flex;
    padding: 1rem;
    background: #f5f5f5;
    border-top: 1px solid #e0e0e0;
    gap: 0.5rem;
  }

  .chat-input {
    flex: 1;
    padding: 0.75rem 1rem;
    border: 1px solid #e0e0e0;
    border-radius: 25px;
    font-size: 1rem;
    background: #fff;
    outline: none;
    resize: none;
    min-height: 50px;
    max-height: 120px;
    font-family: inherit;
    line-height: 1.4;
  }

  .chat-input:focus {
    border-color: #005bb5;
  }

  .chat-input:disabled {
    background: #f5f5f5;
    cursor: not-allowed;
  }

  .send-button {
    width: 50px;
    height: 50px;
    border: none;
    border-radius: 50%;
    background: #005bb5;
    color: #fff;
    font-size: 1.2rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    flex-shrink: 0;
  }

  .send-button:hover:not(:disabled) {
    background: #004499;
    transform: scale(1.05);
  }

  .send-button:disabled {
    background: #ccc;
    cursor: not-allowed;
    transform: none;
  }

  /* Indicador de "escribiendo..." */
  .typing-indicator .message-content {
    background: #f5f5f5;
    padding: 1rem;
  }

  .typing-dots {
    display: flex;
    gap: 0.25rem;
    margin-bottom: 0.5rem;
  }

  .typing-dots span {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #999;
    animation: typing 1.4s infinite;
  }

  .typing-dots span:nth-child(1) { animation-delay: 0s; }
  .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
  .typing-dots span:nth-child(3) { animation-delay: 0.4s; }

  @keyframes typing {
    0%, 60%, 100% {
      transform: scale(1);
      opacity: 0.5;
    }
    30% {
      transform: scale(1.2);
      opacity: 1;
    }
  }

  /* Mejor formato para texto con saltos de línea */
  .message-text {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.4;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  /* Scrollbar personalizada */
  .chat-container::-webkit-scrollbar {
    width: 6px;
  }

  .chat-container::-webkit-scrollbar-track {
    background: #f1f1f1;
  }

  .chat-container::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 3px;
  }

  .chat-container::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
  }

  
  @media (max-width: 768px) {
    .message {
      max-width: 90%;
    }
  }
 .back-btn {
    color: #000;
    font-size: 28px;
    text-decoration: none;
    padding: 6px;
    margin-right: auto;
}
</style>