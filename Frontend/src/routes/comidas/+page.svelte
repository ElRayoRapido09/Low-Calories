<script>
  let query = '';
  let results = [];
  let loading = false;
  let error = '';

  async function searchFood() {
    if (!query.trim()) return;
    loading = true;
    error = '';
    try {
      const response = await fetch(`http://localhost:8000/api/food-search/?q=${encodeURIComponent(query)}`);
      console.log('Estado de respuesta:', response.status);  // Log del código HTTP
      if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
      const data = await response.json();
      console.log('Datos crudos de la API:', data);  // Log completo de la respuesta
      results = data.foods?.food || [];
      console.log('Resultados extraídos:', results);  // Log de los resultados procesados
    } catch (err) {
      console.error('Error capturado:', err);  // Log de errores
      error = err.message;
      results = [];
    } finally {
      loading = false;
    }
  }
</script>

<main>
  <input bind:value={query} placeholder="Buscar alimento (en inglés, ej. avocado)" />
  <button on:click={searchFood} disabled={loading}>Buscar</button>
  {#if loading}
    <p>Cargando...</p>
  {/if}
  {#if error}
    <p style="color: red;">{error}</p>
  {/if}
  {#if results.length > 0}
    <ul>
      {#each results as food}
        <li>{food.food_name || 'Sin nombre'} - {food.food_description || 'Sin descripción'}</li>
      {/each}
    </ul>
  {:else if !loading && query}
    <p>No se encontraron resultados. Prueba con términos en inglés.</p>
  {/if}
</main>