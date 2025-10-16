<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<main>
    <header>
      <header class="header-back">
          <a href="/" class="back-btn" aria-label="Volver">‹</a>
          <h1>Estadísticas</h1>
      </header>
        <p>Visualiza tus progresos y logros</p>
    </header>
  <section class="card-calorias">
      <div class = "icons">
      📈
      </div>
    <h2>Progreso Semanal</h2>
    <p>Aquí puedes ver tu progreso semanal en términos de calorías consumidas y quemadas.</p>
    <div class="progress-container">
      <div class="progress-header">
        <span>Este es el progreso de las calorias consumidas</span>
        <span><b>1240/1800</b></span>
      </div>
      <div class="progress-bar">
        <div class="progress-fill" style="width: 71%;"></div>
      </div>
    </div>

    <!-- Aquí podrías agregar gráficos o tablas para mostrar las estadísticas -->
  </section>
  <section class="card-macronutrientes">
    <h2>Macronutrientes de hoy</h2>
    <p>Has alcanzado 5 metas de alimentación saludable este mes. ¡Sigue así!</p>
    <p>Proteínas: 30g</p>
    <div class="progress-bar-container">
    <div class="progress-bar" style="width: {onprogress}%"></div>
  </div>

    <p>Carbohidratos: 50g</p>
    <div class="progress-bar-container">
    <div class="progress-bar" style="width: {onprogress}%"></div>
  </div>

    <p>Grasas: 20g</p>
    <div class="progress-bar-container">
    <div class="progress-bar" style="width: {onprogress}%"></div>
  </div>
  </section>
  <section class="card-semana">
    <div class="icons">
      📅
    </div> 
    <h2>Esta semana</h2>
    <div class="semana-bar">
      {#each [
        { dia: 'L', kcal: 1650 },
        { dia: 'M', kcal: 1720 },
        { dia: 'M', kcal: 1580 },
        { dia: 'J', kcal: 1890 },
        { dia: 'V', kcal: 1640 },
        { dia: 'S', kcal: 1200 },
        { dia: 'D', kcal: null }
      ] as d}
        <div class="dia">
          <div class="barra" style="opacity: {d.kcal ? 1 : 0.3}; background: linear-gradient(180deg, #0a3d62 70%, #38ada9 100%);">
            <!-- Puedes ajustar el alto según el valor si lo deseas -->
          </div>
          <div class="letra">{d.dia}</div>
          <div class="valor">{d.kcal ?? '-'}</div>
        </div>
      {/each}
    </div>
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
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
      background: linear-gradient(135deg, #ffffffff 0%, #f9f8feff 100%);
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
    }

    main {
      max-width: 400px;
      margin: 0 auto;
      padding: 2rem 1rem;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }

    header {
      text-align: center;
      margin-bottom: 3rem;
    }

    header h1 {
      font-size: 2rem;
      font-weight: 700;
      margin: 0 0 0.5rem 0;
      color: #ffffff;
    }

    header p {
      font-size: 1rem;
      opacity: 0.9;
      margin: 0;
      color: #ffffff;
      }
      .icons{
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
      .card-calorias{
          border-radius: 1rem;
          padding: 2rem;
          text-align: center;
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
          margin-bottom: 24px;  
          cursor: pointer;
          transition: transform 0.2s;
          margin-top: 0rem; 
          background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
          -webkit-backdrop-filter: blur(15px);
          backdrop-filter: blur(15px);
      }
      .card-calorias:hover {
          transform: translateY(-2px);
      }
      .card-macronutrientes{
          border-radius: 1rem;
          padding: 2rem;
          text-align: center;
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
          margin-bottom: 24px;;
          cursor: pointer;
          transition: transform 0.2s;
          margin-top: 0rem;
          background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
          -webkit-backdrop-filter: blur(15px);
          backdrop-filter: blur(15px);
      }
      .card-macronutrientes:hover {
          transform: translateY(-2px);
      }
      .card-semana{
          border-radius: 1rem;
          padding: 2rem;
          text-align: center;
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
          margin-bottom: 24px;
          cursor: pointer;
          transition: transform 0.2s;
          margin-top: 0rem;
          background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
          -webkit-backdrop-filter: blur(15px);
          backdrop-filter: blur(15px);
      }
      .card-semana:hover {
          transform: translateY(-2px);
      }
      

      .card-calorias h2 {
      color: #333;
      font-size: 1.5rem;
      margin: 0 0 1rem 0;
    }

    .card-calorias p {
      color: #666;
      line-height: 1.5;
      margin: 0;
    }
      .card-macronutrientes h2 {
          color: #333;
          font-size: 1.5rem;
          margin: 0 0 1rem 0;
      }
      .card-macronutrientes p {
          color: #666;
          line-height: 1.5;
          margin: 0;
      }
      .card-semana h2 {
          color: #333;
          font-size: 1.5rem;
          margin: 0 0 1rem 0;
      }
    
    .header-back {
      display: flex;
      align-items: left;
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
      color: #ffffff;
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
    .semana-bar {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin: 1.5rem 0 0.5rem 0;
    gap: 0.5rem;
  }
  .dia {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 40px;
  }
  .barra {
    width: 100%;
    height: 48px;
    border-radius: 16px;
    background: #e0ecf7;
    margin-bottom: 0.3rem;
    transition: opacity 0.3s;
  }
  .letra {
    font-size: 0.95rem;
    font-weight: 600;
    color: #333;
    margin-bottom: 0.2rem;
  }
  .valor {
    font-size: 0.95rem;
    color: #38ada9;
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