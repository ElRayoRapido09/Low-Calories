<script>
  import { goto } from "$app/navigation";

  let videoStream;
  let stream = null;

  async function openCamera() {
    try {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert("Tu navegador no soporta la cámara.");
        return;
      }
      stream = await navigator.mediaDevices.getUserMedia({
        video: { 
          facingMode: "environment",
          width: { ideal: 1920 },
          height: { ideal: 1080 },
          aspectRatio: { ideal: 16 / 9 },
          frameRate: { ideal: 30 },
        },
        audio: false,
      });

      const video = document.getElementById("camera-video");
      const cameraContainer = document.getElementById("camera-container");

      video.srcObject = stream;
      cameraContainer.style.display = "flex";
      document.body.style.overflow = "hidden";
    } catch (error) {
      if (error.name === "NotAllowedError" || error.name === "PermissionDeniedError") {
        alert("Permiso denegado para acceder a la camara");
      } else if (error.name === "NotFoundError") {
        alert("No se encontro ninguna camara en el dispositivo.");
      } else {
        alert("Error al acceder a la camara: " + error.message);
      }
    }
  }

  function closeCamera() {
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
      stream = null;
    }
    document.getElementById("camera-container").style.display = "none";
    document.body.style.overflow = "auto";
  }

  function takePhoto() {
    const video = document.getElementById("camera-video");
    const canvas = document.getElementById("camera-canvas");
    const context = canvas.getContext("2d");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0);

    // Convierte la imagen a base64
    const imageData = canvas.toDataURL("image/jpeg");
    console.log("Foto capturada:", imageData);

    // Aquí puedes procesar la imagen o enviarla a tu backend
    closeCamera();
  }

  function goToObjetivos() {
    goto("/objetivos");
  }
  function goToComidas() {
    goto("/comidas");
  }

  console.log("hola layo");

  let isMenuOpen = $state(false);
  let scrollY = $state(0);
  let cardsContainer = $state(null);
  let startY = $state(0);
  let isDragging = $state(false);
  let cardsScrollY = $state(0);
  let maxScroll = $state(0);

  let bottomNavHeight = $derived(
    cardsScrollY <= 50
      ? Math.max(50 - cardsScrollY * 2, 0)
      : Math.min(50 + (cardsScrollY - 50) * 0.15, 100),
  );
  let cardsOpacity = $derived(
    cardsScrollY <= 50 ? Math.max(1 - cardsScrollY / 50, 0) : 1,
  );
  let cardsTransform = $derived(cardsScrollY <= 50 ? -(cardsScrollY * 2) : 0);

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }

  function closeMenu() {
    isMenuOpen = false;
  }

  function handleTouchStart(e) {
    if (!cardsContainer) return;
    startY = e.touches[0].clientY;
    isDragging = true;
  }

  function handleTouchMove(e) {
    if (!isDragging || !cardsContainer) return;

    const currentY = e.touches[0].clientY;
    const deltaY = currentY - startY;

    if (deltaY > 50 && cardsContainer.scrollTop === 0) {
      e.preventDefault();
      cardsContainer.style.transform = `translateY(${Math.min(deltaY - 50, 100)}px)`;
    }
  }

  function handleTouchEnd(e) {
    if (!isDragging || !cardsContainer) return;

    const currentY = e.changedTouches[0].clientY;
    const deltaY = currentY - startY;

    cardsContainer.style.transform = "translateY(0)";

    if (deltaY > 100 && cardsContainer.scrollTop === 0) {
      openCamera();
    }

    isDragging = false;
  }

  function handleScroll(e) {
    if (cardsContainer) {
      cardsScrollY = cardsContainer.scrollTop;
      maxScroll = cardsContainer.scrollHeight - cardsContainer.clientHeight;

      if (cardsScrollY <= 5) {
        openCamera();

        setTimeout(() => {
          if (cardsContainer) {
            cardsContainer.scrollTop = 10;
          }
        }, 100);
      }
    }
  }

  function goToBot() {
    goto("/Bot");
  }
  // son los datos estaticos de los objetivos
  let objetivos = $state([
    {
      id: 1,
      titulo: "Perder 5kg",
      progreso: 60,
      descripcion: "Objetivo de pérdida de peso saludable",
      icono: "⚖️",
    },
    {
      id: 2,
      titulo: "Ganar músculo",
      progreso: 30,
      descripcion: "Aumentar masa muscular con ejercicios",
      icono: "💪",
    },
    {
      id: 3,
      titulo: "Mantener peso",
      progreso: 80,
      descripcion: "Mantener el peso actual",
      icono: "🎯",
    },
  ]);

  // datos estaticos de la racha jejeje
  let diasRacha = $state([
    { dia: "L", enRacha: false },
    { dia: "M", enRacha: false },
    { dia: "M", enRacha: false },
    { dia: "J", enRacha: false },
    { dia: "V", enRacha: true },
    { dia: "S", enRacha: true },
    { dia: "D", enRacha: true },
  ]);
</script>

<svelte:head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
</svelte:head>

<main class="main">
  <header class="header">
    <h1>Low Calories</h1>
  </header>

  <section class="streak-section">
    <div class="section-header">
      <h2>Mi Racha</h2>
      <button class="edit-btn">Ver más</button>
    </div>
    <div class="streak-list">
      {#each diasRacha as dia}
        <div
          class="streak-icon {dia.enRacha
            ? 'streak-active'
            : 'streak-inactive'}"
        >
          {dia.enRacha ? "🔥" : "🗿"}
          <span class="streak-day">{dia.dia}</span>
        </div>
      {/each}
    </div>
  </section>

  <div class="content">
    <section class="ingredients-section">
      <div class="section-header">
        <h2>¿Qué tienes en tu cocina?</h2>
        <button class="edit-btn">Editar</button>
      </div>
      <div class="ingredients-list">
        <div class="ingredient-icon">🍗</div>
        <div class="ingredient-icon">🥩</div>
        <div class="ingredient-icon">🍞</div>
        <div class="ingredient-icon">🥚</div>
        <div class="ingredient-icon">🥚</div>
        <div class="ingredient-icon">🥓</div>
        <div class="ingredient-icon">🥓</div>
        <div class="ingredient-icon">🍖</div>
        <div class="ingredient-more">+99</div>
      </div>
    </section>

    <section class="recommendations-section">
      <h2>Recomendaciones del día</h2>
      <p class="subtitle">
        Estas recetas han sido elegidas exclusivamente para cumplir tu plan
      </p>

      <div class="recipe-card">
        <img
          src="https://images.unsplash.com/photo-1588137378633-dea1336ce1e2?w=500&h=400&fit=crop"
          alt="Comida"
        />
        <div class="recipe-info">
          <h3>Pollo con arroz y puré</h3>
          <p>450 kcal • 30 min</p>
        </div>
      </div>

      <section class="objetivos-section">
        <h2>Mis Objetivos</h2>
        <p class="subtitle">Sigue el progreso de tus metas nutricionales</p>

        {#each objetivos as objetivo}
          <div class="objetivo-card">
            <div class="objetivo-icon">{objetivo.icono}</div>
            <div class="objetivo-info">
              <h3>{objetivo.titulo}</h3>
              <p>{objetivo.descripcion}</p>
              <div class="progreso-bar">
                <div
                  class="progreso-fill"
                  style="width: {objetivo.progreso}%"
                ></div>
              </div>
              <span class="progreso-text">{objetivo.progreso}% completado</span>
            </div>
          </div>
        {/each}
      </section>

      <!-- aqui deben jalar el calendario de planificador_de_comida -->
      <h2>Calendario</h2>
      <div class="calendar-card">
        <div class="mini-calendar">
          <div class="calendar-header">
            <span class="calendar-month">Octubre 2025</span>
            <span class="calendar-arrows">‹ ›</span>
          </div>
          <div class="calendar-days">
            <span>L</span><span>M</span><span>M</span><span>J</span><span
              >V</span
            ><span>S</span><span>D</span>
          </div>
          <div class="calendar-dates">
            <span class="calendar-empty"></span>
            <span class="calendar-empty"></span>
            <span class="calendar-empty"></span>
            <span>1</span><span>2</span><span>3</span><span>4</span>
            <span>5</span><span>6</span><span>7</span><span>8</span><span
              >9</span
            ><span>10</span><span>11</span>
            <span>12</span><span>13</span><span>14</span><span>15</span><span
              >16</span
            ><span>17</span><span>18</span>
            <span>19</span><span>20</span><span>21</span><span>22</span><span
              >23</span
            ><span>24</span><span>25</span>
            <span>26</span><span>27</span><span>28</span><span>29</span><span
              >30</span
            ><span>31</span>
          </div>
        </div>
      </div>
    </section>
  </div>

  <nav class="bottom-nav">
    <a href="/ajustes" class="nav-item">
      <span class="nav-icon">⚙️</span>
      <span class="nav-label">Ajustes</span>
    </a>

    <a href="/estadisticas" class="nav-item">
      <span class="nav-icon">📊</span>
      <span class="nav-label">Metricas</span>
    </a>

    <a href="/estadisticas" class="nav-item">
    </a>

    <button class="nav-item camera-btn" on:click={openCamera}>
      <span class="camera-icon">📷</span>
    </button>

    <a href="/perfil" class="nav-item">
      <span class="nav-icon">👤</span>
      <span class="nav-label">Perfil</span>
    </a>

    <a href="/objetivos" class="nav-item">
      <span class="nav-icon">🎯</span>
      <span class="nav-label">Objetivo</span>
    </a>
  </nav>

  <button class="floating-btn" on:click={goToBot}> 🤖 </button>

  <div id="camera-container" class="camera-container" style="display: none;">
    <video id="camera-video" autoplay playsinline></video>
    <canvas id="camera-canvas" style="display: none;"></canvas>

    <div class="camera-controls">
      <header class="header-back">
        <button id="close-camera-btn" class="back-btn" on:click={closeCamera}>‹</button>
      </header>
      <button id="take-photo-btn" class="camera-btn" on:click={takePhoto}> 📷 </button>
    </div>
  </div>
</main>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap");

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial,
      sans-serif;
    background: #ffffff;
    color: #333;
  }

  .main {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background: #ffffff;
    padding-bottom: 70px;
  }

  .header {
    padding: 1rem;
    text-align: center;
    background: #ffffff;
  }

  .header h1 {
    font-family: "Dancing Script", cursive;
    font-size: 2rem;
    font-weight: 700;
    margin: 0;
    color: #000;
  }

  .content {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
  }

  .section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  .section-header h2 {
    font-size: 1.1rem;
    font-weight: 600;
    margin: 0;
    color: #000;
  }

  .edit-btn {
    background: none;
    border: none;
    color: #666;
    font-size: 0.9rem;
    cursor: pointer;
  }

  .ingredients-section {
    margin-bottom: 2rem;
  }

  .ingredients-list {
    display: flex;
    gap: 0.5rem;
    overflow-x: auto;
    padding-bottom: 0.5rem;
  }

  .ingredient-icon,
  .ingredient-more {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: #005bb5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    flex-shrink: 0;
  }

  .ingredient-more {
    background: #005bb5;
    color: #fff;
    font-size: 0.9rem;
    font-weight: 600;
  }

  .recommendations-section h2 {
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: #000;
  }

  .subtitle {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 1.5rem;
  }

  .recipe-card {
    margin-bottom: 1.5rem;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .recipe-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  .recipe-info {
    padding: 1rem;
    background: #fff;
  }

  .recipe-info h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #000;
  }

  .recipe-info p {
    margin: 0;
    font-size: 0.9rem;
    color: #666;
  }

  .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 70px;
    background: #fff;
    border-top: 1px solid #e0e0e0;
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 0 1rem;
    z-index: 100;
  }
  
  .nav-item.camera-btn {
    position: absolute;
    left: 50%;
    top: 10px; /* distancia sobre la barra: ajustar según se requiera */
    transform: translateX(-50%);
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: #fff; /* círculo blanco */
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.18);
    z-index: 200;
    border: none;
    padding: 0;
  }

  .nav-item.camera-btn .camera-icon {
    font-size: 1.6rem;
    margin: 0;
  }

  .nav-item {
    text-align: center;
    align-items: center; 
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
    color: #666;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.4rem 0.6rem;
    transition: color 0.2s;
  }

  .nav-item:hover {
    color: #000;
  }

  .nav-icon {
    font-size: 1.5rem;
    margin-bottom: 0.25rem;
  }

  .nav-label {
    font-size: 0.8rem;
    font-weight: 500;
    margin-top: 2px;
    text-align: left;
    line-height: 1;
    display: block;
    margin-left: -3px;
  }

  .camera-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    height: 100dvh; /* Usa viewport dinámico en móviles */
    background-color: #000;
    z-index: 9999;
    display: none;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }

  #camera-video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
  }

  .camera-controls {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: env(safe-area-inset-bottom, 20px) 20px 20px;
    z-index: 10000;
    background: linear-gradient(to top, rgba(0,0,0,0.5), transparent);
  }

  .camera-btn {
    padding: 15px 30px;
    font-size: 13px;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    background-color: #4caf50;
    color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
  }

  .camera-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
  }

  .header-back {
    position: fixed;
    left: 20px;
    top: 20px;
    top: max(20px, env(safe-area-inset-top));
    display: flex;
    align-items: center;
    gap: 0.5rem;
    z-index: 10001;
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .back-btn {
    font-size: 1.5rem;
    color: #000000;
    text-decoration: none;
    border: none;
    cursor: pointer;
    padding: 0;
    line-height: 1;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  }

  .back-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.5);
  }

  .back-btn:active {
    transform: scale(0.95);
  }

  .camera-btn {
    font-size: 1.8rem;
    color: #000;
    text-decoration: none;
    cursor: pointer;
    padding: 0;
    line-height: 1;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    border: 4px solid rgba(255, 255, 255, 0.3);
  }

  .camera-icon {
    font-size: 2rem;
  }

  .camera-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.5);
  }

  .camera-btn:active {
    transform: scale(0.95);
  }

  /* Ajustes para dispositivos móviles pequeños */
  @media screen and (max-width: 375px) {
    .header-back {
      left: 15px;
      top: max(15px, env(safe-area-inset-top));
    }

    .back-btn {
      width: 48px;
      height: 48px;
      font-size: 1.3rem;
    }

    .camera-btn {
      width: 60px;
      height: 60px;
      font-size: 1.6rem;
    }
  }

  /* Ajustes para orientación landscape */
  @media screen and (orientation: landscape) {
    .camera-controls {
      padding: 15px 20px;
    }

    .header-back {
      top: 15px;
    }

    .camera-btn {
      width: 60px;
      height: 60px;
    }
  }

  /* Soporte para notch y safe areas */
  @supports (padding: max(0px)) {
    .camera-container {
      padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);
    }
  }

  .calendar-card {
    margin-bottom: 1.5rem;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    background: #fff;
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .mini-calendar {
    width: 100%;
    max-width: 320px;
    margin: 0 auto;
    font-family: inherit;
  }
  .calendar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #005bb5;
    font-size: 1rem;
  }
  .calendar-month {
    font-size: 1rem;
    font-weight: 700;
  }
  .calendar-arrows {
    font-size: 1.2rem;
    color: #666;
    cursor: pointer;
  }
  .calendar-days {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    text-align: center;
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 0.3rem;
    font-weight: 500;
  }
  .calendar-dates {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    text-align: center;
    gap: 0.2rem;
  }
  .calendar-dates span {
    padding: 0.4rem 0;
    border-radius: 6px;
    font-size: 0.95rem;
    color: #333;
    background: #f5f5f5;
    transition: background 0.2s;
  }
  .calendar-dates span:hover {
    background: #005bb5;
    color: #fff;
    cursor: pointer;
  }
  .calendar-empty {
    background: transparent !important;
    cursor: default !important;
  }

  .floating-btn {
    position: fixed;
    bottom: 90px; /* Arriba del bottom-nav */
    right: 10px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #005bb5;
    border: none;
    color: #fff;
    font-size: 1.5rem;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    z-index: 200;
    display: flex;
    align-items: center;
    justify-content: center;
    transition:
      transform 0.2s,
      box-shadow 0.2s;
  }

  .floating-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
  }

  .floating-btn:active {
    transform: scale(0.95);
  }

  .objetivos-section {
    margin-bottom: 2rem;
  }

  .objetivos-section h2 {
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: #000;
  }

  .objetivo-card {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    padding: 1rem;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #e0e0e0;
  }

  .objetivo-icon {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #005bb5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    margin-right: 1rem;
    flex-shrink: 0;
  }

  .objetivo-info {
    flex: 1;
  }

  .objetivo-info h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #000;
  }

  .objetivo-info p {
    margin: 0 0 1rem 0;
    font-size: 0.9rem;
    color: #666;
  }

  .progreso-bar {
    width: 100%;
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 0.5rem;
  }

  .progreso-fill {
    height: 100%;
    background: #005bb5;
    transition: width 0.3s;
  }

  .progreso-text {
    font-size: 0.8rem;
    color: #666;
  }

  .streak-section {
    margin-bottom: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .streak-list {
    display: flex;
    justify-content: space-between;
    padding-bottom: 0.5rem;
  }

  .streak-icon {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    flex-shrink: 0;
    position: relative;
  }

  .streak-active {
    background: #ff6b35; /* Naranja rojizo para fuego */
    color: #fff;
  }

  .streak-inactive {
    background: #f5f5f5;
    color: #666;
  }

  .streak-day {
    font-size: 0.7rem;
    font-weight: 600;
    margin-top: 2px;
  }
</style>
