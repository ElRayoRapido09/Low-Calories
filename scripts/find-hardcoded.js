import { readdir, readFile } from 'fs/promises';
import { join } from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Patrones para detectar texto hardcodeado en español
const patterns = [
  // Títulos y encabezados sin traducción
  /<h[1-6]>([A-ZÁÉÍÓÚÑ¿¡][^<{]*[a-záéíóúñ][^<{]*)<\/h[1-6]>/gi,
  
  // Párrafos con texto en español
  /<p>([A-ZÁÉÍÓÚÑ¿¡][^<{]*[a-záéíóúñ][^<{]*)<\/p>/gi,
  
  // Botones con texto hardcodeado
  /<button[^>]*>([A-ZÁÉÍÓÚÑ¿¡][^<{]*[a-záéíóúñ][^<{]*)<\/button>/gi,
  
  // Placeholders sin traducción
  /placeholder="([A-ZÁÉÍÓÚÑ¿¡][^"]*[a-záéíóúñ][^"]*)"/gi,
  
  // Labels de aria sin traducción
  /aria-label="([A-ZÁÉÍÓÚÑ¿¡][^"]*[a-záéíóúñ][^"]*)"/gi,
  
  // Spans con texto
  /<span[^>]*>([A-ZÁÉÍÓÚÑ¿¡][^<{]*[a-záéíóúñ][^<{]*)<\/span>/gi,
];

// Palabras comunes que indican texto en español (para filtrar false positives)
const spanishIndicators = [
  'el', 'la', 'los', 'las', 'de', 'del', 'al', 'un', 'una', 'es', 'en',
  'por', 'para', 'con', 'sin', 'sobre', 'tu', 'su', 'mi', 'que', 'qué'
];

function isLikelySpanish(text) {
  const cleanText = text.toLowerCase().trim();
  
  // Muy corto o solo números/símbolos
  if (cleanText.length < 3 || /^[\d\s\W]+$/.test(cleanText)) {
    return false;
  }
  
  // Contiene $_( = ya está traducido
  if (text.includes('$_(') || text.includes('{$_')) {
    return false;
  }
  
  // Contiene indicadores de español
  const words = cleanText.split(/\s+/);
  return words.some(word => spanishIndicators.includes(word));
}

async function scanFile(filePath) {
  const content = await readFile(filePath, 'utf-8');
  const issues = [];
  
  // Buscar patrones de texto hardcodeado
  patterns.forEach(pattern => {
    let match;
    const regex = new RegExp(pattern);
    
    while ((match = regex.exec(content)) !== null) {
      const text = match[1].trim();
      
      if (isLikelySpanish(text) && !text.includes('$_')) {
        const lineNumber = content.substring(0, match.index).split('\n').length;
        issues.push({
          line: lineNumber,
          text: text,
          context: match[0]
        });
      }
    }
  });
  
  return issues;
}

async function scanDirectory(dir, baseDir = dir) {
  const files = await readdir(dir, { withFileTypes: true });
  let totalIssues = 0;
  
  for (const file of files) {
    const fullPath = join(dir, file.name);
    
    if (file.isDirectory() && !file.name.startsWith('.') && file.name !== 'node_modules') {
      totalIssues += await scanDirectory(fullPath, baseDir);
    } else if (file.name.endsWith('.svelte')) {
      const issues = await scanFile(fullPath);
      
      if (issues.length > 0) {
        const relativePath = fullPath.replace(baseDir, '').replace(/\\/g, '/');
        console.log(`\n📄 ${relativePath}`);
        console.log(`   Encontrados ${issues.length} textos sin traducir:\n`);
        
        issues.forEach(issue => {
          console.log(`   Línea ${issue.line}: "${issue.text}"`);
        });
        
        totalIssues += issues.length;
      }
    }
  }
  
  return totalIssues;
}

// Ejecutar escaneo
const routesPath = join(__dirname, '../Frontend/src/routes');

console.log('🔍 Escaneando archivos .svelte en busca de textos sin traducir...\n');
console.log('═'.repeat(70));

scanDirectory(routesPath)
  .then(total => {
    console.log('\n' + '═'.repeat(70));
    if (total === 0) {
      console.log('\n✅ ¡Perfecto! No se encontraron textos hardcodeados.\n');
    } else {
      console.log(`\n⚠️  Total de textos sin traducir: ${total}`);
      console.log('\n💡 Para traducir estos textos:');
      console.log('   1. Agrega las claves en Frontend/src/lib/locales/es.json y en.json');
      console.log('   2. Reemplaza el texto por {$_(\'seccion.clave\')}\n');
    }
  })
  .catch(err => {
    console.error('❌ Error al escanear:', err);
  });
