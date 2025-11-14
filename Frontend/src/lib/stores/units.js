import { writable } from 'svelte/store';
import { browser } from '$app/environment';

// Obtener valores iniciales desde localStorage
const getInitialValue = (key, defaultValue) => {
  if (browser) {
    const stored = localStorage.getItem(key);
    return stored || defaultValue;
  }
  return defaultValue;
};

// Store para unidad de masa/volumen
export const massUnit = writable(getInitialValue('massUnit', 'g'));

// Store para unidad de longitud
export const lengthUnit = writable(getInitialValue('lengthUnit', 'cm'));

// Store para unidad de energía
export const energyUnit = writable(getInitialValue('energyUnit', 'kcal'));

// Funciones de conversión
export const conversions = {  
  // Conversiones de masa
  mass: {
    'g-kg': (value) => value / 1000,
    'kg-g': (value) => value * 1000,
    'g-lb': (value) => value * 0.00220462,
    'lb-g': (value) => value / 0.00220462,
    'kg-lb': (value) => value * 2.20462,
    'lb-kg': (value) => value / 2.20462,
  },
  // Conversiones de longitud
  length: {
    'cm-m': (value) => value / 100,
    'm-cm': (value) => value * 100,
    'cm-ft': (value) => value * 0.0328084,
    'ft-cm': (value) => value / 0.0328084,
    'cm-in': (value) => value * 0.393701,
    'in-cm': (value) => value / 0.393701,
  },
  // Conversiones de energía
  energy: {
    'kcal-kj': (value) => value * 4.184,
    'kj-kcal': (value) => value / 4.184,
    'kcal-cal': (value) => value * 1000,
    'cal-kcal': (value) => value / 1000,
  }
};

// Función para convertir valores según las unidades seleccionadas
export function convertValue(value, type, fromUnit, toUnit) {
  if (fromUnit === toUnit) return value;
  
  const conversionKey = `${fromUnit}-${toUnit}`;
  const converter = conversions[type]?.[conversionKey];
  
  if (converter) {
    return converter(value);
  }
  
  return value;
}

// Función para formatear valores con su unidad
export function formatWithUnit(value, unit, decimals = 0) {
  if (value === null || value === undefined) return '-';
  
  // Formato compacto para calorías (cal) cuando son números grandes
  if (unit === 'cal' && value >= 1000) {
    return `${(value / 1000).toFixed(1)}k ${unit}`;
  }
  
  return `${value.toFixed(decimals)} ${unit}`;
}

// Suscribirse a cambios y guardar en localStorage
if (browser) {
  massUnit.subscribe(value => localStorage.setItem('massUnit', value));
  lengthUnit.subscribe(value => localStorage.setItem('lengthUnit', value));
  energyUnit.subscribe(value => localStorage.setItem('energyUnit', value));
}
