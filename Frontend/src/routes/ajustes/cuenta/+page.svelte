<script>
  import { _ } from 'svelte-i18n';
  import { lengthUnit, convertValue, formatWithUnit } from '$lib/stores/units.js';
  import { 
    Plus,          // Edad
    Ruler,         // Altura
    Users,         // Sexo
    FileText,      // Administrar suscripción
    User,          // ID Usuario
    Mail,          // Email
    Key,           // Actualizar contraseña
    FileCheck,     // Términos de Servicio
    Search,        // Buscar
  } from 'lucide-svelte';
  
  // Valores de ejemplo almacenados en la base de datos (siempre en unidades base)
  let heightInCm = $state(180); // Altura almacenada en cm
  
  // Calcular altura en la unidad seleccionada
  let displayHeight = $derived(
    convertValue(heightInCm, 'length', 'cm', $lengthUnit)
  );
  
  let formattedHeight = $derived(
    formatWithUnit(displayHeight, $lengthUnit, 1)
  );
</script>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label={$_('common.back')}>‹</a>
    <h1>{$_('account.title')}</h1>
  </header>

  <h2 class="section-title">{$_('account.personalInfo')}</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <div class="left">
          <span class="icon">
            <Plus size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.age')}</span>
        </div>
        <div class="right">
          <span class="value">30 {$_('account.years')}</span>
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">
            <Ruler size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.height')}</span>
        </div>
        <div class="right">
          <span class="value">{formattedHeight}</span>
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">
            <Users size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.gender')}</span>
        </div>
        <div class="right">
          <span class="value">{$_('account.male')}</span>
          <span class="chev">›</span>
        </div>
      </li>
    </ul>
  </section>

  <h2 class="section-title">{$_('account.accountSection')}</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <div class="left">
          <span class="icon">
            <FileText size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.manageSubscription')}</span>
        </div>
        <div class="right">
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">
            <User size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.userId')}</span>
        </div>
        <div class="right">
          <span class="value">8w46gfbd-4%G$%njrebhej</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">
            <Mail size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.email')}</span>
        </div>
        <div class="right">
          <span class="value">kevin@gmail.com</span>
        </div>
      </li>

      <li class="item">
        <div class="left">
          <span class="icon">
            <Key size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.updateCredentials')}</span>
        </div>
        <div class="right">
          <span class="chev">›</span>
        </div>
      </li>

      <li class="item">
        <div>
          <a class="left" href="/login/" aria-label={$_('account.logout')}>
            <span class="label">{$_('account.logout')}</span>
          </a>
        </div>
      </li>
    </ul>
  </section>

  <h2 class="section-title">{$_('account.other')}</h2>
  <section class="card">
    <ul class="list">
      <li class="item">
        <div class="left">
          <span class="icon">
            <FileCheck size={20} strokeWidth={2} />
          </span>
          <span class="label">{$_('account.termsOfService')}</span>
        </div>
        <div class="right">
          <span class="chev">›</span>
        </div>
      </li>
    </ul>  
  </section>

 <!-- Separacion -->
  <section class="space">  
  </section>

  <section class="card">
    <ul class="list">
      <li class="item">
        <div class="left">
          <span class="label-red">{$_('account.deleteAccount')}</span>
        </div>
      </li>
    </ul>  
  </section>

  <!-- Separacion -->
  <section class="card card--isolated">
  </section>
  
  <div class="search">
    <span class="search-icon">
      <Search size={18} strokeWidth={2} />
    </span>
    <input type="search" placeholder={$_('interface.searchPlaceholder')} aria-label={$_('interface.searchPlaceholder')}>
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


  .card--isolated {
  margin-top: 28px;
  margin-bottom: 36px;
  background: #fff;
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
    color: #000;
    text-decoration: none;
    font-size: 22px;
    padding: 6px;
  }

  .top h1 {
    flex: 1;
    font-size: 20px;
    margin: 0;
    font-weight: 600;
    text-align: center;
    color: #000;
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

  /* Cada fila como tarjeta redondeada (separadas entre sí) */
  .item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
  }

  .item:last-child {
    margin-bottom: 0;
  }

  .left {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
  }

  .right {
    display: flex;
    align-items: center;
    gap: 8px;
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
    flex-shrink: 0;
  }

  .label {
    flex: 1;
    font-size: 15px;
    color: #000000;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .label-red {
    flex: 1;
    font-size: 15px;
    color: #db0404;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .value {
    color: #000000;
    font-size: 14px;
    margin-right: 6px;
  }

  .chev {
    color: #9b9b9b;
    font-size: 18px;
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
    background: #ffffff;
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    border: 1px solid #e0e0e0;
  }


  .search input {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: #333;
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
      background: #ffffff;
      color: #111;
    }
    .item, .search { 
      background: #fff; 
      color: #222; 
      box-shadow: 0 2px 8px rgba(0,0,0,0.1); 
      border: 1px solid #e0e0e0; 
    }
    .icon { 
      color: #fff; /* Iconos blancos en modo claro también */
      background: linear-gradient(180deg,#0066cc,#2077cd); 
    }
    .value { 
      color: #666; 
    }
  }
</style>