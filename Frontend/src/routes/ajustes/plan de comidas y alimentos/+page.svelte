<script>
    import { tick } from "svelte";

    // overlay focus element
    let overlayEl;

    // Alimentos overlay
    let showFoods = false;
    async function openFoods() {
        closeAll();
        showFoods = true;
        await tick();
        if (overlayEl) overlayEl.focus();
    }
    function closeFoods() {
        showFoods = false;
    }

    // generic keyboard close
    function handleKeyDown(e) {
        if (e.key === "Escape") closeAll();
    }

    // Overlays: Variedad, Número de comidas, Tipos de Sugerencias
    let showVariety = false;
    let showNumMeals = false;
    let showSuggestions = false;

    // Variedad
    let variety = "Variedad Moderada"; // default
    const varietyOptions = [
        {
            id: "mucho",
            title: "Mucha Variedad",
            desc: "Ideal si te gusta preparar diferentes platos cada día",
        },
        {
            id: "moderada",
            title: "Variedad Moderada",
            desc: "Buena si te gusta repetir platos pero también quieres algo de variedad",
        },
        {
            id: "poca",
            title: "Poca Variedad",
            desc: "Perfecta para hacer más fácil la planificación de comidas",
        },
    ];

    async function openVariety() {
        closeAll();
        showVariety = true;
        await tick();
        if (overlayEl) overlayEl.focus();
    }

    function selectVariety(id) {
        const opt = varietyOptions.find((o) => o.id === id);
        if (opt) variety = opt.title;
        showVariety = false;
    }

    // Número de comidas
    let meals = [
        { name: "Desayuno", enabled: true, kcal: 677 },
        { name: "Comida", enabled: true, kcal: 880 },
        { name: "Cena", enabled: true, kcal: 609 },
        { name: "Snacks", enabled: false, kcal: 0 },
        ];

    function openNumMeals() {
        closeAll();
        showNumMeals = true;
        tick().then(() => overlayEl && overlayEl.focus());
    }

    function toggleMeal(i) {
        meals[i].enabled = !meals[i].enabled;
    }

    function totalKcal() {
        return meals.filter((m) => m.enabled).reduce((s, m) => s + m.kcal, 0);
    }

    

    

    // Tipos de sugerencias
    let suggestions = { simple: true, recipes: false };

    function openSuggestions() {
        closeAll();
        showSuggestions = true;
        tick().then(() => overlayEl && overlayEl.focus());
    }

    function toggleSuggestion(key) {
        suggestions[key] = !suggestions[key];
    }

    function closeAll() {
        showFoods = false;
        showVariety = false;
        showNumMeals = false;
        showSuggestions = false;
    }

    // Selección de alimentos por comida
    let showMealFoods = false;
    let currentMeal = '';
    const foodCategories = {
        Proteínas: [
            'Pollo','Carne','Pescado','Atún','Camarones','Huevo - Entero','Huevo - Clara','Pavo','Puerco','Jamón','Tofu','Carne de Soya','Tempeh','Seitán','Proteína en Polvo'
        ],
        Carbs: ['Arroz','Papa','Camote','Yuca','Lentejas','Frijoles','Garbanzos','Chícharos','Quinua']
    };

    // mapa mealName -> Set(selected foods)
    let mealSelections = {};

    async function openMealFoods(mealName) {
        closeAll();
        showMealFoods = true;
        currentMeal = mealName;
        if (!mealSelections[currentMeal]) mealSelections[currentMeal] = new Set();
        await tick();
        if (overlayEl) overlayEl.focus();
    }

    function closeMealFoods() {
        showMealFoods = false;
    }

    function toggleFood(food) {
        const set = mealSelections[currentMeal] || new Set();
        if (set.has(food)) set.delete(food);
        else set.add(food);
        // reassign to trigger reactivity
        mealSelections = { ...mealSelections, [currentMeal]: set };
    }

    function selectAllCategory(cat) {
        const list = foodCategories[cat] || [];
        const set = new Set(mealSelections[currentMeal] || []);
        list.forEach(f => set.add(f));
        mealSelections = { ...mealSelections, [currentMeal]: set };
    }
</script>

<main class="app">
    <header class="top">
        <a href="/ajustes" class="back-btn" aria-label="Volver">‹</a>
        <h1>Plan de comidas</h1>
    </header>

    <section class="card">
        <ul class="list">
            <li class="item">
                <button
                    class="item-btn"
                    on:click={openFoods}
                    aria-label="Abrir Alimentos"
                >
                    <div class="left">
                        <span class="icon">🍎</span>
                        <span class="label">Alimentos</span>
                    </div>
                    <div class="right">
                        <span class="value">3</span>
                        <span class="chev">›</span>
                    </div>
                </button>
            </li>

            <li class="item">
                <button
                    class="item-btn"
                    on:click={openVariety}
                    aria-label="Abrir Variedad"
                >
                    <div class="left">
                        <span class="icon">🌱</span>
                        <div>
                            <div class="label">Variedad</div>
                            <div class="sub">{variety}</div>
                        </div>
                    </div>
                    <div class="right">
                        <span class="chev">›</span>
                    </div>
                </button>
            </li>

            <li class="item">
                <button
                    class="item-btn"
                    on:click={openNumMeals}
                    aria-label="Abrir número de comidas"
                >
                    <div class="left">
                        <span class="icon">🍔</span>
                        <div>
                            <div class="label">Número de comidas</div>
                            <div class="sub">
                                {meals.filter((m) => m.enabled).length} comidas
                            </div>
                        </div>
                    </div>
                    <div class="right">
                        <span class="chev">›</span>
                    </div>
                </button>
            </li>

            <li class="item">
                <button
                    class="item-btn"
                    on:click={openSuggestions}
                    aria-label="Abrir tipos de sugerencias"
                >
                    <div class="left">
                        <span class="icon">✨</span>
                        <div>
                            <div class="label">Tipos de Sugerencias</div>
                            <div class="sub">
                                {suggestions.simple
                                    ? "Alimentos Simples"
                                    : ""}{suggestions.simple &&
                                suggestions.recipes
                                    ? " • "
                                    : ""}{suggestions.recipes ? "Recetas" : ""}
                            </div>
                        </div>
                    </div>
                    <div class="right">
                        <span class="chev">›</span>
                    </div>
                </button>
            </li>
        </ul>
    </section>
</main>

{#if showFoods}
    <div
        class="overlay"
        on:click|self={closeFoods}
        role="dialog"
        aria-modal="true"
        tabindex="-1"
        bind:this={overlayEl}
        on:keydown={handleKeyDown}
    >
        <div class="overlay-card" role="document">
            <header class="overlay-top">
                <button
                    class="back-btn overlay-back"
                    on:click={closeFoods}
                    aria-label="Cerrar">‹</button
                >
                <h1>Alimentos</h1>
            </header>

            <ul class="list foods-list">
                <li class="item food-item">
                    <button class="item-btn" on:click={() => openMealFoods('Desayuno')} aria-label="Abrir alimentos Desayuno">
                        <div class="left"><span class="label">Desayuno</span></div>
                        <div class="right"><span class="value">37</span><span class="chev">›</span></div>
                    </button>
                </li>

                <li class="item food-item">
                    <button class="item-btn" on:click={() => openMealFoods('Comida')} aria-label="Abrir alimentos Comida">
                        <div class="left"><span class="label">Comida</span></div>
                        <div class="right"><span class="value">35</span><span class="chev">›</span></div>
                    </button>
                </li>

                <li class="item food-item">
                    <button class="item-btn" on:click={() => openMealFoods('Cena')} aria-label="Abrir alimentos Cena">
                        <div class="left"><span class="label">Cena</span></div>
                        <div class="right"><span class="value">42</span><span class="chev">›</span></div>
                    </button>
                </li>
            </ul>
        </div>
    </div>
{/if}

{#if showMealFoods}
    <div
        class="overlay"
        on:click|self={closeMealFoods}
        role="dialog"
        aria-modal="true"
        tabindex="-1"
        bind:this={overlayEl}
        on:keydown={handleKeyDown}
    >
        <div class="overlay-card" role="document">
            <header class="overlay-top">
                <button
                    class="back-btn overlay-back"
                    on:click={closeMealFoods}
                    aria-label="Cerrar">‹</button
                >
                <h1>Alimentos para {currentMeal}</h1>
            </header>

            <p class="small-desc">Fitia construirá tus comidas solo con los alimentos seleccionados</p>

            {#each Object.keys(foodCategories) as cat}
                <div class="foods-section">
                    <div class="section-head">
                        <strong>{cat}</strong>
                        <button class="select-all" on:click={() => selectAllCategory(cat)}>Seleccionar todo</button>
                    </div>
                    <div class="chips">
                        {#each foodCategories[cat] as food}
                            <button
                                class="chip"
                                class:selected={mealSelections[currentMeal] && mealSelections[currentMeal].has(food)}
                                on:click={() => toggleFood(food)}
                                aria-pressed={mealSelections[currentMeal] && mealSelections[currentMeal].has(food)}
                            >
                                {food}
                            </button>
                        {/each}
                    </div>
                </div>
            {/each}

        </div>
    </div>
{/if}

{#if showVariety}
    <div
        class="overlay"
        on:click|self={() => (showVariety = false)}
        role="dialog"
        aria-modal="true"
        tabindex="-1"
        bind:this={overlayEl}
        on:keydown={handleKeyDown}
    >
        <div class="overlay-card" role="document">
            <header class="overlay-top">
                <button
                    class="back-btn overlay-back"
                    on:click={() => (showVariety = false)}
                    aria-label="Cerrar">‹</button
                >
                <h1>¿Cuánta variedad te gustaría en tus comidas?</h1>
            </header>

            <div class="variety-list">
                {#each varietyOptions as opt}
                    <button
                        class="option-card"
                        class:selected={variety === opt.title}
                        on:click={() => selectVariety(opt.id)}
                        aria-pressed={variety === opt.title}
                    >
                        <div class="option-left">
                            <div class="icon small">🍽️</div>
                            <div>
                                <div class="opt-title">{opt.title}</div>
                                <div class="opt-desc">{opt.desc}</div>
                            </div>
                        </div>
                    </button>
                {/each}
            </div>
        </div>
    </div>
{/if}

{#if showNumMeals}
    <div
        class="overlay"
        on:click|self={() => (showNumMeals = false)}
        role="dialog"
        aria-modal="true"
        tabindex="-1"
        bind:this={overlayEl}
        on:keydown={handleKeyDown}
    >
        <div class="overlay-card" role="document">
            <header class="overlay-top">
                <button
                    class="back-btn overlay-back"
                    on:click={() => (showNumMeals = false)}
                    aria-label="Cerrar">‹</button
                >
                <h1>Número de comidas</h1>
            </header>

            <ul class="meals-list">
                {#each meals as m, i}
                    <li class="meal-row">
                        <div class="meal-left">
                            <div class="drag">≡</div>
                            <button
                                class="switch"
                                class:on={m.enabled}
                                on:click={() => toggleMeal(i)}
                                aria-pressed={m.enabled}
                                aria-label={`Activar ${m.name}`}
                            >
                                <span class="dot"></span>
                            </button>
                            <div class="meal-info">
                                <div class="label">{m.name}</div>
                                <div class="sub">{m.kcal} kcal</div>
                            </div>
                        </div>
                        
                    </li>
                {/each}
            </ul>

            <div class="meals-footer">
                <div class="total">
                    Total <span class="total-val">{totalKcal()} kcal</span>
                </div>
            </div>
        </div>
    </div>
{/if}

{#if showSuggestions}
    <div
        class="overlay"
        on:click|self={() => (showSuggestions = false)}
        role="dialog"
        aria-modal="true"
        tabindex="-1"
        bind:this={overlayEl}
        on:keydown={handleKeyDown}
    >
        <div class="overlay-card" role="document">
            <header class="overlay-top">
                <button
                    class="back-btn overlay-back"
                    on:click={() => (showSuggestions = false)}
                    aria-label="Cerrar">‹</button
                >
                <h1>Tipo de sugerencias</h1>
            </header>

            <section class="suggestion-section">
                <h3>Alimentos Simples</h3>
                <p>
                    Te indicaremos los alimentos base, los cuales podrás cocinar
                    como prefieras. Ejemplo:
                </p>
                <div class="example">🥚 Huevo - 2 unidades</div>
                <button
                    class="switch small"
                    class:on={suggestions.simple}
                    on:click={() => toggleSuggestion("simple")}
                    aria-pressed={suggestions.simple}
                ></button>
            </section>

            <section class="suggestion-section">
                <h3>Recetas</h3>
                <p>
                    Te indicaremos platos con instrucciones detalladas. Ejemplo:
                </p>
                <div class="example">🍳 Omelette de huevo con pan tostado</div>
                <button
                    class="switch small"
                    class:on={suggestions.recipes}
                    on:click={() => toggleSuggestion("recipes")}
                    aria-pressed={suggestions.recipes}
                ></button>
            </section>
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
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
            Arial, sans-serif;
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
            /* make the button visually just the symbol: transparent background, no border */
            padding: 0 6px;
            background: transparent;
            border: none;
            box-shadow: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            line-height: 1;
            /* keep accessible focus outline */
        }

        .back-btn:focus-visible {
            outline: 2px solid rgba(0,0,0,0.12);
            outline-offset: 2px;
    }

    .top h1 {
        flex: 1;
        font-size: 20px;
        margin: 0;
        color: #000;
        font-weight: 600;
        text-align: center;
    }

    .card {
        background: #ffffff;
        border-radius: 12px;
        padding: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 18px;
        border: 1px solid #e0e0e0;

        background: rgba(
            255,
            255,
            255,
            0.2
        ); /* ajuste: más opaco en modo claro si quieres */
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
        background: linear-gradient(180deg, #0066cc, #2077cd);
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

    @media (prefers-color-scheme: light) {
        :global(body) {
            background: #ffffff;
            color: #111;
        }
        .item {
            background: #fff;
            color: #222;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            border: 1px solid #e0e0e0;
        }
        .icon {
            color: #111;
            background: linear-gradient(180deg, #0066cc, #2077cd);
        }
        .value {
            color: #666;
        }
    }

    /* Styles for the new overlay and item button */
    .item-btn {
        all: unset;
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        padding: 12px;
        border-radius: 12px;
        cursor: pointer;
    }

    .overlay {
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.45);
        display: flex;
        align-items: flex-start;
        justify-content: center;
        padding: 28px 12px;
        z-index: 60;
    }

    .overlay-card {
        width: 100%;
        max-width: 420px;
        background: #ffffff;
        border-radius: 14px;
        padding: 12px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
        border: 1px solid rgba(0, 0, 0, 0.08);
    }

        .overlay-top {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 8px;
            font-size: 10px;
        }

        /* overlay back uses same visual: only the symbol */
        .overlay-back {
            color: #000;
            font-size: 22px;
            padding: 0 6px;
            background: transparent;
            border: none;
            box-shadow: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            line-height: 1;
        }

        .overlay-back:focus-visible { outline: 2px solid rgba(0,0,0,0.12); outline-offset: 2px; }

    .foods-list .food-item {
        padding: 12px;
        border-radius: 10px;
        background: transparent;
        margin-bottom: 8px;
    }

    .foods-list .value {
        color: #666;
        font-weight: 600;
    }

    .sub {
        font-size: 13px;
        color: #888;
        margin-top: 2px;
    }

    /* Variedad options */
    .variety-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 8px;
    }
    .option-card {
        all: unset;
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px;
        border-radius: 12px;
        background: rgba(0, 0, 0, 0.05);
        cursor: pointer;
    }
    .option-card.selected {
        border: 2px solid #0066cc;
        background: rgba(240, 180, 0, 0.06);
    }
    .option-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .option-card .small {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        background: linear-gradient(180deg, #0066cc, #2077cd);
        color: #fff;
    }
    .opt-title {
        font-weight: 700;
        margin-bottom: 4px;
    }
    .opt-desc {
        color: #666;
        font-size: 13px;
    }

    /* Número de comidas styles */
    .meals-list {
        list-style: none;
        padding: 0;
        margin: 8px 0 12px;
    }
    .meal-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 0;
        border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    }
    .meal-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .drag {
        color: #999;
        font-size: 18px;
    }
    .switch {
        width: 44px;
        height: 26px;
        border-radius: 20px;
        background: #ddd;
        position: relative;
        display: inline-flex;
        align-items: center;
        padding: 3px;
        cursor: pointer;
        border: none;
    }
    .switch.on {
        background: linear-gradient(90deg, #0066cc, #2077cd);
    }
    .switch .dot {
        width: 18px;
        height: 18px;
        background: #fff;
        border-radius: 50%;
        transition: transform 0.15s ease;
    }
    .switch.on .dot {
        transform: translateX(18px);
    }
    .switch.small {
        width: 38px;
        height: 22px;
    }
    .meal-info .label {
        font-weight: 600;
    }
    .meal-info .sub {
        margin-top: 2px;
    }

    .meals-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 14px;
    }
    

    /* Suggestions */
    .suggestion-section {
        padding: 12px 0;
        border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    }
    .suggestion-section h3 {
        margin: 0 0 6px 0;
    }
    .suggestion-section p {
        margin: 0 0 8px 0;
        color: #666;
    }
    .example {
        margin: 8px 0;
        color: #555;
    }

    /* Chips for food selection */
    .small-desc { color: #666; margin-bottom: 10px; }
    .foods-section { margin: 14px 0; }
    .section-head { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }
    .select-all { all: unset; color:#2077cd; cursor:pointer; font-size:14px; }
    .chips { display:flex; flex-wrap:wrap; gap:8px; }
    .chip { all: unset; padding:8px 12px; border-radius:10px; background:#efefef; color:#111; cursor:pointer; }
    .chip.selected { background: transparent; border: 2px solid #f0b400; color:#111; }

</style>
