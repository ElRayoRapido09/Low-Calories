<script>
  import { _ } from 'svelte-i18n';
  import { energyUnit, convertValue, formatWithUnit } from '$lib/stores/units.js';
  import { 
    TrendingUp,    // Progreso Semanal
    Calendar,      // Esta semana
  } from 'lucide-svelte';
  
  // Valores de calorías almacenados (siempre en kcal)
  let caloriesConsumed = $state(1240);
  let caloriesGoal = $state(1800);
  
  // Calorías por día de la semana (en kcal)
  let weekCalories = $state([
    { dia: 'mon', kcal: 1650 },
    { dia: 'tue', kcal: 1720 },
    { dia: 'wed', kcal: 1580 },
    { dia: 'thu', kcal: 1890 },
    { dia: 'fri', kcal: 1640 },
    { dia: 'sat', kcal: 1200 },
    { dia: 'sun', kcal: null }
  ]);
  
  // Valores convertidos
  let displayConsumed = $derived(
    Math.round(convertValue(caloriesConsumed, 'energy', 'kcal', $energyUnit))
  );
  
  let displayGoal = $derived(
    Math.round(convertValue(caloriesGoal, 'energy', 'kcal', $energyUnit))
  );
  
  let displayWeekCalories = $derived(
    weekCalories.map(d => {
      if (!d.kcal) return { dia: d.dia, kcal: d.kcal, display: null };
      
      const converted = convertValue(d.kcal, 'energy', 'kcal', $energyUnit);
      // Formatear según la unidad para compactar valores grandes
      let formatted;
      if ($energyUnit === 'cal') {
        // Mostrar en formato compacto (1.65k en lugar de 1650000)
        formatted = converted >= 1000 ? `${(converted / 1000).toFixed(1)}k` : Math.round(converted);
      } else if ($energyUnit === 'kj') {
        // kJ suele ser 4x más grande que kcal
        formatted = Math.round(converted);
      } else {
        // kcal - valor normal
        formatted = Math.round(converted);
      }
      
      return { dia: d.dia, kcal: d.kcal, display: formatted };
    })
  );
</script>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<main>
    <header>
      <header class="header-back">
          <a href="/" class="back-btn" aria-label={$_('common.back')}>‹</a>
          <h1>{$_('statistics.title')}</h1>
      </header>
        <p>{$_('statistics.subtitle')}</p>
    </header>
  <section class="card-calorias">
      <div class="icons">
        <TrendingUp size={32} strokeWidth={2} />
      </div>
    <h2>{$_('statistics.weeklyProgress')}</h2>
    <p>{$_('statistics.weeklyProgressDescription')}</p>
    <div class="progress-container">
      <div class="progress-header">
        <span>{$_('statistics.caloriesProgress')}</span>
        <span><b>{displayConsumed}/{displayGoal} {$energyUnit}</b></span>
      </div>
      <div class="progress-bar">
        <div class="progress-fill" style="width: {(caloriesConsumed/caloriesGoal)*100}%;"></div>
      </div>
    </div>

    <!-- Aquí podrías agregar gráficos o tablas para mostrar las estadísticas -->
  </section>
  <section class="card-macronutrientes">
    <h2>{$_('statistics.todayMacros')}</h2>
    <p>{$_('statistics.achievedGoals')}</p>
    <p>{$_('statistics.proteins')}: 30g</p>
    <div class="progress-bar-container">
    <div class="progress-bar" style="width: {onprogress}%"></div>
  </div>

    <p>{$_('statistics.carbs')}: 50g</p>
    <div class="progress-bar-container">
    <div class="progress-bar" style="width: {onprogress}%"></div>
  </div>

    <p>{$_('statistics.fats')}: 20g</p>
    <div class="progress-bar-container">
    <div class="progress-bar" style="width: {onprogress}%"></div>
  </div>
  </section>
  <section class="card-semana">
    <div class="icons">
      <Calendar size={32} strokeWidth={2} />
    </div> 
    <h2>{$_('statistics.thisWeek')}</h2>
    <div class="semana-bar">
      {#each displayWeekCalories as d}
        <div class="dia">
          <div class="barra" style="opacity: {d.kcal ? 1 : 0.3}; background: linear-gradient(180deg, #0a3d62 70%, #38ada9 100%);">
            <!-- Puedes ajustar el alto según el valor si lo deseas -->
          </div>
          <div class="letra">{$_(`home.dayAbbr.${d.dia}`)}</div>
          <div class="valor">{d.display ?? '-'}</div>
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
    background: #ffffff;
    min-height: 100vh;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
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

    @keyframes slide {
      0% {
        transform: translateX(0%);
      }
      100% {
        transform: translateX(50%);
      }
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
      color: #000000;
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
    font-size: 0.75rem;
    color: #38ada9;
    font-weight: 500;
  }
</style>
