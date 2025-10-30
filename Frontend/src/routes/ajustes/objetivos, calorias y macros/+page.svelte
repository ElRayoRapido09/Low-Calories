<script lang="ts">
  let showModal: boolean = false;
  let currentItem: string = '';

  // Variables para Objetivos y Calorias
  let caloriasObjetivo: number = 2000;
  let pesoObjetivo: number = 70;
  let objetivoTipo: 'ganar' | 'mantener' | 'bajar' = 'mantener'; // 'ganar', 'mantener', 'bajar'

  // Variables para Macros
  let proteinas: number = 150; // g
  let carbohidratos: number = 200; // g
  let grasas: number = 70; // g

  // Variables para Funciones Inteligentes
  let iaRecomendaciones: boolean = true;
  let iaAjustes: boolean = false;

  function openModal(item: string) {
    currentItem = item;
    showModal = true;
  }

  function closeModal(): void {
    showModal = false;
    currentItem = '';
  }
</script>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label="Volver">‹</a>
    <h1>Objetivo, Calorias y Macros</h1>
  </header>

  <section class="card">
    <ul class="list">
      <li>
        <button class="item" type="button" on:click={() => openModal('Objetivos y Calorias')}>
          <div class="left">
            <span class="icon">🔥</span>
            <span class="label">Objetivos y Calorias</span>
          </div>
          <div class="right">
            <span class="chev" aria-hidden="true">›</span>
          </div>
        </button>
      </li>

      <li>
        <button class="item" type="button" on:click={() => openModal('Macros y Tipos de dietas')}>
          <div class="left">
            <span class="icon">🍎</span>
            <span class="label">Macros y Tipos de dietas</span>
          </div>
          <div class="right">
            <span class="chev" aria-hidden="true">›</span>
          </div>
        </button>
      </li>

      <li>
        <button class="item" type="button" on:click={() => openModal('Funciones Inteligentes')}>
          <div class="left">
            <span class="icon">✨</span>
            <span class="label">Funciones Inteligentes</span>
          </div>
          <div class="right">
            <span class="chev" aria-hidden="true">›</span>
          </div>
        </button>
      </li>
    </ul>
  </section>

  {#if showModal}
    <div
      class="modal-overlay"
      role="button"
      tabindex="0"
      aria-label="Cerrar modal"
      on:click={closeModal}
      on:keydown={(e) => {
        // support Enter and Space to activate the overlay close
        if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') {
          e.preventDefault();
          closeModal();
        }
      }}
    >
      <div
        class="modal"
        role="dialog"
        aria-modal="true"
        tabindex="0"
        on:click|stopPropagation
        on:keydown={(e) => {
          // allow Escape to close the dialog
          if (e.key === 'Escape') {
            closeModal();
          }
        }}
      >
        <h2>{currentItem}</h2>
        {#if currentItem === 'Objetivos y Calorias'}
          <div class="inputs">
            <label>🎯 Objetivo: 
              <select bind:value={objetivoTipo}>
                <option value="ganar">Ganar peso</option>
                <option value="mantener">Mantener peso</option>
                <option value="bajar">Bajar peso</option>
              </select>
            </label>
            <label>🔥 Calorías objetivo: <input type="number" bind:value={caloriasObjetivo} placeholder="e.g. 2000" /></label>
            <label>⚖️ Peso objetivo (kg): <input type="number" bind:value={pesoObjetivo} placeholder="e.g. 70" /></label>
          </div>
        {:else if currentItem === 'Macros y Tipos de dietas'}
          <div class="inputs">
            <label>🍗 Proteínas (g): <input type="number" bind:value={proteinas} placeholder="e.g. 150" /></label>
            <label>🌾 Carbohidratos (g): <input type="number" bind:value={carbohidratos} placeholder="e.g. 200" /></label>
            <label>🥑 Grasas (g): <input type="number" bind:value={grasas} placeholder="e.g. 70" /></label>
          </div>
        {:else if currentItem === 'Funciones Inteligentes'}
          <div class="inputs">
            <label><input type="checkbox" bind:checked={iaRecomendaciones} /> 🤖 Recomendaciones IA</label>
            <label><input type="checkbox" bind:checked={iaAjustes} /> ⚙️ Ajustes automáticos</label>
          </div>
        {/if}
        <button on:click={closeModal}>Guardar</button>
      </div>
    </div>
  {/if}
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
  }  .app {
    max-width: 420px;
    margin: 0 auto;
    padding: 24px;
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


  .card {
    background: #ffffff;
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 18px;
    border: 1px solid #e0e0e0;
  }


  .list {
  .item {
    /* support both <li class="item"> (old) and <button class="item"> (new) */
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    cursor: pointer;
    width: 100%;
    text-align: left;
    /* reset native button appearance so styling matches the list item look */
    -webkit-appearance: none;
    appearance: none;
    border: none;
    background: transparent;
  }
    gap: 12px;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    cursor: pointer;
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

  .chev {
    color: #9b9b9b;
    font-size: 18px;
  }

  @media (prefers-color-scheme: light) {
    :global(body) {
      background: #ffffff;
      color: #111;
    }
    .item { background: #fff; color: #222; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border: 1px solid #e0e0e0; }
    .icon { color: #111; background: linear-gradient(180deg,#0066cc,#2077cd); }
  }

  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    backdrop-filter: blur(4px);
    animation: fadeIn 0.3s ease-out;
  }

  .modal {
    background: linear-gradient(135deg, #ffffff 0%, #f9f9f9 100%);
    border-radius: 16px;
    padding: 24px;
    max-width: 320px;
    width: 90%;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.2);
    animation: slideUp 0.3s ease-out;
  }

  .modal h2 {
    font-size: 22px;
    margin-bottom: 20px;
    color: #000;
    text-align: center;
    font-weight: 700;
  }

  .modal .inputs {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 24px;
  }

  .modal .inputs label {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
    font-size: 14px;
    color: #333;
    font-weight: 500;
  }

  .modal .inputs input[type="number"] {
    padding: 12px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    font-size: 16px;
    background: #fff;
    transition: border-color 0.2s, box-shadow 0.2s;
  }

  .modal .inputs input[type="number"]:focus {
    border-color: #0066cc;
    box-shadow: 0 0 0 2px rgba(0,102,204,0.2);
    outline: none;
  }

  .modal .inputs select {
    padding: 12px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    font-size: 16px;
    background: #fff;
    transition: border-color 0.2s, box-shadow 0.2s;
  }

  .modal .inputs select:focus {
    border-color: #0066cc;
    box-shadow: 0 0 0 2px rgba(0,102,204,0.2);
    outline: none;
  }

  .modal .inputs input[type="checkbox"] {
    width: 18px;
    height: 18px;
    margin-right: 8px;
  }

  .modal button {
    background: linear-gradient(135deg, #0066cc 0%, #2077cd 100%);
    color: #fff;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    width: 100%;
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .modal button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,102,204,0.3);
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
</style>