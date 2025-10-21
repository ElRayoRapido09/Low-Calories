<script>
 
</script>

<main class="app">
  <header class="top">
    <a href="ajustes" class="back-btn" aria-label="Volver">‹</a>
    <h1>Premium</h1>
</header>

<section class="premium-msj">
    <h1>Premium</h1>
    <p>Simplifica tu progreso con el Plan Premium</p>
    <p>Accede a funciones exclusivas y contenido premium para mejorar tu experiencia.</p>
</section>

  <section class="card-plan">
    <h2 class="section-title">Plan individual</h2>
    <p>El Plan Individual te ofrece todas las funciones premium para un solo usuario, ideal para quienes buscan una experiencia personalizada y sin distracciones.</p>
    <h2 class="price">$9.99 / mes</h2>
    <button class="subscribe-btn" aria-label="Suscribirse al Plan Individual">Suscribirse Ahora</button>
  </section>
  <section class="card-plan">
    <h2 class="section-title">Plan Familiar</h2>
    <p>El Plan Familiar te permite compartir tu suscripción premium con hasta 5 miembros de tu familia, cada uno con su propio perfil y acceso a todas las funciones exclusivas.</p>
    <h2 class="price">$14.99 / mes</h2>
    <button class="subscribe-btn" aria-label="Suscribirse al Plan Familiar">Suscribirse Ahora</button>
  </section>

  <section class="card">
    <h2 class="section-title">Beneficios del Plan Individual</h2>
    <ul class="list">
        <li class="item">🚀 Acceso al escaner alimenticio</li>
      <li class="item">🍽️ Planes de comidas personalizados</li>
      <li class="item">📊 Seguimiento de progreso</li>
      <li class="item">🔔 Recordatorios y notificaciones personalizadas.</li>
      <li class="item">💬 Soporte 24/7</li>
    <li class="item">🌟 Sin anuncios</li>
    </ul>
  </section>

  <section class="card">
    <h2 class="section-title">Beneficios del Plan Familiar</h2>
    <ul class="list">
      <li class="item">👪 Hasta 5 perfiles individuales</li>
      <li class="item">🍽️ Planes de comidas personalizados para cada miembro</li>
      <li class="item">📊 Seguimiento de progreso individual</li>
      <li class="item">🔔 Recordatorios y notificaciones personalizadas para cada usuario</li>
      <li class="item">💬 Soporte 24/7</li>
      <li class="item">💰 Ahorro significativo en comparación con suscripciones individuales</li>
        <li class="item">🌟 Sin anuncios</li>
    </ul>

  <section class="card">
    <h2 class="section-title">Únete Premium</h2>
    <p>Disfruta de todos los beneficios del Plan Individual por solo $9.99 al mes o del Plan Familiar por solo $14.99 al mes.</p>
    <button class="subscribe-btn" aria-label="Suscribirse al Plan Familiar">Comienza tu prueba de 30 dias gratis</button>
  </section>
</main>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

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

 .premium-msj {
    background: linear-gradient(45deg, #FFD700, #FFA500); 
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 18px;
    border: 1px solid #e0e0e0;
    color: #000;
  }

  .premium-msj h1 {
    font-family: 'Dancing Script', cursive;
    font-style: italic;
    font-size: 3rem;
    font-weight: 900;
    margin: 0 0 0.5rem 0;
    color: #000; 
  }
  .top h1 {
    flex: 1;
    font-size: 20px;
    margin: 0;
    font-weight: 600;
    color: #000;
  }

  .top p {
    color: #666;
    margin: 0 0 8px 0;
    font-size: 14px;
  }

  .section-title {
    font-family: 'Dancing Script', cursive;
    font-style: italic;
    color: #000000;
    margin: 18px 0 8px;
    font-size: 30px; 
    font-weight: 900;
  }

  .card, .card-plan {
    background: #ffffff;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 18px;
    border: 1px solid #e0e0e0;
  }

  .card-plan {
    text-align: center;
  }

  .card-plan p {
    color: #000; /* Cambiado a negro para las p en .card-plan */
  }

  .price {
    font-size: 24px;
    font-weight: 700;
    color: #000000;
    margin: 12px 0;
  }

  .subscribe-btn {
    background: linear-gradient(90deg, #FFD700, #FFA500); /* Gradiente dorado horizontal */
    color: #000000;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    width: 100%;
    margin-top: 12px;
  }

  .subscribe-btn:hover {
    opacity: 0.9;
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
    border-bottom: 1px solid #f0f0f0;
    color: #000000;
  }

  .item:last-child {
    border-bottom: none;
  }

  @media (prefers-color-scheme: light) {
    :global(body) {
      background: #ffffff;
      color: #111;
    }
    .card, .card-plan {
      background: #fff;
      color: #222;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .top p, .section-title {
      color: #666;
    }
    .price {
      color: #000;
    }
    .item {
      color: #000;
    }
  }

 .back-btn {
    color: #000;
    text-decoration: none;
    font-size: 22px;
    padding: 6px;
  }

  .card p {
    color: #000; 
    }
</style>