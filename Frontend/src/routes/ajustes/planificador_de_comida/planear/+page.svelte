<script>
  // datos de ejemplo (sustituye por tus stores / props)
  let dateLabel = "Jueves 16";
  let plannedDaysText = "1 / 1 día planeado";
  let kcalPlanned = 2138;
  let kcalTarget = 2167;

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
  let showModal = false;

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

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

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
    <div class="label">Calorías planeadas</div>
    <div class="value">
      {kcalPlanned.toLocaleString()}/{kcalTarget.toLocaleString()} kcal
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
            <div class="meal-meta">{meal.kcal} kcal | {meal.macro}</div>
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
                <div class="kcal">{it.kcal} kcal</div>
                <button class="repeat" title="Repetir">⟳</button>
              </div>
            </li>
          {/each}
        </ul>

        <div class="add-row">
          <button class="add">＋ Agregar</button>
        </div>
      </section>
    {/each}
  </main>

  <div class="bottom-actions">
    <button class="arrows"> ← </button>
    <button class="phantom">⟲ Recalcular</button>
    <button class="danger">Vaciar</button>
    <button class="arrows"> → </button>
    <button class="confirm" on:click={openConfirmModal}>✔</button>
  </div>
</div>

{#if showModal}
  <div class="modal-overlay" on:click={cancelPlan} aria-hidden={!showModal}>
    <div
      class="modal"
      role="dialog"
      aria-modal="true"
      tabindex="0"
      on:click|stopPropagation
      on:keydown={(e) => {
        if (e.key === "Escape") cancelPlan();
      }}
    >
      <h2 class="modal-title">Plan de completados</h2>
      <p class="modal-body">¿Deseas Terminar?</p>
      <div class="modal-actions">
        <button class="btn-accept" on:click={() => window.location.href = '/ajustes'}>Aceptar</button>
        <button class="btn-cancel" on:click={cancelPlan}>Cancelar</button>
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
    background: linear-gradient(70deg, blue 0%, pink 100%);
    color: #f2f2f2;
    min-height: 100vh;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }

  .bg {
    position: fixed;
    background: linear-gradient(
      120deg,
      rgba(34, 34, 108, 0.6),
      rgba(19, 19, 58, 0.9)
    );
    z-index: -1;
    animation: slide 3s ease-in-out infinite alternate;
    background-image: linear-gradient(-60deg, rgb(38, 40, 128) 50%, #09f 50%);
    bottom: 0;
    left: -50%;
    opacity: 0.5;
    right: -50%;
    top: 0;
  }

  .bg2 {
    opacity: 0.6;
    animation-direction: alternate-reverse;
    animation-duration: 4s;
  }

  .bg3 {
    opacity: 0.5;
    animation-duration: 5s;
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
    color: #fff;
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
  }
  .sub {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.6);
    margin-top: 4px;
  }

  .mini-calendar {
    margin: 12px 0 6px;
    background: transparent;
    border-radius: 10px;
    padding: 6px 0;
  }

  .mini-calendar .wk {
    display: inline-block;
    width: calc(100% / 7 - 4px);
    text-align: center;
    font-size: 12px;
    color: rgba(255, 255, 255, 0.5);
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
    color: rgba(255, 255, 255, 0.8);
    padding: 8px 6px;
    border-radius: 999px;
    font-weight: 700;
    cursor: pointer;
  }
  .day.active {
    background: rgba(242, 201, 76, 0.08);
    border: 1px solid rgba(242, 201, 76, 0.18);
    color: #fff;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6);
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
    color: rgba(255, 255, 255, 0.7);
    margin-bottom: 6px;
  }
  .progress .value {
    font-weight: 700;
    text-align: right;
    margin-bottom: 8px;
    color: rgba(255, 255, 255, 0.9);
  }
  .bar {
    height: 8px;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 8px;
    overflow: hidden;
  }
  .bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #3ad85a, #8af27a);
    box-shadow: 0 4px 10px rgba(58, 216, 90, 0.12);
  }

  .meals {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-top: 6px;
  }

  .meal {
    background: linear-gradient(
      180deg,
      rgba(255, 255, 255, 0.02),
      rgba(255, 255, 255, 0.01)
    );
    border-radius: 12px;
    padding: 12px;
    border: 1px solid rgba(255, 255, 255, 0.03);
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
  }
  .meal-meta {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.6);
    margin-top: 4px;
  }
  .meal-actions {
    color: rgba(255, 255, 255, 0.5);
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
    border-top: 1px solid rgba(255, 255, 255, 0.02);
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
    background: rgba(255, 255, 255, 0.03);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
  .info .name {
    font-weight: 700;
  }
  .info .qty {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.6);
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
    color: rgba(255, 255, 255, 0.85);
  }
  .repeat {
    background: transparent;
    border: none;
    color: rgba(255, 255, 255, 0.6);
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
    background: rgba(255, 255, 255, 0.03);
    border: none;
    color: #fff;
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
    background: rgba(255, 255, 255, 0.03);
    border: none;
    color: rgba(255, 255, 255, 0.9);
    padding: 12px;
    border-radius: 10px;
    font-weight: 700;
    cursor: pointer;
  }
  .danger {
    flex: 0 0 64px;
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.06);
    color: #ff6b6b;
    border-radius: 10px;
    padding: 10px;
  }
  .confirm {
    flex: 0 0 64px;
    background: #0099ff;
    border: none;
    color: #000;
    border-radius: 10px;
    font-weight: 800;
    padding: 10px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6);
    cursor: pointer;
  }

  .arrows {
    background: rgba(255, 255, 255, 0.03);
    border: none;
    color: rgba(255, 255, 255, 0.9);
    padding: 12px;
    border-radius: 10px;
    cursor: pointer;

    flex: 0 0 64px;
    font-weight: 800;
    padding: 10px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6);
    cursor: pointer;
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
    background: #0099ff34;
    color: #fff;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.6);
    text-align: center;
  }
  .modal-title {
    font-size: 18px;
    font-weight: 800;
    margin: 6px 0 10px;
  }
  .modal-body {
    color: rgba(255, 255, 255, 0.8);
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
    background: #0099ff;
    color: #000;
    border: none;
    padding: 12px 16px;
    font-weight: 800;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.45);
  }
  .btn-cancel {
    background: transparent;
    color: rgba(255, 255, 255, 0.9);
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

  @keyframes slide {
    0% {
      transform: translateX(-25%);
    }
    100% {
      transform: translateX(25%);
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
