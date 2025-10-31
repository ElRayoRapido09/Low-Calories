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
    <h1>Low Calories</h1>
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
  /* Keep same font stack as app; use the project's white + blue aesthetic */
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

  :global(html), :global(body) {
    height: 100%;
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: #ffffff; /* consistent app background */
    color: #222;
  }

  /* Remove animated blobs visually but keep bg layers for potential decorative use */
  .bg, .bg2, .bg3 { display: none; }

  .main {
    max-width: 100%;
    margin: 0;
    padding: 1.5rem 1rem 0 1rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: hidden;
  }

  .header {
    text-align: center;
    margin-bottom: 1rem;
    width: 100%;
    max-width: 420px;
    transition: opacity 200ms ease, transform 200ms ease;
  }

  .header.hidden { opacity: 0; transform: translateY(-8px); pointer-events: none; }

  .header h1 {
    font-family: 'Dancing Script', cursive;
    font-size: 2.2rem;
    margin: 0;
    color: #000;
    line-height: 1;
  }

  .header p { margin: 0.25rem 0 0; color: #666; font-size: 0.95rem; }

  /* Container that previously acted as bottom-nav -> keep simple centered column */
  .bottom-nav {
    position: relative;
    width: 100%;
    max-width: 480px;
    margin: 0;
    padding: 0;
    z-index: 10;
    display: flex;
    justify-content: center;
  }

  .cards-container {
    padding: 0 0 2.5rem 0;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    width: 100%;
    margin: 0 auto;
    overflow-y: visible;
  }

  .cards-container.center-vertical-horizontal { align-items: center; }

  .scroll-spacer { height: 20px; }

  /* Clean white card with subtle shadow - mobile first */
  .card {
    background: #ffffff;
    border-radius: 14px;
    padding: 1.3rem;
    box-shadow: 0 6px 20px rgba(33,33,33,0.08);
    border: 1px solid #eef1f4;
    width: 100%;
    max-width: 420px;
    box-sizing: border-box;
    transition: transform 0.15s ease;
  }

  .card:hover { transform: translateY(-3px); }

  .card h2 { color: #0b2b40; font-size: 1.25rem; margin: 0 0 0.5rem 0; }
  .card p { color: #666; margin: 0 0 0.5rem 0; }

  .card-form { display: flex; flex-direction: column; gap: 0.6rem; margin-top: 0.25rem; }

  .card label { display:block; font-size: 0.85rem; color: #333; margin-top: 0.6rem; margin-bottom: 0.25rem; }

  .card input {
    width: 100%;
    padding: 0.75rem;
    border-radius: 10px;
    border: 1px solid #e6e9ee;
    background: #fff;
    box-sizing: border-box;
    font-size: 0.95rem;
    color: #1f2933;
  }

  .primary-btn {
    margin-top: 0.6rem;
    width: 100%;
    background: #005bb5; /* project blue */
    color: #fff;
    border: none;
    padding: 0.95rem;
    border-radius: 10px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 6px 18px rgba(0,91,181,0.12);
  }

  .primary-btn:active { transform: scale(0.995); }

  .card-actions {
    margin-top: 0.75rem;
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  .ghost-btn {
    background: transparent;
    border: 1px solid #d7dbe0;
    color: #005bb5;
    padding: 0.55rem 0.9rem;
    border-radius: 10px;
    cursor: pointer;
    font-weight: 600;
  }

  /* Error / success messages inside card */
  .card p[style*="color: #b00020"] { color: #b00020; background: #fff5f6; padding: 0.45rem; border-radius: 8px; }
  .card p[style*="color: #007a00"] { color: #0a7a07; background: #f3fff3; padding: 0.45rem; border-radius: 8px; }

  /* Small helper adjustments */
  @media (min-width: 520px) {
    .card { padding: 1.6rem; }
    .header h1 { font-size: 2.6rem; }
  }

  @media (max-width: 380px) {
    .card { padding: 1rem; border-radius: 12px; }
    .header h1 { font-size: 1.9rem; }
    .primary-btn { padding: 0.85rem; }
  }

</style>