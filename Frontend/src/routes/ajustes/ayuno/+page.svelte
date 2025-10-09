<script>
  // sin JS adicional por ahora
</script>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label="Volver">‹</a>
    <h1>Elige un Ayuno</h1>
  </header>

  <section class="card-plan popular">
    <div class="left">
      <div class="title">16:8</div>
      <p class="desc">Ayunar 16 horas y comer dentro de una ventana de 8 horas. Ideal para perder peso y mejorar la salud metabólica.</p>
    </div>
  </section>

  <section class="card-plan">
    <div class="title">14:10</div>
    <p class="desc">Ayuno moderado: 14 horas de ayuno y 10 horas para comer. Adecuado para principiantes.</p>
  </section>

  <section class="card-plan">
    <div class="title">12:12</div>
    <p class="desc">Periodos iguales de 12 horas. Perfecto si empiezas en el ayuno o buscas bajo impacto en tu rutina.</p>
  </section>

  <section class="card-plan">
    <div class="title">Personalizado</div>
    <p class="desc">Ajusta tu horario según tu estilo de vida y objetivos. Ideal para usuarios avanzados o necesidades especiales.</p>
  </section>

  <div style="height:40px"></div>
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

  .bg { /* degradado sutil animado como en tu tema */
    animation: slide 6s ease-in-out infinite alternate;
    background-image: linear-gradient(-60deg, rgba(25,25,40,0.5) 0%, rgba(10,10,20,0.2) 100%);
    position: fixed;
    inset: 0;
    z-index: -1;
    opacity: 0.6;
  }

  .bg2 { animation-duration: 8s; }

  .bg3 { animation-duration: 10s; }

  .app {
    max-width: 420px;
    margin: 0 auto;
    padding: 20px;
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
    font-size: 26px;
    padding: 6px;
    opacity: 0.95;
  }

  .top h1 {
    flex: 1;
    font-size: 28px;
    margin: 0;
    font-weight: 800;
    letter-spacing: -0.5px;
  }

  .card-plan {
    background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    border: 1px solid rgba(255,255,255,0.03);
    display: flex;
    flex-direction: column;
    gap: 8px;
    position: relative;
  }

  .card-plan.popular {
    padding-right: 100px;
  }

  .card-plan .title {
    font-size: 20px;
    font-weight: 800;
    color: #fff;
    margin-bottom: 6px;
  }

  .card-plan .desc {
    font-size: 14px;
    color: rgba(255,255,255,0.85);
    line-height: 1.45;
    margin: 0;
  }

  .badge {
    position: absolute;
    top: 14px;
    right: 14px;
    background: #f2c94c;
    color: #000;
    font-weight: 700;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.35);
  }

  /* apariencia de tarjetas grandes como en la imagen */
  @media (min-width: 360px) {
    .card-plan { padding: 20px; }
    .card-plan .title { font-size: 22px; }
  }

  /* esquema claro opcional */
  @media (prefers-color-scheme: light) {
    :global(body) { background: linear-gradient(180deg,#f7f7fb,#ffffff); color: #111; }
    .card-plan { background: #1f2937; color: #fff; }
    .badge { background: #ffd54f; }
  }

  @keyframes slide {
    0% { transform: translateX(-20%); }
    100% { transform: translateX(20%); }
  }
</style>