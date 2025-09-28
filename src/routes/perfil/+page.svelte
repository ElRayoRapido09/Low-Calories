<script>

</script>

<main>
  <header class = "back">
    <a href ="/" class = "back-btn" aria-label = "Volver">
    &#8592;
    </a>
    <h1>Mi Perfil</h1>
  </header>

  <section class="card_p" on:click={handleCameraClick} role="button" tabindex="0"> falta poner la camara
    <div class="icons">
      👤
    </div>
    <h2>Kevin Herrera</h2>
    <p>soy una vrga</p>
  </section>

  <section class = "card-meta">
    <div class = "icons">
    🏁
    </div>
    <h2>1800</h2>
    <p>Meta diaria</p>
  </section>

  <section class = "card-act">
    <div class = "icons">
    ⚡
    </div>
    <h2>7</h2>
    <p>Dias activos</p>
  </section>

  <section class = "card-inf_P">
    <h2>Informacion Personal</h2>
    <div class = "columns">
      <div>
        <p>Edad</p>
        <p>Altura</p>
        <p>Peso actual</p>
        <p>Objetivo</p>
      </div>
      <div> 
        <p>28 anos</p>
        <p>165 cm</p>
        <p>62 kg</p>
        <p>mantener peso</p>
      </div>
    </div>
  </section>

  <section class = "card_Prog">
    <div class = "icons">
    🗓
    </div>
    <h2>Progreso semanal</h2>
    <div class = "columns">
      <div>
        <p>Promedio diario</p>
      </div>
      <div>
        <p>1,650 Kcal</p>
      </div>
    </div>
    <div class = "progress-container">
      <div class = "progress-header">
        <span>Dias completados</span>
        <span><b>5/7</b></span>
      </div>
      <div class = "progress-bar"> 
        <div class = "progres-fill" style = "width: 71%;"></div>
      </div>
    </div>
  </section>
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
.card_p {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 90px;  //esto es para que se haga un espacio entre la section y el button
    cursor: pointer;
    transition: transform 0.2s;
    margin-top: 0.5rem; // esta es para separar ambas section
  }

.card_p:hover {
    transform: translateY(-2px);
  }

  .card-meta {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 90px;  //esto es para que se haga un espacio entre la section y el button
    cursor: pointer;
    transition: transform 0.2s;
    margin-top: 0.5rem; // esta es para separar ambas section
  }

.card-meta:hover {
    transform: translateY(-2px);
  }
  .card-meta {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 90px;  //esto es para que se haga un espacio entre la section y el button
    cursor: pointer;
    transition: transform 0.2s;
    margin-top: 0.5rem; // esta es para separar ambas section
  }

.card-meta:hover {
    transform: translateY(-2px);
  }
  .card-act {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 90px;  //esto es para que se haga un espacio entre la section y el button
    cursor: pointer;
    transition: transform 0.2s;
    margin-top: 0.5rem; // esta es para separar ambas section
  }

.card-act:hover {
    transform: translateY(-2px);
  }

  .card-inf_P {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 90px;  //esto es para que se haga un espacio entre la section y el button
    cursor: pointer;
    transition: transform 0.2s;
    margin-top: 0.5rem; // esta es para separar ambas section
  }

.card-inf_P:hover {
    transform: translateY(-2px);
  }

  .card_Prog {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 90px;  //esto es para que se haga un espacio entre la section y el button
    cursor: pointer;
    transition: transform 0.2s;
    margin-top: 0.5rem; // esta es para separar ambas section
  }

.card_Prog:hover {
    transform: translateY(-2px);
  }

.card-inf_P .columns {
    display: flex;
    gap: 2rem;
  }
  .card-inf_P .columns > div {
    flex: 1;
  }
  .progress-container {
    margin-top: 1rem;
  }
  .progress-header {
    display: flex;
    justify-content: space-between;
    font-size: 0.95rem;
    margin-bottom: 0.3rem;
  }
  .progress-bar {
    width: 100%;
    height: 10px;
    background: #e0ecf7;
    border-radius: 6px;
    overflow: hidden;
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #0a3d62, #38ada9);
    width: 71%; /* 5/7 ≈ 71% */
    border-radius: 6px 0 0 6px;
    transition: width 0.3s;
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
  .back {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 3rem;
  }
  .back-btn {
    font-size: 1.5rem;
    color: #222;
    text-decoration: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0 0.5rem 0 0;
    line-height: 1;
  }
  .header-back h1 {
    font-size: 2rem;
    font-weight: 700;
    margin: 0;
    color: #333;
  }
</style>
