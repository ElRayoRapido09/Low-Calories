<script>
  // no JavaScript necesario para el estilo
</script>

<main class="app">
  <header class="top">
    <a href="/" class="back-btn" aria-label="Volver">‹</a>
    <h1>Ajustes</h1>
    <img class="avatar" alt="Perfil" src="src/lib/assets/kk.jpg"/>
  </header>

  <h2 class="section-title">Acceso rápido</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <span class="icon">✨</span>
        <span class="label">Planificador Automático</span>
        <label class="switch">
          <input type="checkbox" aria-label="activar planificador">
          <span class="slider"></span>
        </label>
      </li>

      <li>
        <a class="item" href="/ajustes/planificador_de_comida" aria-label="Abrir Interfaz">
          <span class="icon">📅</span>
          <span class="label">Planificador de Comidas</span>
          <span class="chev">›</span>
        </a>
      </li>

      <li>
        <a class="item" href="/ajustes/lista de compras" aria-label="Abrir Interfaz">
          <span class="icon">🛒</span>
          <span class="label">Lista de Compras</span>
          <span class="chev">›</span>
        </a>
      </li>

      <li>
        <a class="item" href="/ajustes/ayuno" aria-label="Abrir Interfaz">
          <span class="icon">⏱️</span>
          <span class="label">Ayuno</span>
          <span class="chev">›</span>
        </a>
      </li>
    </ul>
  </section>

  <h2 class="section-title">Configuración</h2>
  <section class="card">
    <ul class="list">
      <li>
        <a class="item" href="/ajustes/objetivos, calorias y macros" aria-label="Abrir Interfaz">
          <span class="icon">🔥</span>
          <span class="label">Objetivo, Calorías y Macros</span>
          <span class="chev">›</span>
        </a>
      </li>
      <li class="item"><span class="icon">🍎</span><span class="label">Plan de Comidas y Alimentos</span><span class="chev">›</span></li>
      <li>
        <a class="item" href="/objetivos" aria-label="Abrir Interfaz">
          <span class="icon">🔁</span>
          <span class="label">Rehacer Plan</span>
          <span class="chev">›</span>
        </a>
      </li>
      <li class="item"><span class="icon">🔔</span><span class="label">Recordatorios</span><span class="chev">›</span></li>
      <li class="item"><span class="icon">💛</span><span class="label">Sincronizar Health Connect</span><span class="chev">›</span></li>
      <li>
        <a class="item" href="/ajustes/interfaz" aria-label="Abrir Interfaz">
          <span class="icon">🎨</span>
          <span class="label">Interfaz</span>
          <span class="chev">›</span>
        </a>
      </li>
      <a class="item" href="/premium" aria-label="Abrir Plan Familiar">
        <span class="icon">👪</span>
        <span class="label">Plan Familiar</span>
        <span class="chev">›</span>
      </a>
      <li>
        <a class="item" href="/ajustes/cuenta" aria-label="Abrir cuenta">
          <span class="icon">👤</span>
          <span class="label">Cuenta</span>
          <span class="chev">›</span>
        </a>
      </li>
    </ul>
  </section>

  <div class="search">
    <span class="search-icon">🔍</span>
    <input type="search" placeholder="Busca ajustes, funciones, artículos..." aria-label="buscar ajustes">
  </div>
</main>


<style>
  :global(html) {
    height: auto;
    min-height: 100%;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: #ffffff;
    color: #333;
    min-height: 100vh;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }
  
  .app {
    max-width: 420px;
    margin: 0 auto;
    padding: 24px;
    min-height: 100vh;
  }

  .top {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 18px;
  }

  .back-btn {
    color: #fff;
    text-decoration: none;
    font-size: 22px;
    padding: 6px;
  }

  .top h1 {
    flex: 1;
    font-size: 20px;
    margin: 0;
    font-weight: 600;
  }

  .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    border: 1px solid rgba(255,255,255,0.06);
  }

  .section-title {
    color: #666;
    margin: 18px 0 8px;
    font-size: 14px;
    font-weight: 600;
  }

  .card {
    background: #ffffff;
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 18px;
    border: 1px solid #e0e0e0;
  }

  .list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.03);
  }

  .item:last-child {
    border-bottom: none;
  }

  .icon {
    width: 44px;
    height: 44px;
    min-width: 44px;
    border-radius: 10px;
    background: linear-gradient(180deg,#0066cc,#2077cd);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: #111;
    font-size: 18px;
  }

  .label {
    flex: 1;
    font-size: 15px;
    color: #000000;
  }

  .chev {
    color: #9b9b9b;
    font-size: 20px;
    padding-left: 8px;
  }
  /* Toggle switch estilo móvil */
  .switch {
    display: inline-block;
    width: 44px;
    height: 24px;
    position: relative;
    margin-left: 8px;
  }
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  .slider {
    position: absolute;
    cursor: pointer;
    inset: 0;
    background: rgba(0, 0, 0, 0.241);
    border-radius: 999px;
  }
  .slider::after {
    content: "";
    position: absolute;
    left: 4px;
    top: 4px;
    width: 16px;
    height: 16px;
    background: #000000;
    border-radius: 50%;
    transition: transform 0.18s;
  }
  .switch input:checked + .slider {
    background: linear-gradient(90deg,#0066cc,#0066cc71);
  }
  .switch input:checked + .slider::after {
    transform: translateX(20px);
  }

  .search {
    position: fixed;
    left: 24px;
    right: 24px;
    bottom: 18px;
    max-width: 420px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 10px;

    background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
    
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    border: 1px solid rgba(255,255,255,0.03);
  }

  .search input {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: #ffffff;
    font-size: 14px;
  }

  .search-icon {
    color: #0066cc;
    font-size: 18px;
  }

   @media (prefers-color-scheme: light) {
    :global(body) {
      background: linear-gradient(-45deg, #FFD700 0%, #FFA500 50%, #FFFFFF 50%, #FFFFFF 100%);
      background-attachment: fixed; /* Fondo estático */
      color: #111;
    }
    .card, .search { background: rgba(255,255,255,0.9); color: #222; box-shadow: 0 8px 26px rgba(10,10,10,0.06); }
    .icon { color: #111; }
    .label { color: #000; }
  }
  

  

  @keyframes shimmer {
    0% {
      transform: translateX(100%);
    }
    100% {
      transform: translateX(-100%);
    }
  }
</style>