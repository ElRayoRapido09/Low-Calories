<script>
  // no JavaScript necesario para el estilo
</script>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label="Volver">‹</a>
    <h1>Interfaz</h1>
  </header>

  <h2 class="section-title">Idioma</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <div class="left">
          <span class="icon">🌐</span>
          <span class="label">Lenguaje de interfaz</span>
        </div>
        <div class="right">
          <span class="value">Español</span>
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">📚</span>
          <span class="label">Lenguaje de base de datos</span>
        </div>
        <div class="right">
          <span class="value">Español</span>
          <span class="chev">›</span>
        </div>
      </li>
    </ul>
  </section>

  <h2 class="section-title">Unidades</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <div class="left">
          <span class="icon">⚖️</span>
          <span class="label">Unidad de masa/volumen</span>
        </div>
        <div class="right">
          <span class="value">g / kg / ml</span>
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">📏</span>
          <span class="label">Unidad de longitud</span>
        </div>
        <div class="right">
          <span class="value">cm</span>
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">⚡</span>
          <span class="label">Unidad de energía</span>
        </div>
        <div class="right">
          <span class="value">kcal</span>
          <span class="chev">›</span>
        </div>
      </li>
    </ul>
  </section>

  <div class="search">
    <span class="search-icon">🔍</span>
    <input type="search" placeholder="Busca ajustes, funciones, artículos..." aria-label="buscar ajustes">
  </div>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: linear-gradient(70deg, blue 0%, pink 100%);
    color: #f2f2f2;
    min-height: 100vh;
  }

  .app {
    max-width: 420px;
    margin: 0 auto;
    padding: 24px;
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
    text-align: center;
  }

  .section-title {
    color: #ffffff;
    margin: 18px 0 8px;
    font-size: 14px;
    font-weight: 600;
  }

  .card {
    /* fondo semi-transparente para que el blur sea visible */
    background: none;  /* ajustar opacidad según prefieras */
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    margin-bottom: 18px;

    background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);

  }


  .list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  /* Cada fila como tarjeta redondeada (separadas entre sí) */
  .item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    background: none; /* ajuste: más opaco en modo claro si quieres */
  }

  .item:last-child {
    margin-bottom: 0;
  }

  .left {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
  }

  .right {
    display: flex;
    align-items: center;
    gap: 8px;
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
    flex-shrink: 0;
  }

  .label {
    flex: 1;
    font-size: 15px;
    color: #000000;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .value {
    color: #000000;
    font-size: 14px;
    margin-right: 6px;
  }

  .chev {
    color: #9b9b9b;
    font-size: 18px;
  }

  /* Switch estilo móvil (amarillo cuando está activo) */
  .search {
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    bottom: 18px;
    width: calc(100% - 48px);
    max-width: 420px;
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
      background: linear-gradient(180deg,#ffffff,#f7f7fb);
      color: #111;
    }
    .item, .search { background: #fff; color: #222; box-shadow: 0 8px 26px rgba(10,10,10,0.06); border: 1px solid rgba(10,10,10,0.04); }
    .icon { color: #111; background: linear-gradient(180deg,#0066cc,#2077cd); }
    .value { color: #666; }
  }
</style>