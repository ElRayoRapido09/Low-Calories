# Guía de Implementación de i18n en Low-Calories

## ✅ Archivos Completados

Los siguientes archivos ya tienen i18n implementado:

1. **`Frontend/src/routes/+layout.svelte`** - Configuración inicial de i18n
2. **`Frontend/src/routes/ajustes/interfaz/+page.svelte`** - Con selector de idioma funcional
3. **`Frontend/src/routes/ajustes/+page.svelte`** - Completamente traducido
4. **`Frontend/src/lib/i18n.js`** - Configuración de svelte-i18n
5. **`Frontend/src/lib/locales/es.json`** - Traducciones en español
6. **`Frontend/src/lib/locales/en.json`** - Traducciones en inglés

## 📝 Cómo Aplicar Traducciones en los Archivos Restantes

### Paso 1: Importar las funciones de traducción

En el `<script>` de cada archivo .svelte, agregar:

\`\`\`javascript
import { _ } from 'svelte-i18n';
\`\`\`

### Paso 2: Reemplazar textos estáticos por claves de traducción

**Antes:**
\`\`\`svelte
<h1>Mi Perfil</h1>
<p>¡Sigue así, campeón!</p>
\`\`\`

**Después:**
\`\`\`svelte
<h1>{$_('profile.title')}</h1>
<p>{$_('profile.keepGoing')}</p>
\`\`\`

### Paso 3: Para atributos HTML

**Antes:**
\`\`\`svelte
<a href="/ajustes" aria-label="Volver">‹</a>
<input placeholder="Buscar...">
\`\`\`

**Después:**
\`\`\`svelte
<a href="/ajustes" aria-label={$_('common.back')}>‹</a>
<input placeholder={$_('common.search')}>
\`\`\`

## 📋 Archivos Pendientes de Traducción

### Archivos Prioritarios:

1. **`Frontend/src/routes/+page.svelte`** (Home)
   - Títulos: "Low Calories", "Mi Racha", "¿Qué tienes en tu cocina?"
   - Navegación inferior
   - Recomendaciones del día

2. **`Frontend/src/routes/Bot/+page.svelte`** (Chatbot)
   - Ya tiene las claves en `chatbot.*`
   - Reemplazar textos del mensaje de bienvenida

3. **`Frontend/src/routes/perfil/+page.svelte`**
   - Ya tiene las claves en `profile.*`
   - Información personal, metas, tendencias

4. **`Frontend/src/routes/objetivos/+page.svelte`**
   - Ya tiene las claves en `goals.*`
   - Todas las vistas del flujo de objetivos

5. **`Frontend/src/routes/estadisticas/+page.svelte`**
   - Ya tiene las claves en `statistics.*`
   - Progreso semanal, macronutrientes

6. **`Frontend/src/routes/login/+page.svelte`**
   - Ya tiene las claves en `login.*`
   - Formularios de login/registro

7. **`Frontend/src/routes/comidas/+page.svelte`**
   - Ya tiene las claves en `foods.*`
   - Búsqueda de alimentos

## 🔧 Ejemplo Completo: Chatbot

\`\`\`svelte
<script>
  import { _ } from 'svelte-i18n';
  import { onMount } from 'svelte';

  let messages = $state([
    {
      id: 1,
      content: $_('chatbot.welcome'),
      sender: 'bot',
      timestamp: new Date().toLocaleTimeString()
    }
  ]);

  let newMessage = $state('');
  // ... resto del código
</script>

<main class="chat-main">
  <header class="chat-header">
    <a href="/" class="back-btn" aria-label={$_('common.back')}>‹</a>
    <div class="header-content">
      <h1>{$_('chatbot.title')}</h1>
      <p>{$_('chatbot.poweredBy')}</p>
    </div>
  </header>

  <!-- ... resto del HTML con traducciones -->

  <div class="chat-input-container">
    <textarea
      bind:value={newMessage}
      placeholder={$_('chatbot.placeholder')}
      class="chat-input"
    ></textarea>
    <button title={$_('chatbot.send')}>
      📤
    </button>
  </div>
</main>
\`\`\`

## 🎯 Selector de Idioma

El selector de idioma está implementado en `/ajustes/interfaz`:

\`\`\`javascript
import { _, locale } from 'svelte-i18n';

let currentLang = $state($locale || 'es');

function changeLanguage(lang) {
  locale.set(lang);
  currentLang = lang;
  if (typeof localStorage !== 'undefined') {
    localStorage.setItem('locale', lang);
  }
}
\`\`\`

## 📚 Agregar Nuevas Traducciones

Si necesitas agregar nuevas claves de traducción:

1. Abre `Frontend/src/lib/locales/es.json`
2. Agrega la nueva clave en la sección apropiada:

\`\`\`json
{
  "myNewSection": {
    "title": "Mi Nuevo Título",
    "description": "Mi descripción"
  }
}
\`\`\`

3. Repite en `Frontend/src/lib/locales/en.json` con la traducción en inglés

## 🚀 Próximos Pasos

1. Aplicar traducciones en los archivos restantes siguiendo los ejemplos
2. Probar el cambio de idioma en `/ajustes/interfaz`
3. Verificar que todos los textos se traduzcan correctamente
4. Agregar más idiomas si es necesario (crear `fr.json`, etc.)

## 💡 Notas Importantes

- El idioma se guarda en `localStorage` para persistir entre sesiones
- El idioma inicial se detecta automáticamente del navegador
- Todas las traducciones están centralizadas en los archivos JSON
- Usa `$_()` para texto reactivo que cambia al cambiar el idioma
