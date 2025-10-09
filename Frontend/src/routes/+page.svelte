<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  

  function openCamera() {
    alert('aqui se abre la camara');
  }

  function goToObjetivos() {
    goto('/objetivos');
  }

  console.log("hola layo");

  let isMenuOpen = $state(false);
  let scrollY = $state(0);
  let cardsContainer = $state(null);
  let startY = $state(0);
  let isDragging = $state(false);
  let cardsScrollY = $state(0);
  let maxScroll = $state(0);

  let bottomNavHeight = $derived(cardsScrollY <= 50 ? Math.max(50 - (cardsScrollY * 2), 0) : Math.min(50 + ((cardsScrollY - 50) * 0.15), 100));
  let cardsOpacity = $derived(cardsScrollY <= 50 ? Math.max(1 - (cardsScrollY / 50), 0) : 1);
  let cardsTransform = $derived(cardsScrollY <= 50 ? -(cardsScrollY * 2) : 0);

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }

  function closeMenu() {
    isMenuOpen = false;
  }

  function handleTouchStart(e) {
    if (!cardsContainer) return;
    startY = e.touches[0].clientY;
    isDragging = true;
  }

  function handleTouchMove(e) {
    if (!isDragging || !cardsContainer) return;
    
    const currentY = e.touches[0].clientY;
    const deltaY = currentY - startY;
    
    if (deltaY > 50 && cardsContainer.scrollTop === 0) {
      e.preventDefault();
      cardsContainer.style.transform = `translateY(${Math.min(deltaY - 50, 100)}px)`;
    }
  }

  function handleTouchEnd(e) {
    if (!isDragging || !cardsContainer) return;
    
    const currentY = e.changedTouches[0].clientY;
    const deltaY = currentY - startY;

    cardsContainer.style.transform = 'translateY(0)';
    
    if (deltaY > 100 && cardsContainer.scrollTop === 0) {
      openCamera();
    }
    
    isDragging = false;
  }

  function handleScroll(e) {
    if (cardsContainer) {
      cardsScrollY = cardsContainer.scrollTop;
      maxScroll = cardsContainer.scrollHeight - cardsContainer.clientHeight;
      
      
      if (cardsScrollY <= 5) { 
        openCamera();
        
        setTimeout(() => {
          if (cardsContainer) {
            cardsContainer.scrollTop = 10;
          }
        }, 100);
      }
    }
  }
</script>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<svelte:window bind:scrollY />

<main>
  <header>
    <h1>Low Calories</h1>
    <p>Tu asistente personal de nutrición</p>
  </header>

  <div class="spacer"></div>

  <nav class="bottom-nav" style="height: {bottomNavHeight}vh;">
    <button class="menu-toggle" on:click={toggleMenu} class:active={isMenuOpen}>
      <span></span>
      <span></span>
      <span></span>
    </button>

    {#if isMenuOpen}
      <div class="menu-overlay" on:click={closeMenu}></div>
      <nav class="slide-menu">
        <a class="nav-item" href="/estadisticas" on:click={closeMenu}>
          <span>📊</span>
          <span>Estadísticas</span>
        </a>
        <a class="nav-item" href="/perfil" on:click={closeMenu}>
          <span>👤</span>
          <span>Perfil</span>
        </a>
        <a class="nav-item" href="/ajustes" on:click={closeMenu}>
          <span>⚙️</span>
          <span>Ajustes</span>
        </a>
      </nav>
    {/if}

    <div 
      class="cards-container"
      bind:this={cardsContainer}
      on:touchstart={handleTouchStart}
      on:touchmove={handleTouchMove}
      on:touchend={handleTouchEnd}
      on:scroll={handleScroll}
      style="opacity: {cardsOpacity}; transform: translateY({cardsTransform}px);"
    >
      <!-- Agregar un elemento espaciador al inicio para permitir scroll hacia arriba -->
      <div class="scroll-spacer"></div>

      <section class="card" on:click={handleCameraClick} role="button" tabindex="0">
        <div class="icons">
          📷
        </div>
        <h2>¿Qué vamos a comer hoy?</h2>
        <p>Escanea tu comida y conoce sus calorías al instante</p>
      </section>

      <section class="card-bot">
        <div class="icons">
          🤖
        </div>
        <h2>¿No sabes que comer?</h2>
        <p>Pregunta a nuestro asistente y él te ayudará</p>
      </section>

      <section class="card-bot">
        <div class="icons">
          🥑
        </div>
        <h2>Comidas</h2>
        <p>Guarda tus comidas favoritas</p>
      </section>
      
      <section class="card-bot">
        <div class="icons">
          📈
        </div>
        <h2>Historial</h2>
        <p>Revisa tu progreso diario</p>
      </section>

      <section class="card-bot" on:click={goToObjetivos} role="button" tabindex="0">
        <div class="icons">
          🎯
        </div>
        <h2>Objetivos</h2>
        <p>Establece y sigue tus metas</p>
      </section>

      <section class="card-bot">
        <div class="icons">
          💧
        </div>
        <h2>Hidratación</h2>
        <p>Mantén control de tu consumo de agua</p>
      </section>

      <section class="card-bot">
        <div class="icons">
          ⏰
        </div>
        <h2>Recordatorios</h2>
        <p>Programa tus comidas del día</p>
      </section>

      <section class="card-bot">
        <div class="icons">
          🍽️
        </div>
        <h2>Recetas</h2>
        <p>Descubre nuevas recetas saludables</p>
      </section>
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
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(70deg, blue 0%, pink 100%);
    min-height: 100vh;
    overflow: hidden; 
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

  main {
    max-width: 100%;
    margin: 0;
    padding: 2rem 1rem 0 1rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  header {
    text-align: center;
    margin-bottom: 2rem;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
  }

  header h1 {
    font-family: 'Dancing Script', cursive;
    font-style: italic ;
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    color: #ffffffff;
  }

  header p {
    font-size: 1rem;
    opacity: 0.9;
    margin: 0;
    color: #ffffffff;
  }

  .spacer {
    height: 50vh;
  
  }

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

  .menu-toggle {
    position: sticky;
    top: 1rem;
    left: 1rem;
    width: 30px;
    height: 30px;
    background: none;
    border: none;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    z-index: 1001;
    margin-bottom: 1rem;
  }

  .menu-toggle span {
    width: 100%;
    height: 3px;
    background: #333;
    transition: all 0.3s ease;
    transform-origin: center;
  }

  .menu-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }

  .menu-toggle.active span:nth-child(2) {
    opacity: 0;
  }

  .menu-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -6px);
  }

.menu-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.3); /* Más transparente para que el blur sea visible */
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
    z-index: 999;
  }

  .slide-menu {
    position: fixed;
    top: 0;
    left: 0;
    width: 250px;
    height: 100vh;
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
    background: rgba(255, 255, 255, 0.2); /* Igual que las card-bot */
    box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
    padding: 4rem 1rem 1rem 1rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    z-index: 1000;
    animation: slideIn 0.3s ease;
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
    max-width: 100%;
    margin: 0;
    height: calc(100% - 80px);
    overflow-y: auto;
    overflow-x: hidden;
    scrollbar-width: thin;
    scrollbar-color: #ccc transparent;
    transition: opacity 0.2s ease, transform 0.2s ease;
    -webkit-backdrop-filter: blur(5px);
    backdrop-filter: blur(5px);
    background: rgba(255, 255, 255, 0.3); /* Más transparente para mejor efecto */
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

 .card, .card-bot {
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
    background: rgba(255, 255, 255, 0.2); 
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
    margin: 0 auto;
    max-width: 400px;
    width: calc(100% - 2rem);
    flex-shrink: 0;
  }

  .card:hover, .card-bot:hover {
    transform: translateY(-2px);
  }

  .icons {
    width: 80px;
    height: 80px;
    background: #0066cc;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: white;
    margin: 0 auto 1.5rem auto;
  }

  .card h2, .card-bot h2 {
    color: #333;
    font-size: 1.5rem;
    margin: 0 0 1rem 0;
  }

  .card p, .card-bot p {
    color: #666;
    line-height: 1.5;
    margin: 0;
  }

  .nav-item {
    background: none;
    border: none;
    display: flex;
    align-items: center;
    gap: 1rem;
    color: #666;
    cursor: pointer;
    padding: 1rem;
    border-radius: 0.5rem;
    transition: all 0.2s;
    text-decoration: none;
  }

  .nav-item:hover {
    background: #f0f0f0;
    color: #0066cc;
  }

  .nav-item span:first-child {
    font-size: 1.5rem;
  }

  .nav-item span:last-child {
    font-size: 1rem;
    font-weight: 500;
  }

  @keyframes slide {
    0% {
      transform:translateX(-25%);
    }
    100% {
      transform:translateX(25%);
    }
  }
</style>