<script>
  function handleCameraClick() {
    alert('aun no se poner la camara, solo puse la alerta xD');
  }
  console.log("hola layo");
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
    <a class="nav-item" href="/estadisticas">
      <span>📊</span>
      <span>Estadísticas</span>
    </a>
    <a class="nav-item" href="/perfil">
      <span>👤</span>
      <span>Perfil</span>
    </a>
    <a class="nav-item" href="/ajustes">
      <span>⚙️</span>
      <span>Ajustes</span>
    </a>
  </nav>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(135deg, #ffffffff 0%, #f9f8feff 100%);
    min-height: 100vh;
  }

  main {
    max-width: 400px;
    margin: 0 auto;
    padding: 2rem 1rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  header {
    text-align: center;
    margin-bottom: 3rem;
  }

  header h1 {
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    color: #333;
  }

  header p {
    font-size: 1rem;
    opacity: 0.9;
    margin: 0;
    color: #666;
  }

  .card {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: auto;
    cursor: pointer;
    transition: transform 0.2s;
  }

  .card:hover {
    transform: translateY(-2px);
  }

  .card-bot {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 90px;  
    cursor: pointer;
    transition: transform 0.2s;
    margin-top: 2rem; 
  }

.card-bot:hover {
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


  .card h2 {
    color: #333;
    font-size: 1.5rem;
    margin: 0 0 1rem 0;
  }

  .card p {
    color: #666;
    line-height: 1.5;
    margin: 0;
  }

  .card-bot h2 {
    color: #333;
    font-size: 1.5rem;
    margin: 0 0 1rem 0;
  }

  .card-bot p {
    color: #666;
    line-height: 1.5;
    margin: 0;
  }

  .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100vw;
    height: auto;
    z-index: 10;
    display: flex;
    flex-direction: row;      
    justify-content: space-around;
    align-items: center;
    background: white;
    box-shadow: 0 -2px 20px rgba(0, 0, 0, 0.08);
    padding: 0.01rem 0;
    border-radius: 1.5rem 1.5rem 0 0;  
    text-direction: none;
  }
 

  .nav-item {
    background: none;
    border: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    color: #666;
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 0.5rem;
    transition: all 0.2s;
  }

  .nav-item:hover {
    background: #f0f0f0;
    color: #0066cc;
  }

  .nav-item span:first-child {
    font-size: 1.5rem;
  }

  .nav-item span:last-child {
    font-size: 0.8rem;
    font-weight: 500;
  }
</style>