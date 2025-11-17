# 🌍 Sistema de Detección de Traducciones

Este proyecto incluye herramientas automáticas para detectar textos sin traducir.

## 🚀 Cómo Usar

### Opción 1: Comando npm (Recomendado)
```bash
cd Frontend
npm run check-translations
```

### Opción 2: Directamente con Node
```bash
node scripts/check-translations.mjs
```

## 📊 Qué Hace

El script escanea todos los archivos `.svelte` y detecta:
- ✅ Títulos sin traducción (`<h1>Texto</h1>`)
- ✅ Párrafos hardcodeados (`<p>Texto</p>`)
- ✅ Botones sin traducir
- ✅ Placeholders en español
- ✅ Spans con texto

### Ejemplo de Salida:
```
🔍 Buscando textos sin traducir...

📄 objetivos/+page.svelte
   Línea 45: "Solo ingredientes"
   Línea 67: "Pollo"

📄 perfil/+page.svelte
   Línea 23: "Configuración"

✅ Archivos escaneados: 23
⚠️ Textos sin traducir: 3
```

## 🔴 Detección Visual en Desarrollo

Cuando el proyecto corre en modo desarrollo (`npm run dev`), los textos sin traducir aparecen marcados con **🔴**:

**Ejemplo:**
- Si usas `{$_('clave.que.no.existe')}` → Muestra: **🔴 clave.que.no.existe**
- En la consola verás: `⚠️ Traducción faltante: "clave.que.no.existe" en locale "es"`

## 📝 Cómo Corregir Textos sin Traducir

1. **Agregar la traducción a los archivos JSON:**

   `Frontend/src/lib/locales/es.json`:
   ```json
   {
     "seccion": {
       "miTexto": "Mi Texto en Español"
     }
   }
   ```

   `Frontend/src/lib/locales/en.json`:
   ```json
   {
     "seccion": {
       "miTexto": "My Text in English"
     }
   }
   ```

2. **Usar la traducción en tu componente:**
   ```svelte
   <script>
     import { _ } from 'svelte-i18n';
   </script>

   <!-- Antes -->
   <h1>Mi Texto</h1>

   <!-- Después -->
   <h1>{$_('seccion.miTexto')}</h1>
   ```

## ⚙️ Configuración

El sistema de detección está configurado en:
- `Frontend/src/lib/i18n.js` - handleMissingMessage
- `scripts/check-translations.mjs` - Script de escaneo

### Desactivar Marcado Visual
Si no quieres ver el 🔴 en desarrollo, comenta estas líneas en `i18n.js`:
```javascript
handleMissingMessage: ({ locale, id }) => {
  // if (browser && import.meta.env.DEV) {
  //   console.warn(`⚠️ Traducción faltante: "${id}" en locale "${locale}"`);
  // }
  return id; // Sin emoji
}
```

## 📌 Notas Importantes

- ✅ **No modifica código existente** - Solo detecta y reporta
- ✅ **Solo activo en desarrollo** - En producción no afecta
- ✅ **Compatible con todo el código actual** - No rompe nada
- ✅ **Se puede ejecutar cuando quieras** - No es obligatorio

## 🎯 Casos de Uso

### Antes de hacer commit
```bash
npm run check-translations
# Verifica que no haya textos sin traducir
```

### Al agregar una nueva página
```bash
npm run check-translations
# Detecta automáticamente textos nuevos
```

### Auditoría completa
```bash
cd Frontend
npm run check-translations > ../translation-report.txt
# Genera reporte completo
```
