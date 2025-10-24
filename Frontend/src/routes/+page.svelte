<script>
  import { goto } from '$app/navigation';
  function openCamera() {
    alert('aqui se abre la camara');
  }

  function goToObjetivos() {
    goto('/objetivos');
  }
  function goToComidas() {
    goto('/comidas');
  }

  console.log("hola layo");

  let isMenuOpen = $state(false);
  let scrollY = $state(0);
  let cardsContainer = $state(null);
  let startY = $state(0);
  let isDragging = $state(false);
  let cardsScrollY = $state(0);
  let maxScroll = $state(0);

  let bottomNavHeight = $derived(cardsScrollY <= 50 ? Math.max(50 - (cardsScrollY * 2), 0) : Math.min(50 + ((cardsScrollY - 50) * 0.15), 100));
  let cardsOpacity = $derived(cardsScrollY <= 50 ? Math.max(1 - (cardsScrollY / 50), 0) : 1);
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

    cardsContainer.style.transform = 'translateY(0)';
    
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
</script>

<main class="main">
  <header class="header">
    <h1>Low Calories</h1>
  </header>

 
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
      <p class="subtitle">Estas recetas han sido elegidas exclusivamente para cumplir tu plan</p>
      
      <div class="recipe-card">
        <img src="https://images.unsplash.com/photo-1588137378633-dea1336ce1e2?w=500&h=400&fit=crop" alt="Comida" />
        <div class="recipe-info">
          <h3>Pollo con arroz y puré</h3>
          <p>450 kcal • 30 min</p>
        </div>
      </div>

      <!-- aqui deben jalar el calendario de planificador_de_comida -->
      <h2>Calendario</h2>
      <div class="calendar-card">
  <div class="mini-calendar">
    <div class="calendar-header">
      <span class="calendar-month">Octubre 2025</span>
      <span class="calendar-arrows">‹ ›</span>
    </div>
    <div class="calendar-days">
      <span>L</span><span>M</span><span>M</span><span>J</span><span>V</span><span>S</span><span>D</span>
    </div>
    <div class="calendar-dates">
      <span class="calendar-empty"></span>
      <span class="calendar-empty"></span>
      <span class="calendar-empty"></span>
      <span>1</span><span>2</span><span>3</span><span>4</span>
      <span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span>
      <span>12</span><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span>
      <span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span>
      <span>26</span><span>27</span><span>28</span><span>29</span><span>30</span><span>31</span>
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
      <span class="nav-label">Estadísticas</span>
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
</main>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
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
    font-family: 'Dancing Script', cursive;
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

  .ingredient-icon, .ingredient-more {
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

  .nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    color: #666;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
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
    font-size: 0.7rem;
    font-weight: 500;
  }


  .camera-btn {
    position: relative;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #005bb5;
    box-shadow: 0 4px 12px rgba(255, 215, 0, 0.4);
    margin: 0 0.5rem;
  }

  .camera-icon {
    font-size: 2rem;
  }

  .camera-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 16px rgba(255, 215, 0, 0.5);
  }

  .camera-btn:active {
    transform: scale(0.95);
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
</style>
