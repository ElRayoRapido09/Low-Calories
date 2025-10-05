<script>
  function handleCameraClick() {
    alert('aun no se poner la camara, solo puse la alerta xD');
  }
  console.log("hola layo");
  let isMenuOpen = false;
  let bottomNavElement;
  let scrollY = 0;

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }

  function closeMenu() {
    isMenuOpen = false;
  }

  $: bottomNavHeight = Math.min(50 + (scrollY * 0.8), 95);
</script>

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

    <div class="cards-container">
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
    </div>
  </nav>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(135deg, #000000ff 0%, #000000ff 100%);
    min-height: 100vh;
    overflow-x: hidden;
  }

  main {
    max-width: 100%;
    margin: 0;
    padding: 2rem 1rem 0 1rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  header {
    text-align: center;
    margin-bottom: 2rem;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
  }

  header h1 {
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
    background: white;
    box-shadow: 0 -2px 20px rgba(0, 0, 0, 0.08);
    border-radius: 2rem 2rem 0 0;
    transition: height 0.3s ease;
    overflow-y: auto;
    overflow-x: hidden;
    z-index: 10;
    padding: 0;
    margin: 0;
    scrollbar-width: thin;
    scrollbar-color: #ccc transparent;
  }

  .bottom-nav::-webkit-scrollbar {
    width: 4px;
  }

  .bottom-nav::-webkit-scrollbar-track {
    background: transparent;
  }

  .bottom-nav::-webkit-scrollbar-thumb {
    background: #ccc;
    border-radius: 2px;
  }

  .bottom-nav::-webkit-scrollbar-thumb:hover {
    background: #999;
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
    background: rgba(0, 0, 0, 0.5);
    z-index: 999;
  }

  .slide-menu {
    position: fixed;
    top: 0;
    left: 0;
    width: 250px;
    height: 100vh;
    background: white;
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
    min-height: 100%;
  }

  .card, .card-bot {
    background: white;
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
</style>