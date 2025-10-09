<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let currentView = 1; 

  function goToHome() {
    goto('/');
  }

  function nextView() {
    if (currentView < 10) {
      currentView++;
    }
  }

  function prevView() {
    if (currentView > 1) {
      currentView--;
    }
  }

  let showGenderModal = false;
  let showAgeModal = false;
  let showWeightModal = false;
  let showTargetWeightModal = false;
  let showHeightModal = false;
  let carouselIndex = 0;

  let gender = '';
  let age = '';
  let weight = '';
  let height = '';
  let targetWeight = '';
  let weightUnit = 'kg';
  let heightUnit = 'cm';
  let showSpeedModal = false;
  let selectedSpeed = 'recomendada';
</script>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<main class="app">
  <header class="top">
    <a href="/" class="back-btn" aria-label="Volver">‹</a>
    <h1>Objetivos</h1>
  </header>

  
  {#if currentView === 1}
    <section class="card">
      <h2>¿Cuál es tu objetivo?</h2>
      <p>Calcularemos tus calorías necesarias para lograrlo.</p>
      <div class="lista">
        <label class="opcion">
          <input type="radio" name="objetivo" value="perder" />
          <span class="checkmark"></span>
          Perder grasa
        </label>
        <label class="opcion">
          <input type="radio" name="objetivo" value="mantener" />
          <span class="checkmark"></span>
          Ganar músculo
        </label>
        <label class="opcion">
          <input type="radio" name="objetivo" value="ganar" />
          <span class="checkmark"></span>
          Mantener peso
        </label>
      </div>
      <div class="nav-buttons">
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}

  
  {#if currentView === 2}
    <section class="card">
      <h2>Excelente
      </h2>
      <p>Ahora el primer paso es descubrir cuantas calorías necesitas diariamente.</p>
      <p>Necesitaremos saber tu edad, sexo, peso y altura.</p>
    <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}

  
  {#if currentView === 3}
    <section class="card">
    <h2>Cuéntanos sobre ti</h2>
    <p>Esta información nos ayudará a calcular tus calorías objetivo.</p>
    <div class="info-list">
      <div class="info-item">
        <span class="info-icon">👤</span>
        <span class="info-label">Sexo</span>
        <button class="info-select" on:click={() => showGenderModal = true}>
          {gender ? (gender === 'male' ? 'Hombre' : 'Mujer') : 'Seleccionar'}
          <span class="chev">›</span>
        </button>
      </div>
      <div class="info-item">
        <span class="info-icon">🎂</span>
        <span class="info-label">Edad</span>
        <button class="info-select" on:click={() => showAgeModal = true}>
          {age ? `${age} años` : 'Seleccionar'}
          <span class="chev">›</span>
        </button>
      </div>
      <div class="info-item">
        <span class="info-icon">⚖️</span>
        <span class="info-label">Peso</span>
        <button class="info-select" on:click={() => showWeightModal = true}>
          {weight ? `${weight} kg` : 'Seleccionar'}
          <span class="chev">›</span>
        </button>
      </div>
      <div class="info-item">
        <span class="info-icon">📏</span>
        <span class="info-label">Altura</span>
        <button class="info-select" on:click={() => showHeightModal = true}>
          {height ? `${height} cm` : 'Seleccionar'}
          <span class="chev">›</span>
        </button>
      </div>
    </div>

    <!-- Modal Sexo -->
    {#if showGenderModal}
      <div class="modal-overlay" on:click={() => showGenderModal = false}>
        <div class="modal" on:click|stopPropagation>
          <div class="modal-bar"></div>
          <h3>Sexo</h3>
          <button class="modal-option" on:click={() => { gender = 'male'; showGenderModal = false; }}>Hombre</button>
          <button class="modal-option" on:click={() => { gender = 'female'; showGenderModal = false; }}>Mujer</button>
        </div>
      </div>
    {/if}

    <!-- Modal Edad -->
    {#if showAgeModal}
      <div class="modal-overlay" on:click={() => showAgeModal = false}>
        <div class="modal" on:click|stopPropagation>
          <div class="modal-bar"></div>
          <h3>Edad</h3>
          <div class="modal-picker">
            <input type="number" min="10" max="99" bind:value={age} class="modal-input" />
            <span class="modal-unit">años</span>
          </div>
          <button class="modal-ok" on:click={() => showAgeModal = false}>OK</button>
        </div>
      </div>
    {/if}

    <!-- Modal Peso -->
    {#if showWeightModal}
      <div class="modal-overlay" on:click={() => showWeightModal = false}>
        <div class="modal" on:click|stopPropagation>
          <div class="modal-bar"></div>
          <h3>Peso</h3>
          <div class="modal-toggle">
            <button class:active={weightUnit === 'kg'} on:click={() => weightUnit = 'kg'}>kg</button>
            <button class:active={weightUnit === 'lbs'} on:click={() => weightUnit = 'lbs'}>lbs</button>
          </div>
          <div class="modal-picker">
            <input type="number" min="30" max="200" bind:value={weight} class="modal-input" />
            <span class="modal-unit">{weightUnit}</span>
          </div>
          <button class="modal-ok" on:click={() => showWeightModal = false}>OK</button>
        </div>
      </div>
    {/if}

    <!-- Modal Altura -->
    {#if showHeightModal}
      <div class="modal-overlay" on:click={() => showHeightModal = false}>
        <div class="modal" on:click|stopPropagation>
          <div class="modal-bar"></div>
          <h3>Altura</h3>
          <div class="modal-toggle">
            <button class:active={heightUnit === 'cm'} on:click={() => heightUnit = 'cm'}>cm</button>
            <button class:active={heightUnit === 'ft'} on:click={() => heightUnit = 'ft'}>ft/in</button>
          </div>
          <div class="modal-picker">
            <input type="number" min="120" max="220" bind:value={height} class="modal-input" />
            <span class="modal-unit">{heightUnit}</span>
          </div>
          <button class="modal-ok" on:click={() => showHeightModal = false}>OK</button>
        </div>
      </div>
    {/if}

    <div class="nav-buttons">
      <button on:click={prevView}>Regresar</button>
      <button on:click={nextView}>Continuar</button>
    </div>
  </section>
{/if}

  {#if currentView === 4}
    <section class="card">
      <h2>¿Cuanta actividad tienes?</h2>
      <li class="item">
        <span class="icon">🛌</span>
        <span class="label">nada Activo</span>
      </li>

      <li class="item">
        <span class="icon" >🧘</span>
        <span class="label">Poco activo</span>
      </li>

      <li class="item">
        <span class="icon">🚶</span>
        <span class="label">Moderadamente activo</span>
      </li>

      <li class="item">
        <span class="icon">🤸</span>
        <span class="label">Muy activo</span>
      </li>

      <li class="item">
        <span class="icon">🧗</span>
        <span class="label">Atleta</span>
      </li>
      
      <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 5}
    <section class="card">
      <h2>Que tipo de dieta prefieres?</h2>

      <li class="item">
        <span class="icon">✨</span>
        <span class="label">Recomendada</span>
        <p>La mejor opcion para ti, una mezcla equilibrada de nutrientes.</p>
      </li>
      
      <li class="item">
        <span class="icon">🍗</span>
        <span class="label">Alta en Proteinas</span>
        <p>Ideal para ganar músculo y mantener la saciedad.</p>
      </li>

      <li class="item">
        <span class="icon">🥑</span>
        <span class="label">Baja en Carbohidratos</span>
        <p>Perfecta para perder grasa y controlar el apetito.</p>
      </li>

      <li class="item">
        <span class="icon">🌱</span>
        <span class="label">Baja en Grasas</span>
        <p>Buena para mejorar la salud cardiovascular y perder peso.</p>
      </li>
      
      <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 6}
    
<section class="card">
      <h2>Personalicemos tu Objetivo</h2>
      <p>Este es el último paso para personalizar tu experiencia.</p>

      <div class="info-item">
        <span class="info-icon">⚖️</span>
        <span class="info-label">Peso</span>
        <button class="info-select" on:click={() => showWeightModal = true}>
          {weight ? `${weight} kg` : 'Seleccionar'}
          <span class="chev">›</span>
        </button>
      </div>

      <div class="info-item">
        <span class="info-icon">🎯</span>
        <span class="info-label">Peso Objetivo</span>
        <button class="info-select" on:click={() => showTargetWeightModal = true}>
          {targetWeight ? `${targetWeight} kg` : 'Seleccionar'}
          <span class="chev">›</span>
        </button>
      </div>

      <div class="info-item">   
        <span class="info-icon">⏱️</span>
        <span class="info-label">Velocidad de Ganancia de Peso</span>
        <button class="info-select" on:click={() => showSpeedModal = true}>
          {selectedSpeed === 'recomendada' ? 'Recomendada' : selectedSpeed === 'rapido' ? 'Rápido' : 'Lento'}
          <span class="chev">›</span>
        </button>
      </div>

      <!-- Modal Peso Actual -->
      {#if showWeightModal}
        <div class="modal-overlay" on:click={() => showWeightModal = false}>
          <div class="modal" on:click|stopPropagation>
            <div class="modal-bar"></div>
            <h3>Peso actual</h3>
            <div class="modal-toggle">
              <button class:active={weightUnit === 'kg'} on:click={() => weightUnit = 'kg'}>kg</button>
              <button class:active={weightUnit === 'lbs'} on:click={() => weightUnit = 'lbs'}>lbs</button>
            </div>
            <div class="modal-picker">
              <input type="number" min="30" max="200" bind:value={weight} class="modal-input" />
              <span class="modal-unit">{weightUnit}</span>
            </div>
            <button class="modal-ok" on:click={() => showWeightModal = false}>OK</button>
          </div>
        </div>
      {/if}

      <!-- Modal Peso Objetivo -->
      {#if showTargetWeightModal}
        <div class="modal-overlay" on:click={() => showTargetWeightModal = false}>
          <div class="modal" on:click|stopPropagation>
            <div class="modal-bar"></div>
            <h3>Peso Objetivo</h3>
            <div class="modal-toggle">
              <button class:active={weightUnit === 'kg'} on:click={() => weightUnit = 'kg'}>kg</button>
              <button class:active={weightUnit === 'lbs'} on:click={() => weightUnit = 'lbs'}>lbs</button>
            </div>
            <div class="modal-picker">
              <input type="number" min="30" max="200" bind:value={targetWeight} class="modal-input" />
              <span class="modal-unit">{weightUnit}</span>
            </div>
            <button class="modal-ok" on:click={() => showTargetWeightModal = false}>OK</button>
          </div>
        </div>
      {/if}

      <!-- Modal Velocidad -->
      {#if showSpeedModal}
  <div class="modal-overlay" on:click={() => showSpeedModal = false}>
    <div class="modal" on:click|stopPropagation>
      <div class="modal-bar"></div>
      <h3>Velocidad de Ganancia de Peso</h3>
      <button
        class="speed-option {selectedSpeed === 'recomendada' ? 'active' : ''}"
        on:click={() => selectedSpeed = 'recomendada'}>
        <span class="speed-icon">🎧</span>
        Recomendado
      </button>
      {#if selectedSpeed === 'recomendada'}
        <ul class="speed-details">
          <li><span class="check">✔️</span> Ganancia óptima de masa muscular y peso</li>
          <li><span class="check">✔️</span> Resultados visibles en el corto plazo</li>
          <li><span class="check">✔️</span> Alimentación sostenible</li>
        </ul>
      {/if}
      <button
        class="speed-option {selectedSpeed === 'rapido' ? 'active' : ''}"
        on:click={() => selectedSpeed = 'rapido'}>
        <span class="speed-icon">🚀</span>
        Rápido
      </button>
      {#if selectedSpeed === 'rapido'}
        <ul class="speed-details">
          <li><span class="check">✔️</span> Ganancia rápida de peso y músculo</li>
          <li><span class="check">✔️</span> Ideal para atletas o con poco tiempo</li>
          <li><span class="check">✔️</span> Requiere mayor disciplina y seguimiento</li>
        </ul>
      {/if}
      <button
        class="speed-option {selectedSpeed === 'lento' ? 'active' : ''}"
        on:click={() => selectedSpeed = 'lento'}>
        <span class="speed-icon">🐢</span>
        Lento
      </button>
      {#if selectedSpeed === 'lento'}
        <ul class="speed-details">
          <li><span class="check">✔️</span> Ganancia gradual y sostenible</li>
          <li><span class="check">✔️</span> Mejor para principiantes</li>
          <li><span class="check">✔️</span> Menos riesgo de acumular grasa extra</li>
        </ul>
      {/if}
      <button class="modal-ok" on:click={() => showSpeedModal = false}>OK</button>
    </div>
  </div>
{/if}
      
      <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 7}
    <section class="card">
    <h2>¡Tu progreso y tus calorías!</h2>
    <div class="carousel">
      <div class="carousel-track" style="transform: translateX(-{carouselIndex * 100}%);">
        <!-- Slide 1: Progreso de peso -->
        <div class="carousel-slide">
          <div class="carousel-check">
            <span class="carousel-check-icon">✔️</span>
          </div>
          <p class="carousel-title">...y así será tu progreso</p>
          <div class="carousel-metric-card">
            <div class="metric-header">
              <span class="metric-label">Objetivo actual</span>
              <span class="metric-label metric-label-right">Siguiente</span>
            </div>
            <div class="metric-graph">
              <div class="metric-point metric-point-left">
                <span class="metric-point-label">64 kg</span>
                <span class="metric-point-dot"></span>
              </div>
              <div class="metric-line"></div>
              <div class="metric-point metric-point-right">
                <span class="metric-point-label metric-point-label-right">70 kg</span>
                <span class="metric-point-dot metric-point-dot-right"></span>
              </div>
            </div>
            <div class="metric-footer">
              <span class="metric-date">Hoy</span>
              <span class="metric-date">Oct 28</span>
              <span class="metric-date">Dec 9</span>
              <span class="metric-date metric-date-right">Dec 29</span>
            </div>
          </div>
        </div>
        <!-- Slide 2: Calorías y macros -->
        <div class="carousel-slide">
          <div class="carousel-check">
            <span class="carousel-check-icon">✔️</span>
          </div>
          <p class="carousel-title">¡Genial! Estas son las calorías que necesitas al día</p>
          <div class="carousel-metric-card">
            <div class="metric-kcal">2,167 kcal</div>
            <div class="metric-macros">
              <div class="macro">
                <span class="macro-label">Proteínas</span>
                <span class="macro-value">100 g</span>
                <div class="macro-bar"></div>
              </div>
              <div class="macro">
                <span class="macro-label">Carbs</span>
                <span class="macro-value">252 g</span>
                <div class="macro-bar"></div>
              </div>
              <div class="macro">
                <span class="macro-label">Grasas</span>
                <span class="macro-value">84 g</span>
                <div class="macro-bar"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Carousel dots -->
      <div class="carousel-dots">
        <span class="carousel-dot" class:active={carouselIndex === 0} on:click={() => carouselIndex = 0}></span>
        <span class="carousel-dot" class:active={carouselIndex === 1} on:click={() => carouselIndex = 1}></span>
      </div>
    </div>
    <div class="nav-buttons">
      <button on:click={prevView}>Regresar</button>
      <button class="carousel-next" on:click={() => {
        if (carouselIndex < 1) carouselIndex++;
        else nextView();
      }}>
        {carouselIndex < 1 ? 'Siguiente' : 'Continuar'}
      </button>
    </div>
  </section>  
  {/if}

  {#if currentView === 8}
    <section class="card">
      <h2>Vista 8</h2>
      <p>Configura esta vista</p>
      
      <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 9}
    <section class="card">
      <h2>Vista 9</h2>
      <p>Configura esta vista </p>
      
      <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 10}
    <section class="card">
      <h2>Vista 10</h2>
      <p>Configura esta vista </p>
     
      <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView}>Continuar</button>
      </div>
    </section>
  {/if}
</main>

<style>
  :global(html) {
    height: 100%;
  }

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: linear-gradient(70deg, blue 0%, pink 100%);
    color: #f2f2f2;
    min-height: 100vh;
  }

  .bg {
    animation: slide 3s ease-in-out infinite alternate;
    background-image: linear-gradient(-60deg, #6c3 50%, #09f 50%);
    bottom: 0;
    left: -50%;
    opacity: 0.5;
    position: fixed;
    right: -50%;
    top: 0;
    z-index: -1;
  }

  .bg2 {
    animation-direction: alternate-reverse;
    animation-duration: 4s;
  }

  .bg3 {
    animation-duration: 5s;
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
  }

  .card {
    background: rgba(245, 243, 243, 0.2);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6);
    margin-bottom: 18px;
    -webkit-backdrop-filter: blur(12px);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(233, 225, 225, 0.2);
  }

  h2 {
    color: #cfcfcf;
    font-size: 20px;
    margin-bottom: 10px;
    font-weight: 600;
  }

  p {
    color: #ffffff;
    margin-bottom: 20px;
  }

  .lista {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .opcion {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.2s;
    position: relative;
  }

  .opcion:hover {
    background: rgba(255, 255, 255, 0.2);
  }

  .opcion input[type="radio"] {
    position: absolute;
    opacity: 0;
    cursor: pointer;
  }

  .checkmark {
    width: 20px;
    height: 20px;
    border: 2px solid #ffffff;
    border-radius: 50%;
    position: relative;
    flex-shrink: 0;
  }

  .opcion input[type="radio"]:checked ~ .checkmark {
    background: #005bb5;
    border-color: #005bb5;
  }

  .checkmark::after {
    content: "";
    position: absolute;
    display: none;
    left: 6px;
    top: 2px;
    width: 6px;
    height: 10px;
    border: solid white;
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
  }

  .opcion input[type="radio"]:checked ~ .checkmark::after {
    display: block;
  }

  .barra {
    background-color: rgba(0, 0, 0, 0.2);
    border-radius: 4px;
    height: 20px;
    margin-bottom: 10px;
    overflow: hidden;
  }

  .barra-llena {
    background-color: #005bb5;
    height: 100%;
    color: white;
    text-align: center;
    line-height: 20px;
    font-size: 12px;
  }

  .nav-buttons {
    display: flex;
    gap: 12px;
    margin-top: 20px;
  }

  .nav-buttons button {
    flex: 1;
    background-color: #005bb5;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }

  .nav-buttons button:hover {
    background-color: #004499;
  }

  @media (prefers-color-scheme: light) {
    :global(body) {
      background: linear-gradient(135deg, #ffffffff 0%, #f9f8feff 100%);
      color: #111;
    }
    .card {
      background: #fff;
      color: #222;
      box-shadow: 0 8px 26px rgba(10, 10, 10, 0.06);
      border: 1px solid rgba(10, 10, 10, 0.04);
    }
    h2 {
      color: #333;
    }
    p {
      color: #666;
    }
    .barra {
      background-color: #e0e0e0;
    }
    .opcion {
      background: rgba(0, 0, 0, 0.05);
    }
    .opcion:hover {
      background: rgba(0, 0, 0, 0.1);
    }
    .checkmark {
      border-color: #333;
    }
    .opcion input[type="radio"]:checked ~ .checkmark {
      background: #005bb5;
      border-color: #005bb5;
    }
  }

  @keyframes slide {
    0% {
      transform: translateX(-25%);
    }
    100% {
      transform: translateX(25%);
    }
  }

  .info-list {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-bottom: 24px;
  }
  .info-item {
    display: flex;
    align-items: center;
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 14px 12px;
    gap: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }
  .info-icon {
    font-size: 22px;
    background: rgba(255,255,255,0.12);
    border-radius: 8px;
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffd600;
  }
  .info-label {
    flex: 1;
    font-size: 16px;
    color: #fff;
    font-weight: 500;
  }
  .info-select {
    background: none;
    border: none;
    color: #ffffff;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 0;
  }
  .chev {
    color: #ffffff;
    font-size: 18px;
  }

  /* Modal styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.25); /* Más oscuro pero aún difuminado */
  display: flex;
  align-items: flex-end;
  justify-content: center;
  z-index: 1000;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.modal {
  background: rgba(40, 44, 52, 0.35); /* Más oscuro y difuminado */
  border-radius: 18px 18px 0 0;
  width: 100%;
  max-width: 420px;
  padding: 32px 24px 24px 24px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.28);
  position: relative;
  animation: modalUp 0.2s;
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(233, 225, 225, 0.2);
}

.modal-bar {
  width: 48px;
  height: 5px;
  background: #b3e5fc;
  border-radius: 3px;
  position: absolute;
  top: 12px;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0.5;
}

.modal h3 {
  text-align: center;
  color: #cfcfcf;
  font-size: 22px;
  margin-bottom: 24px;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.modal-option {
  width: 100%;
  background: rgba(255,255,255,0.1);
  color: #ffffff;
  border: none;
  border-radius: 10px;
  padding: 16px;
  font-size: 18px;
  margin-bottom: 12px;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  text-align: left;
  font-weight: 500;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.modal-option:hover {
  background: #ffffff;
  color: #fff;
}

.modal-picker {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 24px;
}

.modal-input {
  width: 80px;
  font-size: 22px;
  padding: 8px;
  border-radius: 8px;
  border: none;
  background: rgba(255,255,255,0.1);
  color: #ffffff;
  text-align: center;
  outline: none;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.modal-unit {
  color: #ffffff;
  font-size: 18px;
  margin-left: 8px;
  font-weight: 500;
}

.modal-toggle {
  display: flex;
  gap: 8px;
  justify-content: center;
  margin-bottom: 18px;
}

.modal-toggle button {
  flex: 1;
  background: rgba(255,255,255,0.1);
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 10px 0;
  font-size: 16px;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.2s, color 0.2s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.modal-toggle button.active,
.modal-toggle button:active {
  background: #005bb5;
  color: #fff;
}

.modal-ok {
  width: 100%;
  background: #005bb5;
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 16px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 8px;
  transition: background 0.2s;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.modal-ok:hover {
  background: #004499;
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

  .item {
  display: flex;
    align-items: center;
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 14px 12px;
    gap: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 18px; 
    border-bottom: none;
}

.icon {
  font-size: 28px;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border-radius: 8px;
  color: #4b2aad;
}

.label {
  flex: 1;
  font-size: 20px;
  color: #fff;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.speed-option {
  width: 100%;
  background: rgba(255,255,255,0.08);
  color: #fff;
  border: none;
  border-radius: 12px;
  padding: 18px 18px;
  font-size: 18px;
  margin-bottom: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 2px solid transparent;
  transition: background 0.2s, border 0.2s;
}

.speed-option.active {
  background: rgba(245, 243, 243, 0.18);
  border: 2px solid #ffd600;
  color: #ffd600;
}

.speed-icon {
  font-size: 24px;
  color: #ffd600;
}

.speed-details {
  list-style: none;
  padding: 0 0 0 8px;
  margin: 0 0 18px 0;
}

.speed-details li {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #fff;
  font-size: 16px;
  margin-bottom: 6px;
}

.check {
  color: #4caf50;
  font-size: 18px;
}

.carousel {
  position: relative;
  width: 100%;
  overflow: hidden;
  margin-bottom: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.carousel-track {
  display: flex;
  transition: transform 0.4s cubic-bezier(.4,.8,.4,1);
  width: 100%;
}
.carousel-slide {
  min-width: 100%;
  box-sizing: border-box;
  padding: 0 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.carousel-check {
  margin: 18px 0 8px 0;
}
.carousel-check-icon {
  font-size: 44px;
  color: #4caf50;
  background: #fff;
  border-radius: 50%;
  padding: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.carousel-title {
  text-align: center;
  color: #fff;
  font-size: 18px;
  margin-bottom: 18px;
  font-weight: 600;
}
.carousel-metric-card {
  background: rgba(245,243,243,0.18);
  border-radius: 18px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.18);
  border: 1px solid rgba(233,225,225,0.18);
  padding: 24px 18px;
  width: 340px; /* Fijo y centrado */
  margin-bottom: 18px;
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
@media (max-width: 400px) {
  .carousel-metric-card {
    width: 100%;
    min-width: 0;
    padding: 16px 4px;
  }
}
.metric-header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 8px;
}
.metric-label {
  color: #fff;
  font-size: 15px;
  font-weight: 500;
  opacity: 0.8;
}
.metric-label-right {
  text-align: right;
}
.metric-graph {
  display: flex;
  align-items: center;
  width: 100%;
  margin: 18px 0 8px 0;
  position: relative;
  height: 48px;
}
.metric-point {
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2;
}
.metric-point-label {
  background: #005bb5;
  color: #222;
  font-size: 15px;
  font-weight: 600;
  border-radius: 6px;
  padding: 2px 10px;
  margin-bottom: 2px;
}
.metric-point-label-right {
  margin-left: 18px;
}
.metric-point-dot {
  width: 14px;
  height: 14px;
  background: #fff;
  border: 3px solid #005bb5;
  border-radius: 50%;
  margin-top: 2px;
}
.metric-point-dot-right {
  border-color: #005bb5;
}
.metric-line {
  flex: 1;
  height: 4px;
  background: linear-gradient(90deg, #005bb5 60%, #fff 100%);
  margin: 0 8px;
  border-radius: 2px;
  position: relative;
  top: 14px;
  z-index: 1;
}
.metric-footer {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-top: 8px;
}
.metric-date {
  color: #fff;
  font-size: 13px;
  opacity: 0.7;
}
.metric-date-right {
  text-align: right;
}
.metric-kcal {
  color: #fff;
  font-size: 28px;
  font-weight: 700;
  text-align: center;
  margin-bottom: 18px;
}
.metric-macros {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 12px;
}
.macro {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
}
.macro-label {
  color: #fff;
  font-size: 15px;
  font-weight: 500;
  margin-bottom: 2px;
}
.macro-value {
  color: #ffffff;
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 2px;
}
.macro-bar {
  width: 80%;
  height: 6px;
  background: #005bb5;
  border-radius: 3px;
  margin-top: 4px;
}
.carousel-dots {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.carousel-dot {
  width: 10px;
  height: 10px;
  background: #fff;
  border-radius: 50%;
  opacity: 0.4;
  cursor: pointer;
  transition: opacity 0.2s;
}
.carousel-dot.active {
  opacity: 1;
  background: #005bb5;
}
.carousel-next {
  background: #005bb5 !important;
  color: #ffffff !important;
  font-weight: 600;
}
</style>