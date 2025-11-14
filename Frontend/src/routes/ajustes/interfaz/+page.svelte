<script>
  import { _, locale } from 'svelte-i18n';
  import { browser } from '$app/environment';
  import { massUnit, lengthUnit, energyUnit } from '$lib/stores/units.js';
  
  let currentLang = $state($locale || 'es');
  let showMassModal = $state(false);
  let showLengthModal = $state(false);
  let showEnergyModal = $state(false);
  
  function changeLanguage(lang) {
    locale.set(lang);
    currentLang = lang;
    if (browser) {
      localStorage.setItem('locale', lang);
    }
  }
  
  function changeMassUnit(unit) {
    massUnit.set(unit);
    showMassModal = false;
  }
  
  function changeLengthUnit(unit) {
    lengthUnit.set(unit);
    showLengthModal = false;
  }
  
  function changeEnergyUnit(unit) {
    energyUnit.set(unit);
    showEnergyModal = false;
  }
</script>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label={$_('common.back')}>‹</a>
    <h1>{$_('interface.title')}</h1>
  </header>

  <h2 class="section-title">Idioma</h2>
  <section class="card">
    <ul class="list">
      <li>
        <button type="button" class="item" onclick={() => changeLanguage(currentLang === 'es' ? 'en' : 'es')}>
          <div class="left">
            <span class="icon">🌐</span>
            <span class="label">{$_('interface.language')}</span>
          </div>
          <div class="right">
            <span class="value">{currentLang === 'es' ? $_('interface.spanish') : $_('interface.english')}</span>
            <span class="chev">›</span>
          </div>
        </button>
      </li>

      <li>
        <div class="item">
          <div class="left">
            <span class="icon">📚</span>
            <span class="label">{$_('interface.databaseLanguage')}</span>
          </div>
          <div class="right">
            <span class="value">{currentLang === 'es' ? $_('interface.spanish') : $_('interface.english')}</span>
            <span class="chev">›</span>
          </div>
        </div>
      </li>
    </ul>
  </section>

  <h2 class="section-title">{$_('interface.units')}</h2>
  <section class="card">
    <ul class="list">
      <li>
        <button type="button" class="item" onclick={() => showMassModal = true}>
          <div class="left">
            <span class="icon">⚖️</span>
            <span class="label">{$_('interface.massUnit')}</span>
          </div>
          <div class="right">
            <span class="value">{$massUnit}</span>
            <span class="chev">›</span>
          </div>
        </button>
      </li>

      <li>
        <button type="button" class="item" onclick={() => showLengthModal = true}>
          <div class="left">
            <span class="icon">📏</span>
            <span class="label">{$_('interface.lengthUnit')}</span>
          </div>
          <div class="right">
            <span class="value">{$lengthUnit}</span>
            <span class="chev">›</span>
          </div>
        </button>
      </li>

      <li>
        <button type="button" class="item" onclick={() => showEnergyModal = true}>
          <div class="left">
            <span class="icon">⚡</span>
            <span class="label">{$_('interface.energyUnit')}</span>
          </div>
          <div class="right">
            <span class="value">{$energyUnit}</span>
            <span class="chev">›</span>
          </div>
        </button>
      </li>
    </ul>
  </section>

  <div class="search">
    <span class="search-icon">🔍</span>
    <input type="search" placeholder={$_('interface.searchPlaceholder')} aria-label="buscar ajustes">
  </div>
</main>

<!-- Modal para unidad de masa -->
{#if showMassModal}
  <div class="modal-overlay" onclick={() => showMassModal = false} onkeydown={(e) => e.key === 'Escape' && (showMassModal = false)} role="button" tabindex="0" aria-label="Cerrar modal">
    <div class="modal" role="dialog" aria-modal="true" tabindex="-1" onclick={(e) => e.stopPropagation()}>
      <div class="modal-bar"></div>
      <h3>{$_('interface.massUnit')}</h3>
      <button class="modal-option" onclick={() => changeMassUnit('g')}>{$_('interface.massUnits.g')}</button>
      <button class="modal-option" onclick={() => changeMassUnit('kg')}>{$_('interface.massUnits.kg')}</button>
      <button class="modal-option" onclick={() => changeMassUnit('lb')}>{$_('interface.massUnits.lb')}</button>
      <button class="modal-option" onclick={() => changeMassUnit('oz')}>{$_('interface.massUnits.oz')}</button>
    </div>
  </div>
{/if}

<!-- Modal para unidad de longitud -->
{#if showLengthModal}
  <div class="modal-overlay" onclick={() => showLengthModal = false} onkeydown={(e) => e.key === 'Escape' && (showLengthModal = false)} role="button" tabindex="0" aria-label="Cerrar modal">
    <div class="modal" role="dialog" aria-modal="true" tabindex="-1" onclick={(e) => e.stopPropagation()}>
      <div class="modal-bar"></div>
      <h3>{$_('interface.lengthUnit')}</h3>
      <button class="modal-option" onclick={() => changeLengthUnit('cm')}>{$_('interface.lengthUnits.cm')}</button>
      <button class="modal-option" onclick={() => changeLengthUnit('m')}>{$_('interface.lengthUnits.m')}</button>
      <button class="modal-option" onclick={() => changeLengthUnit('ft')}>{$_('interface.lengthUnits.ft')}</button>
      <button class="modal-option" onclick={() => changeLengthUnit('in')}>{$_('interface.lengthUnits.in')}</button>
    </div>
  </div>
{/if}

<!-- Modal para unidad de energía -->
{#if showEnergyModal}
  <div class="modal-overlay" onclick={() => showEnergyModal = false} onkeydown={(e) => e.key === 'Escape' && (showEnergyModal = false)} role="button" tabindex="0" aria-label="Cerrar modal">
    <div class="modal" role="dialog" aria-modal="true" tabindex="-1" onclick={(e) => e.stopPropagation()}>
      <div class="modal-bar"></div>
      <h3>{$_('interface.energyUnit')}</h3>
      <button class="modal-option" onclick={() => changeEnergyUnit('kcal')}>{$_('interface.energyUnits.kcal')}</button>
      <button class="modal-option" onclick={() => changeEnergyUnit('kj')}>{$_('interface.energyUnits.kj')}</button>
      <button class="modal-option" onclick={() => changeEnergyUnit('cal')}>{$_('interface.energyUnits.cal')}</button>
    </div>
  </div>
{/if}

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
    color: #000;
    text-decoration: none;
    font-size: 22px;
    padding: 6px;
  }

  .top h1 {
    flex: 1;
    font-size: 20px;
    margin: 0;
    color: #000;
    font-weight: 600;
    text-align: center;
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

    background: rgba(255,255,255,0.2); /* ajuste: más opaco en modo claro si quieres */
    -webkit-backdrop-filter: blur(15px);
    backdrop-filter: blur(15px);

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
    background: none; /* ajuste: más opaco en modo claro si quieres */
    width: 100%;
    border: none;
    font-family: inherit;
    font-size: inherit;
    text-align: left;
    cursor: pointer;
  }

  button.item:hover {
    background: rgba(0, 102, 204, 0.1);
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
    color: #111;
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

  .value {
    color: #000000;
    font-size: 14px;
    margin-right: 6px;
  }

  .chev {
    color: #9b9b9b;
    font-size: 18px;
  }

  /* Switch estilo móvil (amarillo cuando está activo) */
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
  }

  @media (prefers-color-scheme: light) {
    :global(body) {
      background: #ffffff;
      color: #111;
    }
    .item, .search { background: #fff; color: #222; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border: 1px solid #e0e0e0; }
    .icon { color: #111; background: linear-gradient(180deg,#0066cc,#2077cd); }
    .value { color: #666; }
  }

  /* Estilos para modales */
  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: flex-end;
    justify-content: center;
    z-index: 1000;
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
  }

  @keyframes modalUp {
    from {
      transform: translateY(100%);
    }
    to {
      transform: translateY(0);
    }
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
  }

  .modal-option {
    width: 100%;
    background: rgba(255, 255, 255, 0.1);
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
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    font-family: inherit;
  }

  .modal-option:hover {
    background: #f0f0f0;
    color: #000;
  }
</style>