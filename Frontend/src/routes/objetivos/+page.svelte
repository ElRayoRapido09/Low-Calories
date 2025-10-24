<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let currentView = 1; 

  function goToHome() {
    goto('/');
  }

  function nextView() {
    if (currentView < 11) {
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
  
  // Variables para las vistas de comidas
  let selectedMeals = {
    desayuno: true,
    almuerzo: true,
    cena: true,
    snacks: false,
    snacks2: false
  };

  // Variables para preferencias de sugerencias
  let suggestionType = 'recipes'; // 'recipes' o 'ingredients'

  function toggleMeal(mealType) {
    // Las comidas principales no se pueden desmarcar si hay menos de 2 seleccionadas
    const principalMeals = ['desayuno', 'almuerzo', 'cena'];
    const selectedPrincipalCount = principalMeals.filter(meal => selectedMeals[meal]).length;
    
    if (principalMeals.includes(mealType) && selectedMeals[mealType] && selectedPrincipalCount <= 2) {
      return; // No permitir desmarcar si solo quedan 2 comidas principales
    }
    
    selectedMeals[mealType] = !selectedMeals[mealType];
  }

  function setSuggestionType(type) {
    suggestionType = type;
  }
</script>

<main class="app">
  <header class="top">
    <a href="/" class="back-btn" aria-label="Volver">‹</a>
    <h1>Objetivos</h1>
  </header>

  
  {#if currentView === 1}
    <section class="card">
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 10%"></div>
        </div>
      </div>
      
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
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 20%"></div>
        </div>
      </div>
      
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
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 30%"></div>
        </div>
      </div>
      
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
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 40%"></div>
        </div>
      </div>
      
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
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 50%"></div>
        </div>
      </div>
      
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
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 60%"></div>
        </div>
      </div>
      
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
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 70%"></div>
        </div>
      </div>
      
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
    <section class="card meal-planning-intro">
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 80%"></div>
        </div>
      </div>
      
      <div class="intro-content">
        <div class="meal-icon-container">
          <div class="meal-icon-outer">
            <div class="meal-icon-middle">
              <div class="meal-icon-inner">
                <span class="meal-icon">📝</span>
              </div>
            </div>
          </div>
        </div>
        
        <h2 class="intro-title">Ahora, personalicemos tu plan de comidas para alcanzar tus calorías diarias</h2>
      </div>
      
      <div class="nav-buttons">
        <button on:click={nextView} class="continue-btn">Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 9}
    <section class="card meal-selection">
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 80%"></div>
        </div>
      </div>
      
      <div class="meal-header">
        <div class="meal-plate-icon">🍽️</div>
        <h2>¿Cuántas comidas al día deseas?</h2>
        <p class="meal-subtitle">Elige al menos 2 comidas principales</p>
      </div>

      <div class="meal-options">
        <button type="button" class="meal-option" class:selected={selectedMeals.desayuno} on:click={() => toggleMeal('desayuno')}>
          <div class="meal-check" class:visible={selectedMeals.desayuno}>✓</div>
          <span class="meal-name">Desayuno</span>
          <span class="meal-type">Principal</span>
        </button>
        
        <button type="button" class="meal-option" class:selected={selectedMeals.almuerzo} on:click={() => toggleMeal('almuerzo')}>
          <div class="meal-check" class:visible={selectedMeals.almuerzo}>✓</div>
          <span class="meal-name">Almuerzo</span>
          <span class="meal-type">Principal</span>
        </button>
        
        <button type="button" class="meal-option" class:selected={selectedMeals.cena} on:click={() => toggleMeal('cena')}>
          <div class="meal-check" class:visible={selectedMeals.cena}>✓</div>
          <span class="meal-name">Cena</span>
          <span class="meal-type">Principal</span>
        </button>
        
        <button type="button" class="meal-option add-option" class:selected={selectedMeals.snacks} on:click={() => toggleMeal('snacks')}>
          <div class="meal-add" class:meal-check={selectedMeals.snacks} class:visible={selectedMeals.snacks}>
            {selectedMeals.snacks ? '✓' : '+'}
          </div>
          <span class="meal-name">Snacks</span>
        </button>
        
        <button type="button" class="meal-option add-option" class:selected={selectedMeals.snacks2} on:click={() => toggleMeal('snacks2')}>
          <div class="meal-add" class:meal-check={selectedMeals.snacks2} class:visible={selectedMeals.snacks2}>
            {selectedMeals.snacks2 ? '✓' : '+'}
          </div>
          <span class="meal-name">Snacks 2</span>
        </button>
      </div>

      <p class="meal-note">No te preocupes, luego lo puedes cambiar</p>
      
      <div class="nav-buttons">
        <button on:click={nextView} class="continue-btn">Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 10}
    <section class="card food-preferences">
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 90%"></div>
        </div>
      </div>
      
      <div class="preferences-header">
        <div class="preferences-icon">✨</div>
        <h2>¿Cómo prefieres tus sugerencias de comidas?</h2>
      </div>

      <!-- Opciones de tipo de sugerencia -->
      <div class="suggestion-types">
        <button type="button" class="suggestion-option" class:selected={suggestionType === 'recipes'} on:click={() => setSuggestionType('recipes')}>
          <div class="suggestion-content">
            <h3>Recetas</h3>
            <p>Instrucciones paso a paso</p>
            <div class="recipe-example">
              <div class="recipe-image">🥪</div>
              <span class="recipe-name">Sándwich de Pollo con Aguacate</span>
            </div>
          </div>
        </button>
        
        <button type="button" class="suggestion-option" class:selected={suggestionType === 'ingredients'} on:click={() => setSuggestionType('ingredients')}>
          <div class="suggestion-content">
            <h3>Solo ingredientes</h3>
            <p>Puedes prepararlo como quieras</p>
            <div class="ingredients-list">
              <div class="ingredient-item">
                <span class="ingredient-icon">🍗</span>
                <span class="ingredient-name">Pollo</span>
                <span class="ingredient-amount">1 filete mediano</span>
              </div>
              <div class="ingredient-item">
                <span class="ingredient-icon">🍚</span>
                <span class="ingredient-name">Arroz</span>
                <span class="ingredient-amount">1 taza</span>
              </div>
              <div class="ingredient-item">
                <span class="ingredient-icon">🥑</span>
                <span class="ingredient-name">Aguacate</span>
                <span class="ingredient-amount">1/2 unidad</span>
              </div>
            </div>
          </div>
        </button>
      </div>
      
      <div class="nav-buttons">
        <button on:click={prevView}>Regresar</button>
        <button on:click={nextView} class="continue-btn">Continuar</button>
      </div>
    </section>
  {/if}

  {#if currentView === 11}
    <section class="card completion-screen">
      <div class="progress-indicator">
        <div class="progress-bar-small">
          <div class="progress-fill-small" style="width: 100%"></div>
        </div>
      </div>
      
      <div class="completion-content">
        <div class="completion-icon-container">
          <div class="completion-icon-outer">
            <div class="completion-icon-middle">
              <div class="completion-icon-inner">
                <span class="completion-icon">🎉</span>
              </div>
            </div>
          </div>
        </div>
        
        <h2 class="completion-title">¡Configuración Completada!</h2>
        <p class="completion-subtitle">Tu plan personalizado está listo</p>
        
        <div class="completion-summary">
          <div class="summary-item">
            <span class="summary-icon">🎯</span>
            <span class="summary-text">Objetivo configurado</span>
          </div>
          <div class="summary-item">
            <span class="summary-icon">🍽️</span>
            <span class="summary-text">Plan de comidas personalizado</span>
          </div>
          <div class="summary-item">
            <span class="summary-icon">📊</span>
            <span class="summary-text">Calorías y macros calculados</span>
          </div>
        </div>
      </div>
      
      <div class="nav-buttons">
        <button on:click={goToHome} class="completion-btn">Comenzar mi plan</button>
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
    background: #ffffff;
    color: #333;
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
  }

  .card {
    background: #ffffff;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 18px;
    border: 1px solid #e0e0e0;
  }

  h2 {
    color: #000;
    font-size: 20px;
    margin-bottom: 10px;
    font-weight: 600;
  }

  p {
    color: #666;
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
    color: #666;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 0;
  }
  .chev {
    color: #666;
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
  background: rgba(0, 0, 0, 0.5);
}

.modal {
  background: #ffffff;
  border-radius: 18px 18px 0 0;
  width: 100%;
  max-width: 420px;
  padding: 32px 24px 24px 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  position: relative;
  animation: modalUp 0.2s;
  border: 1px solid #e0e0e0;
}

.modal-bar {
  width: 48px;
  height: 5px;
  background: #005bb5;
  border-radius: 3px;
  position: absolute;
  top: 12px;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0.5;
}

.modal h3 {
  text-align: center;
  color: #000;
  font-size: 22px;
  margin-bottom: 24px;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.modal-option {
  width: 100%;
  background: rgba(255,255,255,0.1);
  color: #666;
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
  color: #666;
  text-align: center;
  outline: none;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.modal-unit {
  color: #666;
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
  color: #666;
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
  border: 1px solid #e0e0e0;
  padding: 24px 18px;
  width: 340px; /* Fijo y centrado */
  margin-bottom: 18px;
  background: #ffffff;
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
  color: #666;
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

/* Estilos para Vista 8 - Introducción al plan de comidas */
.meal-planning-intro {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  min-height: 60vh;
  padding: 2rem 1.5rem;
}

.intro-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 3rem;
}

.meal-icon-container {
  margin-bottom: 2rem;
}

.meal-icon-outer {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 91, 181, 0.3) 0%, rgba(0, 91, 181, 0.1) 50%, transparent 70%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.meal-icon-middle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 91, 181, 0.5) 0%, rgba(0, 91, 181, 0.2) 70%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.meal-icon-inner {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, #005bb5 0%, #004499 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(0, 91, 181, 0.3);
}

.meal-icon {
  font-size: 2.5rem;
  color: white;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

.intro-title {
  font-size: 1.5rem;
  font-weight: 600;
  line-height: 1.4;
  color: #000;
  margin: 0;
  max-width: 350px;
}

/* Estilos para Vista 9 - Selección de comidas */
.meal-selection {
  padding: 1.5rem;
}

.progress-indicator {
  margin-bottom: 1.5rem;
}

.progress-bar-small {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 2px;
  overflow: hidden;
}

.progress-fill-small {
  height: 100%;
  background: linear-gradient(90deg, #005bb5, #004499);
  border-radius: 2px;
  transition: width 0.3s ease;
}

.meal-header {
  text-align: center;
  margin-bottom: 2rem;
}

.meal-plate-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, rgba(0, 91, 181, 0.2) 0%, rgba(0, 68, 153, 0.2) 100%);
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem auto;
}

.meal-header h2 {
  font-size: 1.3rem;
  font-weight: 600;
  color: #000;
  margin: 0 0 0.5rem 0;
}

.meal-subtitle {
  font-size: 0.9rem;
  color: #9b9b9b;
  margin: 0;
}

.meal-options {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 1.5rem;
}

.meal-option {
  display: flex;
  align-items: center;
  padding: 16px;
  border-radius: 12px;
  border: 2px solid rgba(0, 91, 181, 0.3);
  background: rgba(255, 255, 255, 0.08);
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  width: 100%;
  text-align: left;
  font-family: inherit;
  font-size: inherit;
}

.meal-option.selected {
  border-color: #005bb5;
  background: rgba(0, 91, 181, 0.1);
}

.meal-option.add-option {
  border-color: rgba(255, 255, 255, 0.2);
  background: rgba(255, 255, 255, 0.05);
}

.meal-option:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.meal-check {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #005bb5;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: bold;
  margin-right: 12px;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.meal-check.visible {
  opacity: 1;
}

.meal-add {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  color: #9b9b9b;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: bold;
  margin-right: 12px;
  transition: all 0.2s ease;
}

.meal-add.meal-check {
  background: #005bb5;
  color: #fff;
  font-size: 0.8rem;
}

.meal-name {
  flex: 1;
  font-size: 1rem;
  font-weight: 500;
  color: #fff;
}

.meal-type {
  font-size: 0.8rem;
  color: #005bb5;
  font-weight: 500;
  background: rgba(0, 91, 181, 0.2);
  padding: 4px 8px;
  border-radius: 6px;
}

.meal-note {
  text-align: center;
  font-size: 0.85rem;
  color: #9b9b9b;
  margin: 1rem 0 2rem 0;
}

.continue-btn {
  width: 100%;
  background: #005bb5;
  color: #fff;
  border: none;
  padding: 16px;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.continue-btn:hover {
  background: #004499;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 91, 181, 0.3);
}

.continue-btn:active {
  transform: translateY(0);
}

/* Estilos para Vista 10 - Preferencias de comidas */
.food-preferences {
  padding: 1.5rem;
}

.preferences-header {
  text-align: center;
  margin-bottom: 2rem;
}

.preferences-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, rgba(0, 91, 181, 0.2) 0%, rgba(0, 68, 153, 0.2) 100%);
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem auto;
}

.preferences-header h2 {
  font-size: 1.3rem;
  font-weight: 600;
  color: #000;
  margin: 0;
}

.suggestion-types {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 2rem;
}

.suggestion-option {
  width: 100%;
  background: rgba(255, 255, 255, 0.08);
  border: 2px solid rgba(0, 91, 181, 0.3);
  border-radius: 12px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
  font-family: inherit;
}

.suggestion-option.selected {
  border-color: #005bb5;
  background: rgba(0, 91, 181, 0.1);
}

.suggestion-option:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2);
}

.suggestion-content h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff;
  margin: 0 0 0.5rem 0;
}

.suggestion-content p {
  font-size: 0.9rem;
  color: #9b9b9b;
  margin: 0 0 1rem 0;
}

.recipe-example {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(0, 91, 181, 0.1);
  padding: 12px;
  border-radius: 8px;
}

.recipe-image {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  background: #005bb5;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
}

.recipe-name {
  font-size: 0.9rem;
  color: #fff;
  font-weight: 500;
}

.ingredients-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ingredient-item {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(0, 91, 181, 0.1);
  padding: 8px 12px;
  border-radius: 6px;
}

.ingredient-icon {
  font-size: 1.2rem;
  width: 24px;
  text-align: center;
}

.ingredient-name {
  flex: 1;
  font-size: 0.9rem;
  color: #fff;
  font-weight: 500;
}

.ingredient-amount {
  font-size: 0.8rem;
  color: #9b9b9b;
}

/* Estilos para Vista 11 - Pantalla de finalización */
.completion-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  min-height: 60vh;
  padding: 2rem 1.5rem;
}

.completion-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 3rem;
}

.completion-icon-container {
  margin-bottom: 2rem;
}

.completion-icon-outer {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 91, 181, 0.3) 0%, rgba(0, 91, 181, 0.1) 50%, transparent 70%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.completion-icon-middle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 91, 181, 0.5) 0%, rgba(0, 91, 181, 0.2) 70%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.completion-icon-inner {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, #005bb5 0%, #004499 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(0, 91, 181, 0.3);
}

.completion-icon {
  font-size: 2.5rem;
  color: white;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

.completion-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #000;
  margin: 0 0 0.5rem 0;
}

.completion-subtitle {
  font-size: 1rem;
  color: #9b9b9b;
  margin: 0 0 2rem 0;
}

.completion-summary {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 100%;
  max-width: 300px;
}

.summary-item {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(0, 91, 181, 0.1);
  padding: 12px 16px;
  border-radius: 8px;
  border: 1px solid rgba(0, 91, 181, 0.2);
}

.summary-icon {
  font-size: 1.2rem;
  width: 24px;
  text-align: center;
}

.summary-text {
  font-size: 0.9rem;
  color: #fff;
  font-weight: 500;
}

.completion-btn {
  width: 100%;
  background: #005bb5;
  color: #fff;
  border: none;
  padding: 18px;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 91, 181, 0.2);
}

.completion-btn:hover {
  background: #004499;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 91, 181, 0.3);
}

.completion-btn:active {
  transform: translateY(0);
}
</style>
