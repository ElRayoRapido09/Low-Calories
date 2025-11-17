<script>
  import { goto } from "$app/navigation";
  import { _ } from 'svelte-i18n';
  import { energyUnit, convertValue, formatWithUnit } from '$lib/stores/units.js';

  let stream = null;
  let isDetecting = false;
  let showCaptureButton = true; // Cambiado a true para mostrar el botón inmediatamente
  let isProcessing = false;
  let alertMessage = '';
  let motionDetected = false;
  let stabilityTimer = null;
  let detectionAttempts = 0;
  const MAX_DETECTION_ATTEMPTS = 3;
  
  // Variables para detección de movimiento
  let lastAcceleration = { x: 0, y: 0, z: 0 };
  let movementThreshold = 1.5;
  let hasMotionSensor = false;
  let lastFrameData = null;
  let pixelChangeThreshold = 30;
  let motionDetectionInterval = null;

  // Variables para el calendario
  let currentDate = $state(new Date());
  let currentMonth = $derived(currentDate.getMonth());
  let currentYear = $derived(currentDate.getFullYear());
  
  // Función para obtener días del mes
  function getDaysInMonth(year, month) {
    return new Date(year, month + 1, 0).getDate();
  }
  
  // Función para obtener el primer día de la semana del mes (0 = domingo, 1 = lunes, etc.)
  function getFirstDayOfMonth(year, month) {
    const firstDay = new Date(year, month, 1).getDay();
    // Convertir domingo (0) a 7 para que lunes sea 1
    return firstDay === 0 ? 6 : firstDay - 1;
  }
  
  // Calcular días del calendario
  let calendarDays = $derived.by(() => {
    const daysInMonth = getDaysInMonth(currentYear, currentMonth);
    const firstDay = getFirstDayOfMonth(currentYear, currentMonth);
    const days = [];
    
    // Agregar espacios vacíos para los días antes del inicio del mes
    for (let i = 0; i < firstDay; i++) {
      days.push({ type: 'empty', value: '' });
    }
    
    // Agregar los días del mes
    for (let i = 1; i <= daysInMonth; i++) {
      const isToday = i === new Date().getDate() && 
                      currentMonth === new Date().getMonth() && 
                      currentYear === new Date().getFullYear();
      days.push({ type: 'day', value: i, isToday });
    }
    
    return days;
  });
  
  function previousMonth() {
    if (currentMonth === 0) {
      currentDate = new Date(currentYear - 1, 11, 1);
    } else {
      currentDate = new Date(currentYear, currentMonth - 1, 1);
    }
  }
  
  function nextMonth() {
    if (currentMonth === 11) {
      currentDate = new Date(currentYear + 1, 0, 1);
    } else {
      currentDate = new Date(currentYear, currentMonth + 1, 1);
    }
  }

  // Valor de calorías almacenado (siempre en kcal)
  let recipeCalories = $state(450);
  
  // Convertir calorías a la unidad seleccionada
  let displayCalories = $derived(
    convertValue(recipeCalories, 'energy', 'kcal', $energyUnit)
  );
  
  let formattedCalories = $derived(
    formatWithUnit(displayCalories, $energyUnit, 0)
  );

  async function openCamera() {
    try {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert($_('home.camera.notSupported'));
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
      
      // Mostrar el botón de captura inmediatamente
      showCaptureButton = true;
      
      // Iniciar detección de movimiento (opcional ahora)
      // initMotionDetection();
      
    } catch (error) {
      if (error.name === "NotAllowedError" || error.name === "PermissionDeniedError") {
        alert($_('home.camera.permissionDenied'));
      } else if (error.name === "NotFoundError") {
        alert($_('home.camera.notFound'));
      } else {
        alert($_('home.camera.error') + ': ' + error.message);
      }
    }
  }

  function initMotionDetection() {
    // Resetear variables
    isDetecting = false;
    detectionAttempts = 0;
    motionDetected = false;
    
    // Intentar usar sensores de movimiento (DeviceMotion)
    if (window.DeviceMotionEvent && typeof DeviceMotionEvent.requestPermission === 'function') {
      // iOS 13+ requiere permiso explícito
      DeviceMotionEvent.requestPermission()
        .then(response => {
          if (response === 'granted') {
            window.addEventListener('devicemotion', handleDeviceMotion);
            hasMotionSensor = true;
            console.log('Sensor de movimiento disponible');
          } else {
            startPixelBasedMotionDetection();
          }
        })
        .catch(() => {
          startPixelBasedMotionDetection();
        });
    } else if (window.DeviceMotionEvent) {
      window.addEventListener('devicemotion', handleDeviceMotion);
      hasMotionSensor = true;
      console.log('Sensor de movimiento disponible');
    } else {
      // Fallback: usar análisis de píxeles
      console.log('Sensor de movimiento no disponible, usando análisis de píxeles');
      startPixelBasedMotionDetection();
    }
  }

  function handleDeviceMotion(event) {
    if (isProcessing) return;
    
    const acceleration = event.accelerationIncludingGravity;
    
    if (!acceleration) return;
    
    // Calcular la diferencia de aceleración
    const deltaX = Math.abs(acceleration.x - lastAcceleration.x);
    const deltaY = Math.abs(acceleration.y - lastAcceleration.y);
    const deltaZ = Math.abs(acceleration.z - lastAcceleration.z);
    
    const totalMovement = deltaX + deltaY + deltaZ;
    
    // Actualizar última aceleración
    lastAcceleration = {
      x: acceleration.x,
      y: acceleration.y,
      z: acceleration.z
    };
    
    // Detectar si hay movimiento
    if (totalMovement > movementThreshold) {
      motionDetected = true;
      // Cancelar el temporizador de estabilidad si existe
      if (stabilityTimer) {
        clearTimeout(stabilityTimer);
        stabilityTimer = null;
      }
    } else {
      // Si no hay movimiento, iniciar temporizador de estabilidad
      if (!stabilityTimer && !isDetecting) {
        startStabilityTimer();
      }
    }
  }

  function startPixelBasedMotionDetection() {
    motionDetectionInterval = setInterval(() => {
      if (isProcessing) return;
      
      const video = document.getElementById("camera-video");
      if (!video || video.readyState !== 4) return;
      
      const tempCanvas = document.createElement('canvas');
      tempCanvas.width = 320;
      tempCanvas.height = 240;
      const ctx = tempCanvas.getContext('2d');
      ctx.drawImage(video, 0, 0, tempCanvas.width, tempCanvas.height);
      
      const currentFrameData = ctx.getImageData(0, 0, tempCanvas.width, tempCanvas.height);
      
      if (lastFrameData) {
        const movement = calculatePixelDifference(lastFrameData, currentFrameData);
        
        if (movement > pixelChangeThreshold) {
          motionDetected = true;
          if (stabilityTimer) {
            clearTimeout(stabilityTimer);
            stabilityTimer = null;
          }
        } else {
          if (!stabilityTimer && !isDetecting) {
            startStabilityTimer();
          }
        }
      }
      
      lastFrameData = currentFrameData;
    }, 200);
  }

  function calculatePixelDifference(frame1, frame2) {
    let totalDiff = 0;
    const pixelCount = frame1.data.length / 4;
    
    for (let i = 0; i < frame1.data.length; i += 4) {
      const r1 = frame1.data[i];
      const g1 = frame1.data[i + 1];
      const b1 = frame1.data[i + 2];
      
      const r2 = frame2.data[i];
      const g2 = frame2.data[i + 1];
      const b2 = frame2.data[i + 2];
      
      const diff = Math.abs(r1 - r2) + Math.abs(g1 - g2) + Math.abs(b1 - b2);
      totalDiff += diff;
    }
    
    return (totalDiff / (pixelCount * 255 * 3)) * 100;
  }

  function startStabilityTimer() {
    motionDetected = false;
    stabilityTimer = setTimeout(() => {
      if (!motionDetected && !isProcessing) {
        attemptAutomaticCapture();
      }
      stabilityTimer = null;
    }, 2000);
  }

  async function attemptAutomaticCapture() {
    if (isDetecting || isProcessing) return;
    
    isDetecting = true;
    detectionAttempts++;
    console.log(`Intento de detección automática #${detectionAttempts}`);
    
    showAlert($_('home.camera.detecting'));
    
    // Capturar frame actual
    const imageBlob = await captureFrame();
    
    // Procesar automáticamente
    await processImage(imageBlob, true);
  }

  async function captureFrame() {
    const video = document.getElementById("camera-video");
    const canvas = document.getElementById("camera-canvas");
    const context = canvas.getContext("2d");

    // Establecer tamaño óptimo para mejor calidad
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    context.drawImage(video, 0, 0);

    return new Promise((resolve) => {
      // Aumentar calidad JPEG a 0.95
      canvas.toBlob((blob) => {
        resolve(blob);
      }, 'image/jpeg', 0.95);  // Calidad 95%
    });
}

  async function processImage(imageBlob, isAutomatic = false) {
    isProcessing = true;
    showAlert($_('home.camera.processing'));
    
    try {
      const formData = new FormData();
      formData.append('image', imageBlob, 'food-scan.jpg');
      
      // Obtener el token de autenticación
      const token = localStorage.getItem('authToken') || sessionStorage.getItem('authToken');
      
      const headers = {};
      if (token) {
        headers['Authorization'] = `Bearer ${token}`;
      }
      
      console.log('Enviando imagen a:', 'http://localhost:8000/api/scan-food/');
      
      const response = await fetch('http://localhost:8000/api/scan-food/', {
        method: 'POST',
        headers: headers,
        body: formData
      });
      
      console.log('Respuesta del servidor:', response.status);
      
      const data = await response.json();
      console.log('Datos recibidos:', data);
      
      if (response.ok && data.success) {
        // Éxito: redirigir a página de resultados
        showAlert($_('home.camera.success'));
        setTimeout(() => {
          closeCamera();
          goto(`/food-details?id=${data.historial_id}`);
        }, 1000);
      } else {
        // Error en el procesamiento
        console.error('Error en procesamiento:', data);
        showAlert(data.error || $_('home.camera.noRecognition'));
        isProcessing = false;
        isDetecting = false;
      }
    } catch (error) {
      console.error('Error procesando imagen:', error);
      showAlert($_('home.camera.connectionError'));
      isProcessing = false;
      isDetecting = false;
    }
  }

  function showAlert(message) {
    alertMessage = message;
    setTimeout(() => {
      if (!isProcessing) { // Solo limpiar si no está procesando
        alertMessage = '';
      }
    }, 5000);
  }

  function closeCamera() {
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
      stream = null;
    }
    
    // Limpiar detección de movimiento
    if (hasMotionSensor) {
      window.removeEventListener('devicemotion', handleDeviceMotion);
    }
    if (motionDetectionInterval) {
      clearInterval(motionDetectionInterval);
      motionDetectionInterval = null;
    }
    if (stabilityTimer) {
      clearTimeout(stabilityTimer);
      stabilityTimer = null;
    }
    
    // Resetear variables
    isDetecting = false;
    showCaptureButton = true; // Mantener en true para la próxima vez
    isProcessing = false;
    alertMessage = '';
    detectionAttempts = 0;
    lastFrameData = null;
    
    document.getElementById("camera-container").style.display = "none";
    document.body.style.overflow = "auto";
  }

  async function takePhoto() {
    if (isProcessing) return; // Evitar múltiples clics
    
    console.log('Tomando foto manualmente...');
    const imageBlob = await captureFrame();
    await processImage(imageBlob, false);
  }

  function goToObjetivos() {
    goto("/objetivos");
  }
  function goToComidas() {
    goto("/comidas");
  }

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
  
  let objetivos = $state([
    {
      id: 1,
      titulo: $_('home.loseWeight'),
      progreso: 60,
      descripcion: $_('home.loseWeightDesc'),
      icono: "⚖️",
    },
    {
      id: 2,
      titulo: $_('home.gainMuscle'),
      progreso: 30,
      descripcion: $_('home.gainMuscleDesc'),
      icono: "💪",
    },
    {
      id: 3,
      titulo: $_('home.maintainWeight'),
      progreso: 80,
      descripcion: $_('home.maintainWeightDesc'),
      icono: "🎯",
    },
  ]);

  let diasRacha = $state([
    { dia: $_('home.dayAbbr.mon'), enRacha: false },
    { dia: $_('home.dayAbbr.tue'), enRacha: false },
    { dia: $_('home.dayAbbr.wed'), enRacha: false },
    { dia: $_('home.dayAbbr.thu'), enRacha: false },
    { dia: $_('home.dayAbbr.fri'), enRacha: true },
    { dia: $_('home.dayAbbr.sat'), enRacha: true },
    { dia: $_('home.dayAbbr.sun'), enRacha: true },
  ]);

   
</script>

<svelte:head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
</svelte:head>

<main class="main">
  <header class="header">
    <h1>{$_('home.title')}</h1>
  </header>

  <section class="streak-section">
    <div class="section-header">
      <h2>{$_('home.myStreak')}</h2>
      <button class="edit-btn">{$_('home.viewMore')}</button>
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
        <h2>{$_('home.kitchen')}</h2>
        <button class="edit-btn">{$_('common.edit')}</button>
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
      <h2>{$_('home.recommendations')}</h2>
      <p class="subtitle">
        {$_('home.recommendationsSubtitle')}
      </p>

      <div class="recipe-card">
        <img
          src="https://images.unsplash.com/photo-1588137378633-dea1336ce1e2?w=500&h=400&fit=crop"
          alt="Arroz con pollo"
        />
        <div class="recipe-info">
          <h3>{$_('home.recommendations')}</h3>
          <p>{formattedCalories} • 30 min</p>
        </div>
      </div>

      <section class="objetivos-section">
        <h2>{$_('home.myGoals')}</h2>
        <p class="subtitle">{$_('home.goalsSubtitle')}</p>

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
              <span class="progreso-text">{objetivo.progreso}% {$_('home.completed')}</span>
            </div>
          </div>
        {/each}
      </section>

      <h2>{$_('home.calendar.title')}</h2>
      <div class="calendar-card">
        <div class="mini-calendar">
          <div class="calendar-header">
            <button class="calendar-arrow-btn" onclick={previousMonth} aria-label="Mes anterior">‹</button>
            <span class="calendar-month">{$_(`home.months.${currentMonth}`)} {currentYear}</span>
            <button class="calendar-arrow-btn" onclick={nextMonth} aria-label="Mes siguiente">›</button>
          </div>
          <div class="calendar-days">
            <span>{$_('home.dayAbbr.mon')}</span>
            <span>{$_('home.dayAbbr.tue')}</span>
            <span>{$_('home.dayAbbr.wed')}</span>
            <span>{$_('home.dayAbbr.thu')}</span>
            <span>{$_('home.dayAbbr.fri')}</span>
            <span>{$_('home.dayAbbr.sat')}</span>
            <span>{$_('home.dayAbbr.sun')}</span>
          </div>
          <div class="calendar-dates">
            {#each calendarDays as day}
              {#if day.type === 'empty'}
                <span class="calendar-empty"></span>
              {:else}
                <span class:calendar-today={day.isToday}>{day.value}</span>
              {/if}
            {/each}
          </div>
        </div>
      </div>
    </section>
  </div>

  <nav class="bottom-nav">
    <a href="/ajustes" class="nav-item">
      <span class="nav-icon">⚙️</span>
      <span class="nav-label">{$_('navigation.settings')}</span>
    </a>

    <a href="/estadisticas" class="nav-item">
      <span class="nav-icon">📊</span>
      <span class="nav-label">{$_('navigation.metrics')}</span>
    </a>

    <a href="/estadisticas" class="nav-item">
    </a>

    <button class="nav-item camera-btn" onclick={openCamera}>
      <span class="camera-icon">📷</span>
    </button>

    <a href="/perfil" class="nav-item">
      <span class="nav-icon">👤</span>
      <span class="nav-label">{$_('navigation.profile')}</span>
    </a>

    <a href="/objetivos" class="nav-item">
      <span class="nav-icon">🎯</span>
      <span class="nav-label">{$_('navigation.goals')}</span>
    </a>
  </nav>

  <button class="floating-btn" onclick={goToBot}> 🤖 </button>

  <div id="camera-container" class="camera-container" style="display: none;">
    <video id="camera-video" autoplay playsinline></video>
    <canvas id="camera-canvas" style="display: none;"></canvas>

    <!-- Overlay con información de detección -->
    {#if alertMessage}
      <div class="alert-overlay">
        {alertMessage}
      </div>
    {/if}

    <div class="camera-controls">
      <header class="header-back">
        <button id="close-camera-btn" class="back-btn" onclick={closeCamera}>‹</button>
      </header>
      
      {#if showCaptureButton && !isProcessing}
        <button id="take-photo-btn" class="camera-btn-capture" onclick={takePhoto}>
          {$_('home.camera.takePhoto')}
        </button>
      {/if}
      
      {#if isProcessing}
        <div class="processing-overlay">
          <div class="spinner"></div>
          <p>{$_('home.camera.processingImage')}</p>
        </div>
      {/if}
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
    top: 10px;
    transform: translateX(-50%);
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: #fff;
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
    height: 100dvh;
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

  .alert-overlay {
    position: absolute;
    top: 80px;
    left: 1rem;
    right: 1rem;
    background: rgba(255, 152, 0, 0.95);
    color: white;
    padding: 1rem;
    border-radius: 12px;
    text-align: center;
    z-index: 10001;
    font-weight: 600;
    animation: slideDown 0.3s ease-out;
    backdrop-filter: blur(10px);
  }

  @keyframes slideDown {
    from {
      transform: translateY(-100%);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }

  .spinner {
    width: 50px;
    height: 50px;
    border: 4px solid rgba(255, 255, 255, 0.3);
    border-top-color: white;
    border-radius: 50%;
    margin: 0 auto 1rem;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
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

  .camera-btn-capture {
    padding: 18px 40px;
    font-size: 1.2rem;
    font-weight: bold;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    background-color: #4caf50;
    color: white;
    box-shadow: 0 6px 20px rgba(76, 175, 80, 0.6);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    z-index: 10001;
  }

  .camera-btn-capture:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 25px rgba(76, 175, 80, 0.8);
  }

  .camera-btn-capture:active {
    transform: scale(0.95);
  }

  .processing-overlay {
    position: absolute;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0, 0, 0, 0.85);
    padding: 1.5rem 2rem;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    text-align: center;
    color: white;
  }

  .processing-overlay p {
    margin: 0;
    font-weight: 600;
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

    .camera-btn-capture {
      padding: 15px 32px;
      font-size: 1.05rem;
    }
  }

  @media screen and (orientation: landscape) {
    .camera-controls {
      padding: 15px 20px;
    }

    .header-back {
      top: 15px;
    }
  }

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
  
  .calendar-arrow-btn {
    background: transparent;
    border: none;
    font-size: 1.5rem;
    color: #005bb5;
    cursor: pointer;
    padding: 0.2rem 0.5rem;
    transition: transform 0.2s;
  }
  
  .calendar-arrow-btn:hover {
    transform: scale(1.2);
  }
  
  .calendar-arrow-btn:active {
    transform: scale(0.95);
  }
  
  .calendar-today {
    background: #005bb5 !important;
    color: #fff !important;
    font-weight: 700;
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
    bottom: 90px;
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
    background: #ff6b35;
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