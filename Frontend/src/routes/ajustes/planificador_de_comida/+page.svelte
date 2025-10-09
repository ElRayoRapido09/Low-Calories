<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  const weekdays = ['Lu','Ma','Mi','Ju','Vi','Sá','Do'];
  const monthNames = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];

  let today = new Date();
  let year = today.getFullYear();
  let month = today.getMonth(); // 0-11
  let months = []; // array de {year, month, grid}

  // selección de rango
  let rangeStart = null;
  let rangeEnd = null;

  function startOfDay(d){ return new Date(d.getFullYear(), d.getMonth(), d.getDate()); }
  function sameDay(a,b){ return a && b && startOfDay(a).getTime() === startOfDay(b).getTime(); }

  function generateMonth(y, m){
    // normaliza año/mes en caso de overflow (ej. month = 12 -> enero del año siguiente)
    const first = new Date(y, m, 1);
    const actualYear = first.getFullYear();
    const actualMonth = first.getMonth(); // 0-11 normalizado
    const daysInMonth = new Date(actualYear, actualMonth + 1, 0).getDate();
    // convertir a lunes=0
    const offset = (first.getDay() + 6) % 7;
    const totalCells = Math.ceil((offset + daysInMonth) / 7) * 7;
    const grid = new Array(totalCells).fill(null).map((_, i) => {
      const dayIndex = i - offset + 1;
      if (dayIndex < 1 || dayIndex > daysInMonth) return null;
      return new Date(actualYear, actualMonth, dayIndex);
    });
    return { year: actualYear, month: actualMonth, grid };
  }

  onMount(() => {
    months = [ generateMonth(year, month), generateMonth(year, month+1) ];
    console.log('months generated', months.map(m => `${m.month+1}/${m.year}`));
  });

  function selectDay(d){
    if(!d) return;
    console.log('selectDay click:', d);
    if(!rangeStart || (rangeStart && rangeEnd)){
      rangeStart = startOfDay(d);
      rangeEnd = null;
      console.log('rangeStart set:', rangeStart);
      return;
    }
    // si ya hay start pero no end -> definir end (ordenar)
    const t = startOfDay(d);
    if (t.getTime() === rangeStart.getTime()){
      // mismo día -> seleccionar como rango de un día
      rangeStart = t;
      rangeEnd = t;
      console.log('rangeStart=rangeEnd (mismo día):', rangeStart);
      return;
    }
    if (t.getTime() < rangeStart.getTime()){
      rangeEnd = rangeStart;
      rangeStart = t;
    } else {
      rangeEnd = t;
    }
    console.log('range selected:', rangeStart, rangeEnd);
  }

  function inRange(d){
    if(!d || !rangeStart) return false;
    const t = startOfDay(d).getTime();
    if(rangeEnd){
      return t >= rangeStart.getTime() && t <= rangeEnd.getTime();
    } else {
      return t === rangeStart.getTime();
    }
  }

  function clearSelection(){
    rangeStart = null;
    rangeEnd = null;
    console.log('selection cleared');
  }

  function confirmRange(){
    if(!(rangeStart && rangeEnd)){
      console.warn('confirmRange llamado sin rango completo');
      return;
    }
    const payload = { start: rangeStart.toISOString(), end: rangeEnd.toISOString() };
    console.log('Rango confirmado ->', payload);
    
    // Navegar a la página de planear con el rango en query params
    const searchParams = new URLSearchParams({
      start: rangeStart.toISOString(),
      end: rangeEnd.toISOString()
    });
    goto(`/ajustes/planificador_de_comida/planear?${searchParams.toString()}`);
  }
</script>

<div class="bg"></div>
<div class="bg bg2"></div>
<div class="bg bg3"></div>

<main class="app">
  <header class="top">
    <a href="/ajustes" class="back-btn" aria-label="Volver">‹</a>
    <div class="header-center">
      <div class="icon">📅</div>
      <h1>¿Qué días quieres planificar?</h1>
    </div>
  </header>

  <div class="tabs">
    {#each weekdays as w}<div class="tab">{w}</div>{/each}
  </div>

  <div class="months">
    {#each months as m}
      <div class="month">
        <div class="month-title">{monthNames[m.month]} {m.year}</div>
        <div class="grid">
          {#each m.grid as day}
            <button class="cell" on:click={() => selectDay(day)} disabled={!day} aria-pressed={inRange(day)}>
              <span class:today={day && sameDay(day, today)} class:inactive={!day}>{day ? day.getDate() : ''}</span>
              {#if inRange(day)}
                <span class="dot" />
              {/if}
            </button>
          {/each}
        </div>
      </div>
    {/each}
  </div>

  <div class="footer-gap"></div>

  <div class="bottom">
    <button class="btn secondary" on:click={clearSelection}>Limpiar</button>
    <button
      class="btn primary"
      on:click={confirmRange}
      disabled={!rangeStart || !rangeEnd}
      aria-disabled={!rangeStart || !rangeEnd}
    >
      <span class="item">
        {#if rangeStart && rangeEnd}
          Seleccionar {rangeStart.toLocaleDateString()} – {rangeEnd.toLocaleDateString()}
        {:else}
          Selecciona un rango
        {/if}
      </span>
    </button>
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
    background: linear-gradient(70deg, blue 0%, pink 100%);
    color: #f2f2f2;
    min-height: 100vh;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }

  .bg{
    position:fixed;
    background:linear-gradient(120deg, rgba(34, 34, 108, 0.6), rgba(19, 19, 58, 0.9));
    z-index:-1;
    animation:slide 3s ease-in-out infinite alternate;
    background-image: linear-gradient(-60deg, rgb(38, 40, 128) 50%, #09f 50%);
    bottom:0;
    left:-50%;
    opacity:.5;
    right:-50%;
    top:0;
  }

  .bg2{
    opacity:0.6;
    animation-direction: alternate-reverse;
    animation-duration: 4s;
  }

  .bg3{
    opacity:0.5;
    animation-duration: 5s;
  }

  .app{ max-width:420px; margin:0 auto; padding:20px; min-height:100vh; display:flex; flex-direction:column; }
  .top{ display:flex; align-items:center; gap:12px; margin-bottom:8px; }
  .back-btn{ color:#fff; font-size:28px; text-decoration:none; padding:6px; }
  .header-center{ flex:1; text-align:center; }
  .icon{ width:64px; height:64px; border-radius:999px; background:rgba(242,201,76,0.12); display:inline-flex; align-items:center; justify-content:center; font-size:26px; margin-bottom:8px; color:#f2c94c; }
  .top h1{ margin:0; font-size:20px; font-weight:800; }

  .tabs{ display:flex; gap:8px; justify-content:space-between; margin:12px 0; padding:10px; background:rgba(255,255,255,0.02); border-radius:10px; }
  .tab{ flex:1; text-align:center; color:rgba(255,255,255,0.75); font-size:13px; padding:6px 0; }

  .months{ margin-top:6px; display:flex; flex-direction:column; gap:18px; }

  .month-title{ font-weight:700; color:rgba(255,255,255,0.9); margin:6px 10px; }

  .grid{ display:grid; grid-template-columns: repeat(7, 1fr); gap:6px; padding:8px 10px; }
  .cell{ background:transparent; border:none; color:#fff; padding:12px 6px; border-radius:8px; display:flex; flex-direction:column; align-items:center; justify-content:flex-start; position:relative; min-height:54px; }
  .cell:disabled{ opacity:0.3; pointer-events:none; } /* deshabilitado no responde a eventos */

  .cell span{ display:block; font-weight:600; font-size:16px; }
  .cell span.inactive{ opacity:0; }
  .cell span.today{ color:#fff; }

  .cell[aria-pressed="true"]{ background: linear-gradient(180deg, rgba(242,201,76,0.12), rgba(242,201,76,0.06)); border-radius:8px; }

  .dot{ width:8px; height:8px; background:#f2c94c; border-radius:999px; position:absolute; bottom:10px; }

  .bottom{ position:sticky; bottom:12px; display:flex; gap:10px; padding:12px; background:transparent; margin-top:auto; justify-content:space-between; }
  .btn{ flex:1; padding:14px 12px; border-radius:12px; font-weight:700; border:none; cursor:pointer; }
  .btn.secondary{ background: rgba(255,255,255,0.03); color:rgba(255,255,255,0.9); }
  .btn.primary{ background:#111; color:#fff; box-shadow: 0 6px 18px rgba(0,0,0,0.6); border:1px solid rgba(242,201,76,0.18); }
  .btn.primary:disabled{ opacity:0.45; cursor:not-allowed; pointer-events:none; }

  @media (max-width:420px){
    .cell{ min-height:52px; padding:10px 4px; }
    .header-center .icon{ width:56px; height:56px; font-size:22px; }
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