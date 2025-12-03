<script>
  import { _ } from 'svelte-i18n';
  import { massUnit, convertValue, formatWithUnit } from '$lib/stores/units.js';
  import {
    BarChart3,     // 📊 Tendencias
    Calendar,      // 🗓 Progreso semanal
    Target,        // 🏁 Meta diaria
    Zap,           // ⚡ Días activos
    Bell,          // 🔔 Notificaciones
    User,          // 👤 Usuario/Perfil
    Plus,          // ➕ Edad
    Ruler,         // 📏 Altura
    Scale,         // ⚖️ Peso actual
    Target as TargetIcon, // 🎯 Objetivo
  } from 'lucide-svelte';
  
  let bottomNavHeight = $derived(Math.min(50 + (scrollY * 0.8), 95));
  let scrollY = 0;
  let notificationOpen = $state(false);
  
  // Peso almacenado en kg
  let weightInKg = 62;
  
  // Peso convertido a la unidad seleccionada
  let displayWeight = $derived(
    Math.round(convertValue(weightInKg, 'mass', 'kg', $massUnit) * 10) / 10
  );
  
  let formattedWeight = $derived(
    formatWithUnit(displayWeight, $massUnit, 1)
  );

  function toggleNotifications() {
    notificationOpen = !notificationOpen;
  }

  function closeNotifications() {
    notificationOpen = false;
  }

  function handleClickOutside(e) {
    // Si el click es fuera del dropdown y del botón, cierra el dropdown
    if (e.target && !e.target.closest('.notification-button') && !e.target.closest('.dropdown-content')) {
      closeNotifications();
    }
  }
</script>

<svelte:window bind:scrollY on:click={handleClickOutside} />

<main class="main">
  <div class="container-back">
    <header class="back"> 
        <a href="/" class="back-btn" aria-label={$_('common.back')}>‹</a>
        <h1>{$_('profile.title')}</h1>
        <span class="icon">
          <User size={20} strokeWidth={2} />
        </span>
        <img class="avatar" alt={$_('navigation.profile')} src="src/lib/assets/kk.jpg" />
        <!-- Botón de notificaciones -->
        <button class="notification-button" onclick={toggleNotifications}>
            <Bell size={20} strokeWidth={2} />
            <span class="badge">3</span> <!-- Insignia de notificaciones -->
        </button>
        {#if notificationOpen}
          <div class="dropdown-content" role="menu" tabindex="-1" onclick={(e) => e.stopPropagation()} onkeydown={(e) => e.key === 'Escape' && closeNotifications()}>
              <!-- Contenido de la notificación -->
              <h3>{$_('profile.notifications')}</h3>
              <div class="notification-item">
                <p>📢 {$_('profile.notification1')}</p>
                <span class="notification-time">{$_('profile.timeAgo.hours', { values: { count: 2 } })}</span>
              </div>
              <div class="notification-item">
                <p>✅ {$_('profile.notification2')}</p>
                <span class="notification-time">{$_('profile.timeAgo.hours', { values: { count: 4 } })}</span>
              </div>
              <div class="notification-item">
                <p>🎯 {$_('profile.notification3')}</p>
                <span class="notification-time">{$_('profile.timeAgo.day')}</span>
              </div>
          </div>
        {/if}
      </header>
  </div>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

  <div class="scroll-spacer"></div>
 <!-- Usuario -->
  <div class="card-user-container">
    <section class="card-user"> 
        <div class="icons">
          <img class="avatar" alt="Perfil" src="src/lib/assets/kk.jpg" />
        </div> 
      </section>
      <h2>Jorge Mendoza Ordoñez</h2>
        <p>{$_('profile.keepGoing')}</p>
    </div>

  <div class="spacer-container"></div>

    <div class="card-container"> 
        <div class="carousel-container">  
          <div class="carousel-wrapper">

              <!-- Meta diaria -->
            <section class="card-meta">
              <div class="icons">
                <Target size={32} strokeWidth={2} />
              </div>
              <h2>1800</h2>
              <p>{$_('profile.dailyGoal')}</p>
            </section>
              <!-- Dias activos -->
            <section class="card-active">
              <div class="icons">
                <Zap size={32} strokeWidth={2} />
              </div>
              <h2>7</h2>
              <p>{$_('profile.activeDays')}</p>
            </section>
              <!-- Informacion personal -->
            <section class="card-info">
              <h2>{$_('profile.personalInfo')}</h2>
              <div class="columns">
                <div class="info-labels">
                  <p class="info-row">
                    <Plus size={16} strokeWidth={2} class="info-icon" />
                    {$_('profile.age')}
                  </p>
                  <p class="info-row">
                    <Ruler size={16} strokeWidth={2} class="info-icon" />
                    {$_('profile.height')}
                  </p>
                  <p class="info-row">
                    <Scale size={16} strokeWidth={2} class="info-icon" />
                    {$_('profile.currentWeight')}
                  </p>
                  <p class="info-row">
                    <TargetIcon size={16} strokeWidth={2} class="info-icon" />
                    {$_('profile.goal')}
                  </p>
                </div>
                <div class="info-values"> 
                  <p>28 {$_('profile.years')}</p>
                  <p>165 cm</p>
                  <p>{formattedWeight}</p>
                  <p>{$_('profile.maintainWeight')}</p>
                </div>
              </div>
            </section>
                <!-- Progreso semanal -->
            <section class="card-progress">
              <div class="icons">
                <Calendar size={32} strokeWidth={2} />
              </div>
              <h2>{$_('profile.weeklyProgress')}</h2>
              <div class="columns">
                <div>
                  <p>{$_('profile.dailyAverage')}</p>
                </div>
                <div>
                  <p>1,650 Kcal</p>
                </div>
              </div>
                
              <div class="progress-container">
                <div class="progress-header">
                  <span>{$_('profile.completedDays')}</span>
                  <span><b>5/7</b></span>
                </div>
                <div class="progress-bar"> 
                  <div class="progres-fill" style="width: 71%;"></div>
                </div>
              </div>
            </section>
          </div>
        </div>
    </div>

    <div class="spacer-container"></div>

    <div class="card-tendencias-container">
        <section class="card-tendencias">
    <div class="icons">
      <BarChart3 size={32} strokeWidth={2} />
    </div> 
    <h2>{$_('profile.trends')}</h2>
    <div class="columns">
        <div>
              <p>{$_('profile.weeklyAverage')}</p>
              <p>{$_('profile.bestDay')}</p>
              <p>{$_('profile.currentStreak')}</p>
          </div>
          <div>
              <p>1650 kcal</p>
              <p>1800 kcal</p>
              <p>{$_('profile.timeAgo.day')}</p>
          </div>
      </div>    
      </section>
    </div>
      
</main>

<style>
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

  :global(html) {
  height:100%;
}

  .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    border: 1px solid rgba(255,255,255,0.06);
  }
  
  .main {
    max-width: 400px;
    margin: 0 auto;
    padding: 2rem 2rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

      .notification-button {
        position: relative;
        background: #eee;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .notification-button :global(svg) {
        color: #333;
    }

    .badge {
        position: absolute;
        top: -5px;
        right: -5px;
        background-color: red;
        color: white;
        border-radius: 50%;
        padding: 3px 7px;
        font-size: 10px;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
    }

    .notification-button:hover + .dropdown-content {
        display: block;
    }
.dropdown-content{
  right: 10px;
  top: 70px;
  padding: 15px;
  border-radius: 8px;
  background: white;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
  min-width: 300px;
  max-height: 400px;
  overflow-y: auto;
  display: block;
}

.dropdown-content h3 {
  margin: 0 0 15px 0;
  font-size: 16px;
  font-weight: 600;
  color: #333;
}

.notification-item {
  padding: 12px;
  border-bottom: 1px solid #eee;
  cursor: pointer;
  transition: background-color 0.2s;
}

.notification-item:hover {
  background-color: #f5f5f5;
  border-radius: 5px;
}

.notification-item:last-child {
  border-bottom: none;
}

.notification-item p {
  margin: 0 0 5px 0;
  font-size: 14px;
  color: #333;
}

.notification-time {
  font-size: 12px;
  color: #999;
}
 
.card-user-container {
  text-align: center;
  align-items: flex-start;
  background: none;  /* ajustar opacidad según prefieras */
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    margin-bottom: 18px;

    background: #ffffff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

 .card-meta h2, .card-active h2, .card-info h2, .card-progress h2 {
   color: #000;
    font-size: 1.5rem;
    margin: 0 0 1rem 0;
  }
  .card-meta p, .card-active p, .card-info p, .card-progress p {
    color: #000000;
    margin: 0;
    font-size: 1rem;
    opacity: 0.8; 
  }
.card-user {
   background: white;
    padding: 2rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
    margin: 0 auto;
    width: calc(100% - 2rem);
    flex-shrink: 0;
    border-radius: 30%;
    width: 100px;
    height: 100px;
  }

.card-user:hover {
    transform: translateY(-2px);
  }

  .card-meta {
  background: rgb(38, 92, 172);
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
    margin: 0 auto;
    max-width: 400px;
    width: 80%; /* Ajusta según tus necesidades */
    margin: 0 auto;
    overflow: hidden;
    position: relative; /* Necesario para la posicion de flechas si las agregas */
  }

.card-meta:hover {
    transform: translateY(-2px);
  }

  .card-active {
    background: rgb(38, 92, 172);;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
    margin: 0 auto;
    max-width: 400px;
    width: 80%; /* Ajusta según tus necesidades */
    margin: 0 auto;
    overflow: hidden;
    position: relative; /* Necesario para la posicion de flechas si las agregas */
  }

.card-active:hover {
    transform: translateY(-2px);
  }
  .card-info {
    background: rgb(38, 92, 172);;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
    margin: 0 auto;
    max-width: 400px;
    width: 80%; /* Ajusta según tus necesidades */
    margin: 0 auto;
    overflow: hidden;
    position: relative; /* Necesario para la posicion de flechas si las agregas */
  }

.card-info:hover {
    transform: translateY(-2px);
  }

  .columns {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
  }

  .card-progress {
    background: rgb(38, 92, 172);;
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
    margin: 0 auto;
    max-width: 400px;
    width: 80%; /* Ajusta según tus necesidades */
    margin: 0 auto;
    overflow: hidden;
    position: relative; /* Necesario para la posicion de flechas si las agregas */
  }

.card-progress:hover {
    transform: translateY(-2px);
  }


 .carousel-container {
  width: 200%; /* Ajusta según tus necesidades */
  margin: 0 auto;
  scroll-snap-type: x mandatory; /* Asegura que las cartas se alineen al hacer scroll */
  -webkit-overflow-scrolling: touch; /* Suaviza el desplazamiento en dispositivos táctiles */
  scrollbar-width: thin; /* Estilo del scrollbar para Firefox */
  }


.carousel-wrapper {
  display: flex; /* Pone las cartas en línea */
  overflow-y: auto; /* Permite el desplazamiento horizontal */
  gap: 1rem; /* Espacio entre las cartas */
  padding-bottom: 1rem; /* Espacio para el scrollbar */
}

.card-meta, .card-active, .card-info, .card-progress {
  width: 50%; /* 100% / número de imágenes */
  flex-shrink: 0; /* Evita que las imágenes se encojan */
  scroll-snap-align: start; /* Alinea cada carta al inicio del contenedor */
  box-sizing: border-box; /* Asegura que el padding y border no afecten el ancho */
  margin: 0 auto;
}

.card-tendencias-container {
  text-align: center;
  align-items: flex-start;
  background: none;  /* ajustar opacidad según prefieras */
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    margin-bottom: 18px;
    background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
  }


.card-container {
  align-items: start;
  background: none;  /* ajustar opacidad según prefieras */
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 18px;

    background: #ffffff;
    overflow-x: auto; /* Permite el desplazamiento horizontal */
    scrollbar-width: thin ; /* Estilo del scrollbar para Firefox */

}
  .card-container::-webkit-scrollbar {
    width: 8px;
  }

  .card-container::-webkit-scrollbar-thumb {
    background-color: #ccc;
    border-radius: 4px;
  }

  .spacer-container {
    height: 4vh;
  
  }

  .scroll-spacer {
    height: 60px; /* Espacio para permitir scroll hacia arriba */
    width: 60%;
    flex-shrink: 0;
  }

  h2 {
    font-size: 1.5rem;
    margin: 0.5rem 0;
    color: #333;
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
    gap: 12px;
    margin-bottom: 18px;
  }
  .back-btn {
    font-size: 1.5rem;
    color: #000000;
    text-decoration: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0 0.5rem 0 0;
    line-height: 1;
  }
  .back h1 {
    flex: 1;
    font-size: 20px;
    margin: 0;
    font-weight: 600;

  }
</style>
