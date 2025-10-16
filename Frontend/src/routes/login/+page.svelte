<script>
  // Login / Registro / Recuperación de contraseña
  import { onMount } from 'svelte';

  let mode = 'login'; // 'login' | 'register' | 'recover'

  // Campos comunes
  let email = '';
  let password = '';
  let passwordConfirm = '';

  // Estado UI
  let loading = false;
  let error = '';
  let success = '';

  function clearMessages() {
    error = '';
    success = '';
  }

  /**
   * @param {string} value
   */
  function validateEmail(value) {
    return /\S+@\S+\.\S+/.test(value);
  }

  async function submitLogin() {
    clearMessages();
    if (!validateEmail(email)) { error = 'Introduce un correo válido'; return; }
    if (!password) { error = 'Introduce la contraseña'; return; }
    loading = true;
    // Aquí se llamaría al backend. Por ahora solo simulamos.
    await new Promise(r => setTimeout(r, 600));
    console.log('login', { email, password });
    success = 'Inicio de sesión simulado. Conecta con tu API para autenticar.';
    loading = false;
  }

  async function submitRegister() {
    clearMessages();
    if (!validateEmail(email)) { error = 'Introduce un correo válido'; return; }
    if (password.length < 6) { error = 'La contraseña debe tener al menos 6 caracteres'; return; }
    if (password !== passwordConfirm) { error = 'Las contraseñas no coinciden'; return; }
    loading = true;
    await new Promise(r => setTimeout(r, 800));
    console.log('register', { email, password });
    success = 'Registro simulado. Envía los datos al backend para crear la cuenta.';
    loading = false;
  }

  async function submitRecover() {
    clearMessages();
    if (!validateEmail(email)) { error = 'Introduce un correo válido'; return; }
    loading = true;
    await new Promise(r => setTimeout(r, 600));
    console.log('recover', { email });
    success = 'Se ha enviado (simulado) un enlace de recuperación a tu correo.';
    loading = false;
  }

  // pequeña mejora: resetear campos cuando cambie modo
  $: if (mode) {
    // no sobrescribir mientras haya texto útil
  }

  onMount(() => {
    // placeholder: podríamos recuperar correo recordado
  });
  
  // Mostrar/ocultar header al hacer scroll
  let headerHidden = false;
  let lastScrollY = 0;
  const HIDE_THRESHOLD = 30; // px

  function handleWindowScroll() {
    const y = window.scrollY || document.documentElement.scrollTop;
    // si scroll mayor que umbral y mayor que último -> ocultar
    if (y > HIDE_THRESHOLD && y > lastScrollY) {
      headerHidden = true;
    } else if (y < lastScrollY) {
      headerHidden = false;
    }
    lastScrollY = y;
  }
</script>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<svelte:window on:scroll={handleWindowScroll} />

<main class="main">
 
  <header class="header" class:hidden={headerHidden}>
    <h1>xLow Calories</h1>
    <p>Tu asistente personal de nutrición</p>
  </header>

  <!-- Centramos el card usando flexbox en cards-container y eliminamos spacers innecesarios -->
  <nav class="bottom-nav">
    <div class="cards-container center-vertical-horizontal">
      <div class="scroll-spacer"></div>

      <div class="card">
        <h2 style="margin-bottom:0.5rem">{mode === 'login' ? 'Inicia sesión' : mode === 'register' ? 'Regístrate' : 'Recuperar contraseña'}</h2>

        {#if error}
          <p style="color: #b00020; margin: 0.5rem 0">{error}</p>
        {/if}
        {#if success}
          <p style="color: #007a00; margin: 0.5rem 0">{success}</p>
        {/if}

        <form class="card-form" on:submit|preventDefault={mode === 'login' ? submitLogin : mode === 'register' ? submitRegister : submitRecover}>
          <label for="email">Correo</label>
          <input id="email" name="email" type="email" bind:value={email} placeholder="tucorreo@ejemplo.com" />

          {#if mode !== 'recover'}
            <label for="password">Contraseña</label>
            <input id="password" name="password" type="password" bind:value={password} placeholder="Contraseña" />
          {/if}

          {#if mode === 'register'}
            <label for="passwordConfirm">Confirmar contraseña</label>
            <input id="passwordConfirm" name="passwordConfirm" type="password" bind:value={passwordConfirm} placeholder="Repite la contraseña" />
          {/if}

          <button class="primary-btn">
            {#if loading}
              Procesando...
            {:else}
              {mode === 'login' ? 'Entrar' : mode === 'register' ? 'Crear cuenta' : 'Enviar enlace'}
            {/if}
          </button>
        </form>
        <div class="card-actions">
          {#if mode !== 'login'}
            <button class="ghost-btn" on:click={() => { mode = 'login'; clearMessages(); }}>¿Ya tienes cuenta? Entrar</button>
          {/if}
          {#if mode !== 'register'}
            <button class="ghost-btn" on:click={() => { mode = 'register'; clearMessages(); }}>Crear cuenta</button>
          {/if}
          {#if mode !== 'recover'}
            <button class="ghost-btn" on:click={() => { mode = 'recover'; clearMessages(); }}>Recuperar contraseña</button>
          {/if}
        </div>
      </div>



    </div>
  </nav>
</main>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

  :global(html) {
    height:100%;
  }

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: linear-gradient(70deg, blue 0%, pink 100%);
    color: #f2f2f2;
    min-height: 100vh;
  }

  .bg {
    animation:slide 3s ease-in-out infinite alternate;
    background-image: linear-gradient(-60deg, #6c3 50%, #09f 50%);
    bottom:0;
    left:-50%;
    opacity:.5;
    position:fixed;
    right:-50%;
    top:0;
    z-index:-1;
  }

  .bg2 {
    animation-direction:alternate-reverse;
    animation-duration:4s;
  }

  .bg3 {
    animation-duration:5s;
  }

  /* .spacer eliminado (ya no se usa) */

  .main {
    max-width: 100%;
    margin: 0;
    padding: 2rem 1rem 0 1rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .header {
    text-align: center;
    margin-bottom: 2rem;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
    transition: opacity 200ms ease, transform 200ms ease;
  }

  .header.hidden {
    opacity: 0;
    transform: translateY(-12px);
    pointer-events: none;
  }

  .header h1 {
    font-family: 'Dancing Script', cursive;
    font-style: italic ;
    font-size: 5rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    color: #ffffffff;
  }

  .header p {
    font-size: 1rem;
    opacity: 0.9;
    margin: 0;
    color: #ffffffff;
  }

  /* .spacer removed (unused) */

  .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100vw;
    background: rgba(255, 255, 255, 0.1); /* Cambiado de white a semi-transparente para que el blur sea visible */
    box-shadow: 0 -2px 20px rgba(0, 0, 0, 0.08);
    border-radius: 2rem 2rem 0 0;
    transition: height 0.1s ease;
    overflow: hidden;
    z-index: 10;
    padding: 0;
    margin: 0;
  }

  @keyframes slideIn {
    from {
      transform: translateX(-100%);
    }
    to {
      transform: translateX(0);
    }
  }

  .cards-container {
    padding: 1rem 1rem 3rem 1rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    width: 100%;
    max-width: 200%;
    margin: 0;
    height: calc(150% - 100px);
    overflow-y: auto;
    overflow-x: hidden;
    scrollbar-width: thin;
    scrollbar-color: #ccc transparent;
    transition: opacity 0.2s ease, transform 0.2s ease;
  }

  /* centrar vertical y horizontalmente el contenido dentro de cards-container */
  .cards-container.center-vertical-horizontal {
    align-items: center;
    justify-content: center;
  }

  .scroll-spacer {
    height: 100px; /* Espacio para permitir scroll hacia arriba */
    width: 100%;
    flex-shrink: 0;
  }

  .cards-container::-webkit-scrollbar {
    width: 4px;
  }

  .cards-container::-webkit-scrollbar-track {
    background: transparent;
  }

  .cards-container::-webkit-scrollbar-thumb {
    background: #ccc;
    border-radius: 2px;
  }

  .cards-container::-webkit-scrollbar-thumb:hover {
    background: #999;
  }

 .card {
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
    background: rgba(255, 255, 255, 0.2); 
    border-radius: 1rem;
    padding: 3.2rem; /* aumentado para mayor altura interna */
    min-height: 420px; /* altura mínima mayor para que el card se vea más alto */
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
    margin: 0 auto;
    max-width: 400px;
    width: calc(100% - 2rem);
    flex-shrink: 0;
  }

  .card:hover{
    transform: translateY(-2px);
  }

  /* .icons removed (unused) */

  .card h2 {
    color: #333;
    font-size: 1.5rem;
    margin: 0 0 1rem 0;
  }

  .card p {
    color: #666;
    line-height: 1.6;
    margin: 0 0 0.5rem 0;
  }

  /* Mayor separación entre input/label dentro del card */
  .card label {
    display: block;
    text-align: left;
    margin-top: 1.25rem; /* aumentado */
    margin-bottom: 0.45rem; /* separación entre label e input */
  }

  .card input {
    width: 100%;
    padding: 0.75rem; /* un poco más de padding */
    border-radius: 0.6rem;
    border: 1px solid #ddd;
    margin-bottom: 0.6rem; /* espacio debajo del input */
    box-sizing: border-box;
  }

  /* Form dentro del card con gap uniforme */
  .card-form {
    display: flex;
    flex-direction: column;
    gap: 0.9rem; /* gap entre label/input y siguientes elementos */
    margin-top: 0.5rem;
  }

  .primary-btn {
    margin-top: 0.4rem;
    width: 100%;
    justify-content: center;
    background: #0066cc;
    color: white;
    border: none;
    padding: 0.9rem;
    border-radius: 0.6rem;
    cursor: pointer;
  }

  .card-actions {
    margin-top: 1rem;
    display: flex;
    gap: 0.75rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  .ghost-btn {
    background: none;
    border: 1px solid rgba(255,255,255,0.4);
    color: #fff;
    padding: 0.6rem 1rem;
    border-radius: 0.6rem;
    cursor: pointer;
    backdrop-filter: none;
  }

  /* .nav-item styles removed because component uses .primary-btn and .ghost-btn now */

  /* unused .nav-item span selectors removed */

  @keyframes slide {
    0% {
      transform:translateX(-25%);
    }
    100% {
      transform:translateX(25%);
    }
  }
</style>