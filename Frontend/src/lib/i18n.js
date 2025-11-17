import { register, init, getLocaleFromNavigator } from 'svelte-i18n';
import { browser } from '$app/environment';

register('es', () => import('./locales/es.json'));
register('en', () => import('./locales/en.json'));

init({
  fallbackLocale: 'es',
  initialLocale: browser ? (localStorage.getItem('locale') || getLocaleFromNavigator() || 'es') : 'es',
  
  // Detectar traducciones faltantes automáticamente
  handleMissingMessage: ({ locale, id, defaultValue }) => {
    if (browser && import.meta.env.DEV) {
      console.warn(`⚠️ Traducción faltante: "${id}" en locale "${locale}"`);
    }
    // En desarrollo, marca con emoji rojo para fácil identificación
    return import.meta.env.DEV ? `🔴 ${id}` : defaultValue || id;
  }
});
