<script>

</script>

<main>
  <header>
    <h1>Low Calories</h1>
    <p>Tu asistente personal de nutrición</p>
  </header>

  <section class="card" on:click={handleCameraClick} role="button" tabindex="0"> falta poner la camara
    <div class="icons">
      📷
    </div>
    <h2>¿Qué vamos a comer hoy?</h2>
    <p>Escanea tu comida y conoce sus calorías al instante</p>
  </section>

  <section class = "card-bot">
    <div class = "icons">
    🤖
    </div>
    <h2>¿No sabes que comer?</h2>
    <p>pregunta a nuestro asistente y el te ayudara</p>
  </section>

  <nav class="bottom-nav">
    <a class="nav-item" href = "../estadisticas/estadisticas.svelte">
      <span>📊</span>
      <span>Estadísticas</span>
    </a>
    <a class="nav-item" href = "/perfil.svelte">
      <span>👤</span>
      <span>Perfil</span>
    </a>
    <button class="nav-item" href = "../ajustes/ajustes.svelte">
      <span>⚙️</span>
      <span>Ajustes</span>
    </button>
  </nav>
</main>
