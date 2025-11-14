<script lang="ts">
  import { _ } from 'svelte-i18n';
  
  let ayuno16: number = 16;
  let comida16: number = 8;
  let ayuno14: number = 14;
  let comida14: number = 10;
  let ayuno12: number = 12;
  let comida12: number = 12;
  let ayunoPersonal: number | string = '';
  let comidaPersonal: number | string = '';

  let dateStart16: string = '';
  let dateEnd16: string = '';
  let dateStart14: string = '';
  let dateEnd14: string = '';
  let dateStart12: string = '';
  let dateEnd12: string = '';
  let dateStartPersonal: string = '';
  let dateEndPersonal: string = '';

  let showModal: boolean = false;
  let currentPlan: string = '';
  let tempAyuno: string = '';
  let tempComida: string = '';
  let tempDateStart: string = '';
  let tempDateEnd: string = '';

  function openModal(plan: string): void {
    currentPlan = plan;
    tempAyuno = String(getAyuno(plan) || '');
    tempComida = String(getComida(plan) || '');
    tempDateStart = getDateStart(plan);
    tempDateEnd = getDateEnd(plan);
    showModal = true;
  }

  function closeModal(): void {
    setAyuno(currentPlan, Number(tempAyuno));
    setComida(currentPlan, Number(tempComida));
    setDateStart(currentPlan, tempDateStart);
    setDateEnd(currentPlan, tempDateEnd);
    showModal = false;
    currentPlan = '';
  }

  function getAyuno(plan: string): number | string | undefined {
    if (plan === '16:8') return ayuno16;
    if (plan === '14:10') return ayuno14;
    if (plan === '12:12') return ayuno12;
    if (plan === 'Personalizado') return ayunoPersonal;
  }

  function setAyuno(plan: string, value: number | string): void {
    if (plan === '16:8') ayuno16 = Number(value);
    if (plan === '14:10') ayuno14 = Number(value);
    if (plan === '12:12') ayuno12 = Number(value);
    if (plan === 'Personalizado') ayunoPersonal = value;
  }

  function getComida(plan: string): number | string | undefined {
    if (plan === '16:8') return comida16;
    if (plan === '14:10') return comida14;
    if (plan === '12:12') return comida12;
    if (plan === 'Personalizado') return comidaPersonal;
  }

  function setComida(plan: string, value: number | string): void {
    if (plan === '16:8') comida16 = Number(value);
    if (plan === '14:10') comida14 = Number(value);
    if (plan === '12:12') comida12 = Number(value);
    if (plan === 'Personalizado') comidaPersonal = value;
  }

  function getDateStart(plan: string): string {
    if (plan === '16:8') return dateStart16;
    if (plan === '14:10') return dateStart14;
    if (plan === '12:12') return dateStart12;
    if (plan === 'Personalizado') return dateStartPersonal;
    return '';
  }

  function setDateStart(plan: string, value: string): void {
    if (plan === '16:8') dateStart16 = value;
    if (plan === '14:10') dateStart14 = value;
    if (plan === '12:12') dateStart12 = value;
    if (plan === 'Personalizado') dateStartPersonal = value;
  }
  function getDateEnd(plan: string): string {
    if (plan === '16:8') return dateEnd16;
    if (plan === '14:10') return dateEnd14;
    if (plan === '12:12') return dateEnd12;
    if (plan === 'Personalizado') return dateEndPersonal;
    return '';
  }

  function setDateEnd(plan: string, value: string): void {
    if (plan === '16:8') dateEnd16 = value;
    if (plan === '14:10') dateEnd14 = value;
    if (plan === '12:12') dateEnd12 = value;
    if (plan === 'Personalizado') dateEndPersonal = value;
  }
</script>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label={$_('common.back')}>‹</a>
    <h1>{$_('fasting.title')}</h1>
  </header>

  <button type="button" class="card-plan popular" onclick={() => openModal('16:8')}>
    <div class="left">
      <div class="title">16:8</div>
      <p class="desc">{$_('fasting.plan168')}</p>
    </div>
  </button>

  <button type="button" class="card-plan" onclick={() => openModal('14:10')}>
    <div class="title">14:10</div>
    <p class="desc">{$_('fasting.plan1410')}</p>
  </button>

  <button type="button" class="card-plan" onclick={() => openModal('12:12')}>
    <div class="title">12:12</div>
    <p class="desc">{$_('fasting.plan1212')}</p>
  </button>

  <button type="button" class="card-plan" onclick={() => openModal('Personalizado')}>
    <div class="title">{$_('fasting.custom')}</div>
    <p class="desc">{$_('fasting.customDesc')}</p>
  </button>

  <div style="height:40px"></div>

  {#if showModal}
    <div
      class="modal-overlay"
      role="button"
      tabindex="0"
      aria-label={$_('fasting.closeModal')}
      onclick={closeModal}
      onkeydown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); closeModal(); } }}
    >
      <div
        class="modal"
        role="dialog"
        aria-modal="true"
        tabindex="-1"
        onclick={(e) => e.stopPropagation()}
        onkeydown={(e) => { if (e.key === 'Escape') { e.preventDefault(); closeModal(); } }}
      >
        <h2>{currentPlan === 'Personalizado' ? $_('fasting.custom') : currentPlan}</h2>
        <div class="inputs">
          <label>{$_('fasting.fastingHours')}: <input type="number" bind:value={tempAyuno} readonly={currentPlan !== 'Personalizado'} /></label>
          <label>{$_('fasting.eatingHours')}: <input type="number" bind:value={tempComida} readonly={currentPlan !== 'Personalizado'} /></label>
          <label>{$_('fasting.startDate')}: <input type="date" bind:value={tempDateStart} /></label>
          <label>{$_('fasting.endDate')}: <input type="date" bind:value={tempDateEnd} /></label>
        </div>
        <button onclick={closeModal}>{$_('fasting.select')}</button>
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
  }

  .app {
    max-width: 420px;
    margin: 0 auto;
    padding: 20px;
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
    font-size: 26px;
    padding: 6px;
    opacity: 0.95;
  }

  .top h1 {
    flex: 1;
    font-size: 28px;
    margin: 0;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #000;
  }

  .card-plan {
    background: #ffffff;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    border: 1px solid #e0e0e0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    position: relative;
    cursor: pointer;
  }

  .card-plan.popular {
    background: #ffffff;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    border: 1px solid #e0e0e0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    position: relative;
    cursor: pointer;
  }

  .card-plan .title {
    font-size: 20px;
    font-weight: 800;
    color: #000;
    margin-bottom: 6px;
  }

  .card-plan .desc {
    font-size: 14px;
    color: #666;
    line-height: 1.45;
    margin: 0;
  }

  .inputs {
    display: flex;
    gap: 10px;
    margin-top: 10px;
    flex-wrap: wrap;
  }

  .inputs label {
    font-size: 14px;
    color: #666;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .inputs input {
    width: 60px;
    padding: 4px;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    font-size: 14px;
  }

  /* apariencia de tarjetas grandes como en la imagen */
  @media (min-width: 360px) {
    .card-plan { padding: 20px; }
    .card-plan .title { font-size: 22px; }
  }

  /* esquema claro opcional */
  @media (prefers-color-scheme: light) {
    :global(body) { background: linear-gradient(180deg,#f7f7fb,#ffffff); color: #111; }
    .card-plan { background: #1f2937; color: #fff; }
  }

  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }

  .modal {
    background: #ffffff;
    border-radius: 12px;
    padding: 20px;
    max-width: 300px;
    width: 90%;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  }

  .modal h2 {
    font-size: 24px;
    margin-bottom: 16px;
    color: #000;
  }

  .modal .inputs {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 20px;
  }

  .modal button {
    background: #000;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    width: 100%;
  }
</style>