import { register, init, getLocaleFromNavigator } from 'svelte-i18n';
import { browser } from '$app/environment';

register('es', () => import('./locales/es.json'));
register('en', () => import('./locales/en.json'));

init({
  fallbackLocale: 'es',
  initialLocale: browser ? (localStorage.getItem('locale') || getLocaleFromNavigator() || 'es') : 'es',
});
