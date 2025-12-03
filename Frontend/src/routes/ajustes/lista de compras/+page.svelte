<script>
  import { _ } from 'svelte-i18n';
  import { massUnit, convertValue, formatWithUnit } from '$lib/stores/units.js';
  import { 
    Egg,           // Huevo
    Beef,          // Carne
    Drumstick,     // Pollo
    Ham,           // Puerco (cambiado de PiggyBank)
    Milk,          // Leche
    IceCream2,     // Yogurt (cambiado de IceCream)
    Cookie,        // Queso (Cheese no existe, usar Cookie)
    Cherry,        // Fresas (cambiado de Strawberry)
    Apple,         // Aguacate
    Calendar,      // Calendario
    Share2,        // Compartir/Exportar
  } from 'lucide-svelte';
  
  // Función para convertir masa
  function displayMass(grams) {
    const converted = convertValue(grams, 'mass', 'g', $massUnit);
    return formatWithUnit(converted, $massUnit, 1);
  }
  
  // datos de ejemplo — sustituye por tus stores/backend
  const startDate = "Jue 09 Oct";
  const endDate = "Mie 15 Oct";

  const sections = [
    {
      title: $_('shoppingList.meats'),
      items: [
        {
          icon: "egg",
          name: $_('shoppingList.egg'),
          qty: `19 ${$_('shoppingList.units')} - ${displayMass(1000)}`,
          checked: true,
        },
        { 
          icon: "beef", 
          name: $_('shoppingList.meat'), 
          qty: displayMass(150), 
          checked: true 
        },
        { 
          icon: "drumstick", 
          name: $_('shoppingList.chicken'), 
          qty: displayMass(250), 
          checked: true 
        },
        { 
          icon: "piggybank", 
          name: $_('shoppingList.pork'), 
          qty: displayMass(475), 
          checked: false 
        },
      ],
    },
    {
      title: $_('shoppingList.dairy'),
      items: [
        { 
          icon: "milk", 
          name: $_('shoppingList.milk'), 
          qty: "1.1 L", 
          checked: false 
        },
        { 
          icon: "icecream", 
          name: $_('shoppingList.yogurt'), 
          qty: "720 ml", 
          checked: false 
        },
        {
          icon: "cheese",
          name: $_('shoppingList.whiteChees'),
          qty: displayMass(75),
          checked: false,
        },
        {
          icon: "cheese",
          name: $_('shoppingList.yellowCheese'),
          qty: displayMass(75),
          checked: false,
        },
      ],
    },
    {
      title: $_('shoppingList.fruits'),
      items: [
        { 
          icon: "strawberry", 
          name: $_('shoppingList.strawberries'), 
          qty: "150 g", 
          checked: false 
        },
        {
          icon: "apple",
          name: $_('shoppingList.avocado'),
          qty: `8.8 ${$_('shoppingList.units')} - 2.1 kg`,
          checked: false,
        },
      ],
    },
  ];
</script>

<div class="page">
  <header class="header">
    <a class="back" href="/ajustes" aria-label={$_('common.back')}>‹</a>
    <h1>{$_('shoppingList.title')}</h1>

    <div class="actions">
      <button class="export-btn" aria-label={$_('shoppingList.export')}>
        <Share2 size={18} strokeWidth={2} />
      </button>
    </div>
  </header>

  <div class="date-row">
    <div class="chip">
      <div class="chip-label">{$_('shoppingList.startDate')}</div>
      <div class="chip-value">
        {startDate} 
        <span class="cal">
          <Calendar size={18} strokeWidth={2} />
        </span>
      </div>
    </div>
    <div class="chip">
      <div class="chip-label">{$_('shoppingList.endDate')}</div>
      <div class="chip-value">
        {endDate} 
        <span class="cal">
          <Calendar size={18} strokeWidth={2} />
        </span>
      </div>
    </div>
  </div>

  <main class="list">
    {#each sections as s}
      <h2 class="section-title">{s.title}</h2>
      <ul class="section">
        {#each s.items as it}
          <li class="item">
            <div class="left">
              <div class="icon">
                {#if it.icon === 'egg'}
                  <Egg size={20} strokeWidth={2} />
                {:else if it.icon === 'beef'}
                  <Beef size={20} strokeWidth={2} />
                {:else if it.icon === 'drumstick'}
                  <Drumstick size={20} strokeWidth={2} />
                {:else if it.icon === 'piggybank'}
                  <Ham size={20} strokeWidth={2} />
                {:else if it.icon === 'milk'}
                  <Milk size={20} strokeWidth={2} />
                {:else if it.icon === 'icecream'}
                  <IceCream2 size={20} strokeWidth={2} />
                {:else if it.icon === 'cheese'}
                  <Cookie size={20} strokeWidth={2} />
                {:else if it.icon === 'strawberry'}
                  <Cherry size={20} strokeWidth={2} />
                {:else if it.icon === 'apple'}
                  <Apple size={20} strokeWidth={2} />
                {/if}
              </div>
              <div class="meta">
                <div class="name">{it.name}</div>
                <div class="qty">{it.qty}</div>
              </div>
            </div>
            <button
              class:checked={it.checked}
              class="check"
              aria-pressed={it.checked}
              onclick={() => (it.checked = !it.checked)}
            >
              {#if it.checked}
                <svg
                  viewBox="0 0 24 24"
                  width="18"
                  height="18"
                  fill="none"
                >
                  <path
                    d="M20 6L9 17l-5-5"
                    stroke="#fff"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              {:else}
                <div class="circle"></div>
              {/if}
            </button>
          </li>
        {/each}
      </ul>
    {/each}
  </main>

  <div style="height:36px"></div>
</div>

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

    .page {
        max-width: 420px;
        margin: 0 auto;
        padding: 18px;
        box-sizing: border-box;
    }

    .header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }
    .back {
        color: #000;
        font-size: 28px;
        text-decoration: none;
        padding: 6px;
    }
    h1 {
        flex: 1;
        font-size: 20px;
        margin: 0;
        font-weight: 600;
        color: #000;
    }
    .actions {
        display: flex;
        gap: 8px;
        align-items: center;
    }

    .export-btn {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        color: #005bb5;
        padding: 8px 10px;
        border-radius: 12px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .date-row {
        display: flex;
        gap: 12px;
        margin: 12px 0 18px;
    }
    .chip {
        background: #ffffff;
        padding: 12px;
        border-radius: 12px;
        flex: 1;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .chip-label {
        font-size: 12px;
        color: #666;
        margin-bottom: 6px;
    }
    .chip-value {
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .cal {
        margin-left: 8px;
        opacity: 0.95;
        display: flex;
        align-items: center;
        color: #005bb5;
    }

    .list {
        display: flex;
        flex-direction: column;
        gap: 18px;
    }

    .section-title {
        margin: 0 0 8px;
        font-weight: 800;
        font-size: 16px;
        color: #000;
    }

    .section {
        list-style: none;
        margin: 0;
        padding: 0;
        border-radius: 12px;
        background: #ffffff;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        overflow: hidden;
        background: transparent;
    }
    .item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 10px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.03);
        gap: 12px;
    }
    .item:last-child {
        border-bottom: none;
    }

    .left {
        display: flex;
        gap: 12px;
        align-items: center;
        min-width: 0;
    }
    .icon {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #f5f5f5;
        color: #005bb5; /* Color azul para los iconos */
    }
    .meta .name {
        font-weight: 700;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 220px;
        color: #000;
    }
    .meta .qty {
        font-size: 13px;
        color: #666;
        margin-top: 4px;
    }

    .check {
        width: 25px;
        height: 25px;
        border-radius: 444px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: transparent;
        border: 1px solid rgba(0, 0, 0, 0.8);
        cursor: pointer;
    }
    .check.checked {
        background: linear-gradient(180deg, #2ecc71, #27ae60);
        border: none;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.8);
    }
    .check .circle {
        width: 12px;
        height: 12px;
        border-radius: 444px;
        border: 1.6px solid rgba(0, 0, 0, 0.8);
    }

    @media (max-width: 420px) {
        .page {
            padding: 14px;
        }
        h1 {
            font-size: 26px;
        }
        .meta .name {
            max-width: 160px;
        }
    }


</style>
