<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    import { goto } from '$app/navigation';
    import { _ } from 'svelte-i18n';
    
    let foodData = null;
    let loading = true;
    let error = null;
    let historialId = null;
    
    onMount(async () => {
        historialId = $page.url.searchParams.get('id');
        
        console.log('🔍 ID del historial:', historialId);
        
        if (!historialId) {
            error = $_('foodDetails.noIdProvided');
            loading = false;
            return;
        }
        
        await loadFoodDetails(historialId);
    });
    
    async function loadFoodDetails(id) {
        try {
            const token = localStorage.getItem('authToken') || sessionStorage.getItem('authToken');
            
            const headers = {};
            if (token) {
                headers['Authorization'] = `Bearer ${token}`;
            }
            
            console.log('📡 Cargando datos del historial...');
            
            const response = await fetch(`http://localhost:8000/api/food-history/`, {
                headers: headers
            });
            
            if (!response.ok) {
                throw new Error($_('foodDetails.loadError'));
            }
            
            const historyData = await response.json();
            console.log('📊 Datos del historial recibidos:', historyData);
            
            foodData = historyData.find(item => item.id === parseInt(id));
            
            console.log('🍽️ Datos de la comida encontrada:', foodData);
            
            if (!foodData) {
                error = $_('foodDetails.notFound');
            }
            
        } catch (err) {
            console.error('❌ Error cargando detalles:', err);
            error = err.message;
        } finally {
            loading = false;
        }
    }
    
    function goBack() {
        goto('/');
    }
    
    function scanAgain() {
        goto('/');
        setTimeout(() => {
            const cameraButton = document.querySelector('.camera-btn');
            if (cameraButton) {
                cameraButton.click();
            }
        }, 100);
    }
    
    function formatDate(dateString) {
        const date = new Date(dateString);
        const options = { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        return date.toLocaleDateString('es-ES', options);
    }
    
    // Función para formatear números con decimales
    function formatNumber(value) {
        if (value === null || value === undefined) {
            return 'N/A';
        }
        return typeof value === 'number' ? value.toFixed(1) : value;
    }
</script>

<svelte:head>
    <title>{$_('foodDetails.title')} - Low Calories</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
</svelte:head>

<div class="food-details-container">
    {#if loading}
        <div class="loading">
            <div class="spinner"></div>
            <p>{$_('foodDetails.loading')}</p>
        </div>
    {:else if error}
        <div class="error-container">
            <div class="error-icon">⚠️</div>
            <h2>{$_('foodDetails.error')}</h2>
            <p>{error}</p>
            <button class="btn-primary" on:click={goBack}>{$_('foodDetails.backToHome')}</button>
        </div>
    {:else if foodData}
        <div class="header">
            <button class="back-btn" on:click={goBack}>
                <span class="back-icon">←</span>
                <span>{$_('foodDetails.backButton')}</span>
            </button>
            <h1>{$_('foodDetails.nutritionalDetails')}</h1>
        </div>
        
        <div class="content">
            {#if foodData.image_url}
                <div class="image-container">
                    <img src={foodData.image_url} alt={foodData.nombre_alimento || $_('foodDetails.unknownFood')} />
                    <div class="image-overlay">
                        <span class="scan-badge">✓ {$_('foodDetails.scanned')}</span>
                    </div>
                </div>
            {/if}
            
            <div class="food-info">
                <h2>{foodData.nombre_alimento || $_('foodDetails.unknownFood')}</h2>
                <p class="scan-date">
                    📅 {formatDate(foodData.fecha)}
                </p>
                {#if foodData.tipo_comida}
                    <span class="meal-type-badge">{foodData.tipo_comida}</span>
                {/if}
            </div>
            
            <div class="section-title">
                <span class="icon">📊</span>
                <h3>{$_('foodDetails.nutritionalInfo')}</h3>
            </div>
            
            <div class="nutrition-grid">
                <div class="nutrition-card calories">
                    <div class="card-icon">🔥</div>
                    <div class="card-content">
                        <div class="value">{formatNumber(foodData.calorias)}</div>
                        <div class="label">{$_('foodDetails.calories')}</div>
                        <div class="unit">kcal</div>
                    </div>
                </div>
                
                <div class="nutrition-card protein">
                    <div class="card-icon">🥩</div>
                    <div class="card-content">
                        <div class="value">{formatNumber(foodData.proteinas)}</div>
                        <div class="label">{$_('foodDetails.protein')}</div>
                        <div class="unit">g</div>
                    </div>
                </div>
                
                <div class="nutrition-card carbs">
                    <div class="card-icon">🍞</div>
                    <div class="card-content">
                        <div class="value">{formatNumber(foodData.carbohidratos)}</div>
                        <div class="label">{$_('foodDetails.carbs')}</div>
                        <div class="unit">g</div>
                    </div>
                </div>
                
                <div class="nutrition-card fat">
                    <div class="card-icon">🥑</div>
                    <div class="card-content">
                        <div class="value">{formatNumber(foodData.grasas)}</div>
                        <div class="label">{$_('foodDetails.fat')}</div>
                        <div class="unit">g</div>
                    </div>
                </div>
            </div>
            
            {#if foodData.cantidad_consumida}
                <div class="serving-info">
                    <span class="icon">🍽️</span>
                    <span>{$_('foodDetails.servingInfo')}: <strong>{foodData.cantidad_consumida}g</strong></span>
                </div>
            {/if}
            
            <div class="section-title">
                <span class="icon">ℹ️</span>
                <h3>{$_('foodDetails.additionalInfo')}</h3>
            </div>
            
            <div class="info-card">
                <div class="info-row">
                    <span class="info-label">{$_('foodDetails.registrationMethod')}:</span>
                    <span class="info-value">{foodData.metodo_registro || $_('foodDetails.notSpecified')}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">{$_('foodDetails.mealType')}:</span>
                    <span class="info-value">{foodData.tipo_comida || $_('foodDetails.notSpecified')}</span>
                </div>
            </div>
            
            <div class="actions">
                <button class="btn-secondary" on:click={goBack}>
                    🏠 {$_('foodDetails.backToHome')}
                </button>
            </div>
        </div>
    {/if}
</div>

<style>
    .food-details-container {
        min-height: 100vh;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding-bottom: 2rem;
    }
    
    .loading {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        color: white;
        text-align: center;
        padding: 2rem;
    }
    
    .loading p {
        margin-top: 1rem;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .spinner {
        width: 60px;
        height: 60px;
        border: 5px solid rgba(255, 255, 255, 0.3);
        border-top-color: white;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    .error-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        color: white;
        text-align: center;
        padding: 2rem;
    }
    
    .error-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .error-container h2 {
        font-size: 2rem;
        margin: 0 0 1rem 0;
    }
    
    .error-container p {
        font-size: 1.1rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .header {
        padding: 1.5rem;
        background: transparent;
    }
    
    .back-btn {
        background: rgba(255, 255, 255, 0.25);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-size: 1rem;
        cursor: pointer;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        transition: all 0.3s;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: 600;
    }
    
    .back-btn:hover {
        background: rgba(255, 255, 255, 0.35);
        transform: translateX(-5px);
    }
    
    .back-btn:active {
        transform: translateX(-3px) scale(0.98);
    }
    
    .back-icon {
        font-size: 1.2rem;
        font-weight: bold;
    }
    
    .header h1 {
        color: white;
        font-size: 2rem;
        margin: 0;
        font-weight: 700;
    }
    
    .content {
        background: white;
        border-radius: 30px 30px 0 0;
        padding: 2rem 1.5rem;
        box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.15);
        min-height: calc(100vh - 150px);
    }
    
    .image-container {
        width: 100%;
        height: 280px;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 1.5rem;
        position: relative;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }
    
    .image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .image-overlay {
        position: absolute;
        top: 1rem;
        right: 1rem;
    }
    
    .scan-badge {
        background: rgba(76, 175, 80, 0.95);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        backdrop-filter: blur(10px);
        display: inline-block;
    }
    
    .food-info {
        margin-bottom: 2rem;
    }
    
    .food-info h2 {
        color: #2d3436;
        margin: 0 0 0.5rem 0;
        font-size: 1.75rem;
        font-weight: 700;
    }
    
    .scan-date {
        color: #636e72;
        font-size: 0.95rem;
        margin: 0 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .meal-type-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .section-title {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 2rem 0 1rem 0;
    }
    
    .section-title .icon {
        font-size: 1.5rem;
    }
    
    .section-title h3 {
        margin: 0;
        font-size: 1.3rem;
        color: #2d3436;
        font-weight: 700;
    }
    
    .nutrition-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .nutrition-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        transition: all 0.3s;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.75rem;
    }
    
    .nutrition-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }
    
    .nutrition-card.calories {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
    }
    
    .nutrition-card.protein {
        background: linear-gradient(135deg, #fab1a0 0%, #ff7675 100%);
    }
    
    .nutrition-card.carbs {
        background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%);
    }
    
    .nutrition-card.fat {
        background: linear-gradient(135deg, #55efc4 0%, #00b894 100%);
    }
    
    .card-icon {
        font-size: 2.5rem;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
    }
    
    .card-content {
        width: 100%;
    }
    
    .value {
        font-size: 2rem;
        font-weight: 800;
        color: #2d3436;
        margin-bottom: 0.25rem;
        line-height: 1;
    }
    
    .label {
        font-size: 0.9rem;
        color: #2d3436;
        font-weight: 600;
        margin-bottom: 0.25rem;
    }
    
    .unit {
        font-size: 0.75rem;
        color: #636e72;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .serving-info {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 15px;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 2rem;
        border-left: 4px solid #667eea;
    }
    
    .serving-info .icon {
        font-size: 1.5rem;
    }
    
    .serving-info strong {
        color: #667eea;
        font-weight: 700;
    }
    
    .info-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    
    .info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem 0;
    }
    
    .info-row:not(:last-child) {
        border-bottom: 1px solid #e0e0e0;
    }
    
    .info-label {
        color: #636e72;
        font-size: 0.95rem;
        font-weight: 500;
    }
    
    .info-value {
        color: #2d3436;
        font-size: 0.95rem;
        font-weight: 600;
        text-transform: capitalize;
    }

    .debug-panel {
        background: #f0f0f0;
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        margin: 2rem 0;
        overflow-x: auto;
    }

    .debug-panel h4 {
        margin: 0 0 0.5rem 0;
        color: #333;
    }

    .debug-panel pre {
        margin: 0;
        font-size: 0.85rem;
        color: #555;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    
    .actions {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .btn-primary,
    .btn-secondary {
        padding: 1rem 2rem;
        border: none;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    .btn-primary:active {
        transform: translateY(0);
    }
    
    .btn-secondary {
        background: white;
        color: #667eea;
        border: 2px solid #667eea;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    .btn-secondary:hover {
        background: #f8f9fa;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
    }
    
    .btn-secondary:active {
        transform: translateY(0);
    }
    
    @media screen and (max-width: 375px) {
        .content {
            padding: 1.5rem 1rem;
        }
        
        .header h1 {
            font-size: 1.75rem;
        }
        
        .food-info h2 {
            font-size: 1.5rem;
        }
        
        .nutrition-grid {
            gap: 0.75rem;
        }
        
        .nutrition-card {
            padding: 1rem;
        }
        
        .card-icon {
            font-size: 2rem;
        }
        
        .value {
            font-size: 1.75rem;
        }
    }
    
    @media screen and (min-width: 768px) {
        .content {
            max-width: 600px;
            margin: 0 auto;
            border-radius: 30px;
        }
        
        .actions {
            flex-direction: row;
        }
        
        .btn-primary,
        .btn-secondary {
            flex: 1;
        }
    }
</style>