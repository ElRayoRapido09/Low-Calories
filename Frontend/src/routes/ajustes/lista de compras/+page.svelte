<script>
    // datos de ejemplo — sustituye por tus stores/backend
    const startDate = "Jue 09 Oct";
    const endDate = "Mie 15 Oct";

    const sections = [
        {
            title: "Carnes, Aves y Pescados",
            items: [
                {
                    icon: "🥚",
                    name: "Huevo - Entero",
                    qty: "19 unidad - 1.0 kg",
                    checked: true,
                },
                { 
                    icon: "🥩", 
                    name: "Carne", 
                    qty: "150 g", 
                    checked: true 
                },
                { 
                    icon: "🍗", 
                    name: "Pollo", 
                    qty: "250 g", 
                    checked: true 
                },
                { 
                    icon: "🐖", 
                    name: "Puerco", 
                    qty: "475 g", 
                    checked: true 
                },
            ],
        },
        {
            title: "Lácteos y Embutidos",
            items: [
                { 
                    icon: "🥛", 
                    name: "Leche", 
                    qty: "1.1 L", 
                    checked: false 
                },
                { 
                    icon: "🍦", 
                    name: "Yogurt", 
                    qty: "720 ml", 
                    checked: false 
                },
                {
                    icon: "🧀",
                    name: "Queso Blanco",
                    qty: "75 g",
                    checked: false,
                },
                {
                    icon: "🧀",
                    name: "Queso Amarillo",
                    qty: "75 g",
                    checked: false,
                },
            ],
        },
        {
            title: "Frutas",
            items: [
                { icon: "🍓", name: "Fresas", qty: "150 g", checked: false },
                {
                    icon: "🥑",
                    name: "Aguacate",
                    qty: "8.8 unidad - 2.1 kg",
                    checked: false,
                },
            ],
        },
    ];
</script>


<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<div class="page">
    <header class="header">
        <a class="back" href="/ajustes" aria-label="Volver">‹</a>
        <h1>Lista de Compras</h1>

        <div class="actions">
            <button class="export-btn" aria-label="Exportar">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none"
                    ><path
                        d="M12 16V4"
                        stroke="currentColor"
                        stroke-width="1.6"
                        stroke-linecap="round"
                    /><path
                        d="M8 8l4-4 4 4"
                        stroke="currentColor"
                        stroke-width="1.6"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    /><rect
                        x="3"
                        y="12"
                        width="18"
                        height="8"
                        rx="2"
                        stroke="currentColor"
                        stroke-width="1.2"
                    /></svg
                >
            </button>
        </div>
    </header>

    <div class="date-row">
        <div class="chip">
            <div class="chip-label">Fecha inicial</div>
            <div class="chip-value">
                {startDate} <span class="cal">📅</span>
            </div>
        </div>
        <div class="chip">
            <div class="chip-label">Fecha final</div>
            <div class="chip-value">{endDate} <span class="cal">📅</span></div>
        </div>
    </div>

    <main class="list">
        {#each sections as s}
            <h2 class="section-title">{s.title}</h2>
            <ul class="section">
                {#each s.items as it}
                    <li class="item">
                        <div class="left">
                            <div class="icon">{it.icon}</div>
                            <div class="meta">
                                <div class="name">{it.name}</div>
                                <div class="qty">{it.qty}</div>
                            </div>
                        </div>
                        <button
                            class:checked={it.checked}
                            class="check"
                            aria-pressed={it.checked}
                            on:click={() => (it.checked = !it.checked)}
                        >
                            {#if it.checked}
                                <svg
                                    viewBox="0 0 24 24"
                                    width="18"
                                    height="18"
                                    fill="none"
                                    ><path
                                        d="M20 6L9 17l-5-5"
                                        stroke="#fff"
                                        stroke-width="2"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                    /></svg
                                >
                            {:else}
                                <div class="circle" />
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
        background: linear-gradient(70deg, rgb(123, 0, 255) 0%, rgb(155, 44, 120) 100%);
        color: #f2f2f2;
        min-height: 100vh;
        overflow-y: auto;
        -webkit-overflow-scrolling: touch;
    }

    .bg {
        animation:slide 3s ease-in-out infinite alternate;
        background-image: linear-gradient(-60deg, rgb(204, 51, 161) 50%, rgba(83, 8, 176, 0.845) 50%);
        bottom:0;   
        left:-50%;
        opacity:.5;
        position:fixed;
        right:-50%;
        top:0;
        z-index:-1;
    }

    .bg2 {
        animation-direction:alternate-reverse;
        animation-duration:4s;
    }

    .bg3 {
        animation-duration:5s;
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
        color: #fff;
        font-size: 28px;
        text-decoration: none;
        padding: 6px;
    }
    h1 {
        flex: 1;
        font-size: 20px;
        margin: 0;
        font-weight: 600;
    }
    .actions {
        display: flex;
        gap: 8px;
        align-items: center;
    }

    .export-btn {
        background: rgba(255, 255, 255, 0.06);
        border: none;
        color: #fff;
        padding: 8px 10px;
        border-radius: 12px;
        cursor: pointer;
    }

    .date-row {
        display: flex;
        gap: 12px;
        margin: 12px 0 18px;
    }
    .chip {
        background: linear-gradient(
            180deg,
            rgba(126, 126, 126, 0.3),
            rgba(126, 126, 126, 0.3)
        );
        padding: 12px;
        border-radius: 12px;
        flex: 1;
        border: 1px solid rgba(255, 255, 255, 0.03);
    }
    .chip-label {
        font-size: 12px;
        color: rgba(255, 255, 255, 0.6);
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
    }

    .section {
        list-style: none;
        margin: 0;
        padding: 0;
        border-radius: 12px;
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
        background: rgba(255, 255, 255, 0.03);
        font-size: 18px;
    }
    .meta .name {
        font-weight: 700;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 220px;
    }
    .meta .qty {
        font-size: 13px;
        color: rgba(255, 255, 255, 0.6);
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

    @keyframes slide {
        0% {
        transform:translateX(-25%);
        }
        100% {
        transform:translateX(25%);
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
