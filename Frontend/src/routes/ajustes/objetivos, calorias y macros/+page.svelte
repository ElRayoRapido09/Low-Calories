<script>
  // no JavaScript necesario para el estilo
</script>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label="Volver">‹</a>
    <h1>Cuenta</h1>
  </header>

  <h2 class="section-title">Edad, Altura y Sexo</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <div class="left">
          <span class="icon">🔥</span>
          <span class="label">Objetivos y Calorias</span>
        </div>
        <div class="right">
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">🍎</span>
          <span class="label">Macros y Tipos de dietas</span>
        </div>
        <div class="right">
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">✨</span>
          <span class="label">Funciones Inteligentes</span>
        </div>
        <div class="right">
          <span class="chev">›</span>
        </div>
      </li>
    </ul>
  </section>
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
    background: linear-gradient(70deg, blue 0%, pink 100%);
    color: #f2f2f2;
    min-height: 100vh;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
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
  }  .app {
    max-width: 420px;
    margin: 0 auto;
    padding: 24px;
    min-height: 100vh;
  }


  .card--isolated {
    margin-top: 28px;   /* separación arriba */
    margin-bottom: 36px; /* separación abajo si quieres más espacio */
    background: rgb(255, 255, 255); /* ajuste: más opaco en modo claro si quieres */
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
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
    color: #cfcfcf;
    margin: 18px 0 8px;
    font-size: 14px;
    font-weight: 600;
  }

  .card {
    /* fondo semi-transparente para que el blur sea visible */
    background: rgba(245, 243, 243, 0.2);  /* ajustar opacidad según prefieras */
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    margin-bottom: 18px;

    /* fondo semi-transparente para que el blur sea visible */
    -webkit-backdrop-filter: blur(12px);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(233, 225, 225, 0.2);
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

  .label-red {
    flex: 1;
    font-size: 15px;
    color: #db0404;
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
    color: #ddd;
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

  @keyframes slide {
    0% {
      transform: translateX(-100%) translateY(-100%);
    }
    100% {
      transform: translateX(100%) translateY(100%);
    }
  }
</style>