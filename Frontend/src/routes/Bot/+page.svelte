<script>
  import { onMount } from 'svelte';


  let messages = $state([
    {
      id: 1,
      text: "¡Hola! Soy tu asistente nutricional. ¿En qué puedo ayudarte hoy? 🍎",
      sender: 'bot',
      timestamp: new Date().toLocaleTimeString()
    }
  ]);

  let newMessage = $state('');
  let chatContainer = $state(null);

  // Función para enviar mensaje
  function sendMessage() {
    if (newMessage.trim() === '') return;

    // Agregar mensaje del usuario
    messages.push({
      id: messages.length + 1,
      text: newMessage,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString()
    });

    const userMessage = newMessage;
    newMessage = '';

    // Simular respuesta del bot (puedes reemplazar con API real)
    setTimeout(() => {
      let botResponse = "¡Gracias por tu mensaje! Estoy procesando tu consulta sobre nutrición.";

      // Respuestas simuladas basadas en palabras clave
      if (userMessage.toLowerCase().includes('Jorge')) {
        botResponse = "Jorge es mi puta";
      } else if (userMessage.toLowerCase().includes('Antuane')) {
        botResponse = "ese wey la mama bien rico";
      } else if (userMessage.toLowerCase().includes('ricardo')) {
        botResponse = "ricardo no le sabe al sexo";
      }

      messages.push({
        id: messages.length + 1,
        text: botResponse,
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      });

    
      scrollToBottom();
    }, 1000);

    scrollToBottom();
  }


  function scrollToBottom() {
    if (chatContainer) {
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  }

 
  function handleKeyPress(event) {
    if (event.key === 'Enter') {
      sendMessage();
    }
  }

  onMount(() => {
    scrollToBottom();
  });
</script>

<main class="chat-main">

    <header class="chat-header">
        <a href="/" class="back-btn" aria-label="Volver">‹</a>
        <div class="header-content">
            <h1>Asistente Nutricional</h1>
            <p>Tu compañero para una vida saludable</p>
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
          <p class="message-text">{message.text}</p>
          <span class="message-time">{message.timestamp}</span>
        </div>
      </div>
    {/each}
  </div>

 
  <div class="chat-input-container">
    <input
      type="text"
      bind:value={newMessage}
      on:keydown={handleKeyPress}
      placeholder="Escribe tu mensaje aquí..."
      class="chat-input"
    />
    <button on:click={sendMessage} class="send-button" disabled={!newMessage.trim()}>
      📤
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
  }

  .chat-input:focus {
    border-color: #005bb5;
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
    transition: background 0.2s;
  }

  .send-button:hover:not(:disabled) {
    background: #004499;
  }

  .send-button:disabled {
    background: #ccc;
    cursor: not-allowed;
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