<script>
  import { _ } from 'svelte-i18n';
  import { energyUnit, convertValue, formatWithUnit } from '$lib/stores/units.js';
  
  // datos de ejemplo (sustituye por tus stores / props)
  let dateLabel = $derived($_('plan.thursday') + " 16");
  let plannedDaysText = $derived("1 / 1 " + $_('plan.dayPlanned'));
  let kcalPlanned = 2138;
  let kcalTarget = 2167;
  
  // Convertir calorías a la unidad seleccionada
  let displayPlanned = $derived(
    Math.round(convertValue(kcalPlanned, 'energy', 'kcal', $energyUnit))
  );
  
  let displayTarget = $derived(
    Math.round(convertValue(kcalTarget, 'energy', 'kcal', $energyUnit))
  );
  
  let formattedPlanned = $derived(
    formatWithUnit(displayPlanned, $energyUnit, 0)
  );
  
  let formattedTarget = $derived(
    formatWithUnit(displayTarget, $energyUnit, 0)
  );
  
  // Función para mostrar calorías con unidades
  function displayCalories(kcal) {
    const converted = convertValue(kcal, 'energy', 'kcal', $energyUnit);
    return formatWithUnit(converted, $energyUnit, 0);
  }

  const meals = [
    {
      title: "Desayuno",
      kcal: 434,
      items: [
        {
          icon: "🥚",
          name: "Huevo - Entero",
          qty: "1 unidad (55 g)",
          kcal: 79,
        },
        {
          icon: "🥓",
          name: "Jamón",
          qty: "1 rebanada (30 g)",
          kcal: 44,
        },
        {
          icon: "🥭",
          name: "Papaya",
          qty: "1 taza (160 g)",
          kcal: 69,
        },
      ],
    },
    {
      title: "Comida",
      kcal: 1104,
      items: [
        { 
          icon: "🐟", 
          name: "Atún", 
          qty: "1/2 lata (60 g)", 
          kcal: 94 
        },
        { 
          icon: "🌽", 
          name: "Elote", 
          qty: "2 taza (300 g)", 
          kcal: 
          180 
        },
      ],
    },
    {
      title: "Cena",
      kcal: 1104,
      items: [
        { 
          icon: "🥛", 
          name: "Leche de soya", 
          qty: "1 1/2 vaso (800 ml)", 
          kcal: 94 
        },
        { 
          icon: "🍪", 
          name: "Galleta de avena", 
          qty: "4 pz (300 g)", 
          kcal: 180 
        },
      ],
    },
  ];

  // control del modal
  let showModal = $state(false);

  function openConfirmModal() {
    showModal = true;
  }
  function acceptPlan() {
    showModal = false;
    // aquí ejecuta la acción real (recalcular, llamar API, navegar...)
    console.log("Aceptar: recalcular plan y aplicar cambios");
  }
  function cancelPlan() {
    showModal = false;
  }
</script>

<div class="day-view">
  <header class="header">
    <a class="back" href="/ajustes/planificador_de_comida">‹</a>
    <div class="title-wrap">
      <div class="date">{dateLabel}</div>
      <div class="sub">{plannedDaysText}</div>
    </div>
  </header>

  <nav class="mini-calendar" aria-hidden="true">
    <div class="wk">L</div>
    <div class="wk">M</div>
    <div class="wk">M</div>
    <div class="wk">J</div>
    <div class="wk">V</div>
    <div class="wk">S</div>
    <div class="wk">D</div>
    <div class="days">
      <button class="day">13</button>
      <button class="day">14</button>
      <button class="day">15</button>
      <button class="day active">16</button>
      <button class="day">17</button>
      <button class="day">18</button>
      <button class="day">19</button>
    </div>
  </nav>

  <section class="progress">
    <div class="label">{$_('plan.caloriesPlanned')}</div>
    <div class="value">
      {formattedPlanned} / {formattedTarget}
    </div>
    <div class="bar">
      <div
        class="bar-fill"
        style="width: {Math.min(kcalPlanned / kcalTarget, 1) * 100}%"
      ></div>
    </div>
  </section>

  <main class="meals">
    {#each meals as meal}
      <section class="meal">
        <div class="meal-header">
          <div>
            <div class="meal-title">{meal.title}</div>
            <div class="meal-meta">{displayCalories(meal.kcal)} | {meal.macro}</div>
          </div>
          <div class="meal-actions">⋯</div>
        </div>

        <ul class="items">
          {#each meal.items as it}
            <li class="item">
              <div class="left">
                <div class="icon">{it.icon}</div>
                <div class="info">
                  <div class="name">{it.name}</div>
                  <div class="qty">{it.qty}</div>
                </div>
              </div>
              <div class="right">
                <div class="kcal">{displayCalories(it.kcal)}</div>
                <button class="repeat" title="Repetir">⟳</button>
              </div>
            </li>
          {/each}
        </ul>

        <div class="add-row">
          <button class="add">＋ {$_('plan.add')}</button>
        </div>
      </section>
    {/each}
  </main>

  <div class="bottom-actions">
    <button class="arrows"> ← </button>
    <button class="phantom">⟲ {$_('plan.recalculate')}</button>
    <button class="danger">{$_('plan.empty')}</button>
    <button class="arrows"> → </button>
    <button class="confirm" onclick={openConfirmModal}>✔</button>
  </div>
</div>

{#if showModal}
  <div class="modal-overlay" onclick={cancelPlan} aria-hidden={!showModal}>
    <div
      class="modal"
      role="dialog"
      aria-modal="true"
      tabindex="0"
      onclick={(e) => e.stopPropagation()}
      onkeydown={(e) => {
        if (e.key === "Escape") cancelPlan();
      }}
    >
      <h2 class="modal-title">{$_('plan.completedPlan')}</h2>
      <p class="modal-body">{$_('plan.wantToFinish')}</p>
      <div class="modal-actions">
        <button class="btn-accept" onclick={() => window.location.href = '/ajustes'}>{$_('common.accept')}</button>
        <button class="btn-cancel" onclick={cancelPlan}>{$_('common.cancel')}</button>
      </div>
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
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial,
      sans-serif;
    background: #ffffff;
    color: #333;
    min-height: 100vh;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }

  .day-view {
    max-width: 420px;
    margin: 0 auto;
    padding: 16px 14px 28px;
    min-height: 100vh;
    box-sizing: border-box;
  }

  .header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
  }

  .back {
    color: #000;
    font-size: 28px;
    text-decoration: none;
    padding: 6px;
    opacity: 0.95;
  }

  .title-wrap {
    flex: 1;
    text-align: center;
  }

  .date {
    font-size: 18px;
    font-weight: 800;
    color: #000;
  }
  .sub {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
  }

  .mini-calendar {
    margin: 12px 0 6px;
    background: #f5f5f5;
    border-radius: 10px;
    padding: 6px 0;
  }

  .mini-calendar .wk {
    display: inline-block;
    width: calc(100% / 7 - 4px);
    text-align: center;
    font-size: 12px;
    color: #666;
  }
  .days {
    display: flex;
    gap: 6px;
    margin-top: 6px;
  }
  .day {
    flex: 1;
    border: none;
    background: transparent;
    color: #000;
    padding: 8px 6px;
    border-radius: 999px;
    font-weight: 700;
    cursor: pointer;
  }
  .day.active {
    background: #e3f2fd;
    border: 1px solid #005bb5;
    color: #005bb5;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    position: relative;
  }
  .day.active::after {
    content: "";
    width: 8px;
    height: 8px;
    background: #3ad85a;
    border-radius: 999px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: -8px;
  }

  .progress {
    margin: 14px 0 10px;
  }
  .progress .label {
    font-size: 14px;
    color: #666;
    margin-bottom: 6px;
  }
  .progress .value {
    font-weight: 700;
    text-align: right;
    margin-bottom: 8px;
    color: #000;
  }
  .bar {
    height: 8px;
    background: #f5f5f5;
    border-radius: 8px;
    overflow: hidden;
  }
  .bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #3ad85a, #8af27a);
    box-shadow: 0 2px 4px rgba(58, 216, 90, 0.2);
  }

  .meals {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-top: 6px;
  }

  .meal {
    background: #ffffff;
    border-radius: 12px;
    padding: 12px;
    border: 1px solid #e0e0e0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  .meal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
  }
  .meal-title {
    font-size: 20px;
    font-weight: 800;
    color: #000;
  }
  .meal-meta {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
  }
  .meal-actions {
    color: #666;
    font-size: 20px;
  }

  .items {
    list-style: none;
    padding: 0;
    margin: 6px 0 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 6px;
    border-radius: 8px;
    background: transparent;
    border-top: 1px solid #f0f0f0;
  }
  .left {
    display: flex;
    gap: 12px;
    align-items: center;
  }
  .icon {
    width: 40px;
    height: 40px;
    border-radius: 8px;
    background: #f5f5f5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
  .info .name {
    font-weight: 700;
    color: #000;
  }
  .info .qty {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
  }

  .right {
    text-align: right;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .kcal {
    font-size: 13px;
    color: #000;
  }
  .repeat {
    background: transparent;
    border: none;
    color: #666;
    font-size: 18px;
    cursor: pointer;
    padding: 6px;
  }

  .add-row {
    margin-top: 8px;
    display: flex;
  }
  .add {
    flex: 1;
    background: #f5f5f5;
    border: 1px solid #e0e0e0;
    color: #000;
    padding: 12px;
    border-radius: 10px;
    font-weight: 800;
    cursor: pointer;
  }

  .bottom-actions {
    position: sticky;
    bottom: 12px;
    display: flex;
    gap: 8px;
    margin-top: 18px;
  }
  .phantom {
    flex: 1;
    background: #f5f5f5;
    border: 1px solid #e0e0e0;
    color: #000;
    padding: 12px;
    border-radius: 10px;
    font-weight: 700;
    cursor: pointer;
  }
  .danger {
    flex: 0 0 64px;
    background: transparent;
    border: 1px solid #ff6b6b;
    color: #ff6b6b;
    border-radius: 10px;
    padding: 10px;
  }
  .confirm {
    flex: 0 0 64px;
    background: #005bb5;
    border: none;
    color: #fff;
    border-radius: 10px;
    font-weight: 800;
    padding: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    cursor: pointer;
  }

  .arrows {
    background: #f5f5f5;
    border: 1px solid #e0e0e0;
    color: #000;
    padding: 12px;
    border-radius: 10px;
    cursor: pointer;
    flex: 0 0 64px;
    font-weight: 800;
    padding: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  /* modal */
  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 60;
    padding: 20px;
    -webkit-backdrop-filter: blur(12px);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(233, 225, 225, 0.2);
  }
  .modal {
    width: 100%;
    max-width: 360px;
    background: #ffffff;
    color: #000;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    text-align: center;
  }
  .modal-title {
    font-size: 18px;
    font-weight: 800;
    margin: 6px 0 10px;
    color: #000;
  }
  .modal-body {
    color: #666;
    font-size: 14px;
    line-height: 1.4;
    margin-bottom: 18px;
  }
  .modal-actions {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .btn-accept {
    background: #005bb5;
    color: #fff;
    border: none;
    padding: 12px 16px;
    font-weight: 800;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  .btn-cancel {
    background: transparent;
    color: #666;
    border: none;
    padding: 10px 8px;
    font-size: 15px;
    cursor: pointer;
  }

  @media (max-width: 420px) {
    .modal {
      padding: 16px;
      max-width: 340px;
    }
    .modal-title {
      font-size: 16px;
    }
  }

  @media (max-width: 420px) {
    .day-view {
      padding: 12px;
    }
    .icon {
      width: 36px;
      height: 36px;
      font-size: 18px;
    }
    .date {
      font-size: 16px;
    }
  }
</style>
