<script>
  import { _ } from 'svelte-i18n';
  import { 
    Sparkles,        //  Planificador Automático
    Calendar,        //  Planificador de Comidas
    ShoppingCart,    //  Lista de Compras
    Timer,           //  Ayuno
    Flame,           //  Objetivos, Calorías y Macros
    Apple,           //  Plan de Comidas y Alimentos
    RefreshCw,       //  Rehacer Plan
    Palette,         //  Interfaz
    Users,           //  Plan Familiar
    UserCircle,      //  Cuenta
    Search,          //  Buscar
  } from 'lucide-svelte';
</script>

<main class="app">
  <header class="top">
    <a href="/" class="back-btn" aria-label={$_('common.back')}>‹</a>
    <h1>{$_('settings.title')}</h1>
    <div class="avatar-container">
      <img class="avatar" alt={$_('settings.profile')} src="/src/lib/assets/kk.jpg"/>
    </div>
  </header>

  <h2 class="section-title">{$_('settings.quickAccess')}</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <span class="icon">
          <Sparkles size={20} strokeWidth={2} />
        </span>
        <span class="label">{$_('settings.autoPlanner')}</span>
        <label class="switch">
          <input type="checkbox" aria-label="activar planificador">
          <span class="slider"></span>
        </label>
      </li>

      <li>
        <a class="item" href="/ajustes/planificador_de_comida" aria-label={$_('settings.mealPlanner')}>
          <span class="icon">
            <Calendar size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.mealPlanner')}</span>
          <span class="chev">›</span>
        </a>
      </li>

      <li>
        <a class="item" href="/ajustes/lista de compras" aria-label={$_('settings.shoppingList')}>
          <span class="icon">
            <ShoppingCart size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.shoppingList')}</span>
          <span class="chev">›</span>
        </a>
      </li>

      <li>
        <a class="item" href="/ajustes/ayuno" aria-label={$_('settings.fasting')}>
          <span class="icon">
            <Timer size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.fasting')}</span>
          <span class="chev">›</span>
        </a>
      </li>
    </ul>
  </section>

  <h2 class="section-title">{$_('settings.configuration')}</h2>
  <section class="card">
    <ul class="list">
      <li>
        <a class="item" href="/ajustes/objetivos, calorias y macros" aria-label={$_('settings.goalCaloriesMacros')}>
          <span class="icon">
            <Flame size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.goalCaloriesMacros')}</span>
          <span class="chev">›</span>
        </a>
      </li>
      <li>
        <a class="item" href="/ajustes/plan de comidas y alimentos" aria-label={$_('settings.mealPlanFoods')}>
          <span class="icon">
            <Apple size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.mealPlanFoods')}</span>
          <span class="chev">›</span>
        </a>
      </li>
      <li>
        <a class="item" href="/objetivos" aria-label={$_('settings.redoPlan')}>
          <span class="icon">
            <RefreshCw size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.redoPlan')}</span>
          <span class="chev">›</span>
        </a>
      </li>
      <li>
        <a class="item" href="/ajustes/interfaz" aria-label={$_('settings.interface')}>
          <span class="icon">
            <Palette size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.interface')}</span>
          <span class="chev">›</span>
        </a>
      </li>
      <li>
        <a class="item" href="/premium" aria-label={$_('settings.familyPlan')}>
          <span class="icon">
            <Users size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.familyPlan')}</span>
          <span class="chev">›</span>
        </a>
      </li>
      <li>
        <a class="item" href="/ajustes/cuenta" aria-label={$_('settings.account')}>
          <span class="icon">
            <UserCircle size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('settings.account')}</span>
          <span class="chev">›</span>
        </a>
      </li>
    </ul>
  </section>

  <div class="search">
    <span class="search-icon">
      <Search size={18} strokeWidth={2} />
    </span>
    <input type="search" placeholder={$_('settings.searchPlaceholder')} aria-label="buscar ajustes">
  </div>
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

  .back-btn {
    color: #000000;
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

  .avatar-container {
    position: relative;
    width: 50px;
    height: 50px;
  }

  .avatar {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #e0e0e0;
    display: block;
  }

  /* Si la imagen no carga, mostrar un placeholder */
  .avatar-container::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    z-index: -1;
  }

  .section-title {
    color: #666;
    margin: 18px 0 8px;
    font-size: 14px;
    font-weight: 600;
  }

  .card {
    background: #ffffff;
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 18px;
    border: 1px solid #e0e0e0;
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
    border-bottom: 1px solid rgba(255,255,255,0.03);
  }

  .item:last-child {
    border-bottom: none;
  }

  .icon {
    width: 44px;
    height: 44px;
    min-width: 44px;
    border-radius: 10px;
    background: linear-gradient(180deg,#0066cc,#2077cd);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: #fff; /* Cambiado de #111 a #fff para iconos blancos */
    font-size: 18px;
  }

  .label {
    flex: 1;
    font-size: 15px;
    color: #000000;
  }

  .chev {
    color: #9b9b9b;
    font-size: 20px;
    padding-left: 8px;
  }
  /* Toggle switch estilo móvil */
  .switch {
    display: inline-block;
    width: 44px;
    height: 24px;
    position: relative;
    margin-left: 8px;
  }
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  .slider {
    position: absolute;
    cursor: pointer;
    inset: 0;
    background: rgba(0, 0, 0, 0.241);
    border-radius: 999px;
  }
  .slider::after {
    content: "";
    position: absolute;
    left: 4px;
    top: 4px;
    width: 16px;
    height: 16px;
    background: #000000;
    border-radius: 50%;
    transition: transform 0.18s;
  }
  .switch input:checked + .slider {
    background: linear-gradient(90deg,#0066cc,#0066cc71);
  }
  .switch input:checked + .slider::after {
    transform: translateX(20px);
  }

  .search {
    position: fixed;
    left: 24px;
    right: 24px;
    bottom: 18px;
    max-width: 420px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 10px;

    background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);
    
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.6);
    border: 1px solid rgba(255,255,255,0.03);
  }

  .search input {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: #ffffff;
    font-size: 14px;
  }

  .search-icon {
    color: #0066cc;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

   @media (prefers-color-scheme: light) {
    :global(body) {
      background: linear-gradient(-45deg, #FFD700 0%, #FFA500 50%, #FFFFFF 50%, #FFFFFF 100%);
      background-attachment: fixed;
      color: #111;
    }
    .card, .search { 
      background: rgba(255,255,255,0.9); 
      color: #222; 
      box-shadow: 0 8px 26px rgba(10,10,10,0.06); 
    }
    .icon { 
      color: #fff;
    }
    .label { 
      color: #000; 
    }
    .back-btn {
      color: #000;
    }
    .avatar {
      border: 2px solid #e0e0e0;
    }
  }
  

  

  @keyframes shimmer {
    0% {
      transform: translateX(100%);
    }
    100% {
      transform: translateX(-100%);
    }
  }
</style>