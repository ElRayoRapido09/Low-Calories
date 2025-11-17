import { readdir, readFile } from 'fs/promises';
import { join } from 'path';

// Patrones simplificados para detectar texto en español
const spanishWords = /\b(el|la|los|las|de|del|al|un|una|es|en|por|para|con|que|más|año|día|mes)\b/i;

async function scanFile(filePath) {
  const content = await readFile(filePath, 'utf-8');
  const issues = [];
  const lines = content.split('\n');
  
  lines.forEach((line, index) => {
    // Buscar texto entre > y < que no tenga $_
    const matches = line.match(/>([^<{]+)</g);
    
    if (matches) {
      matches.forEach(match => {
        const text = match.slice(1, -1).trim();
        
        // Verificar si es texto en español y no está traducido
        if (text.length > 2 && 
            spanishWords.test(text) && 
            !line.includes('$_') &&
            !line.includes('<!--') &&
            !/^[\d\s\W]+$/.test(text)) {
          
          issues.push({
            line: index + 1,
            text: text.substring(0, 50) + (text.length > 50 ? '...' : '')
          });
        }
      });
    }
  });
  
  return issues;
}

async function scanDirectory(dir, results = { files: 0, issues: 0 }) {
  const entries = await readdir(dir, { withFileTypes: true });
  
  for (const entry of entries) {
    const fullPath = join(dir, entry.name);
    
    if (entry.isDirectory() && !entry.name.startsWith('.') && entry.name !== 'node_modules') {
      await scanDirectory(fullPath, results);
    } else if (entry.name.endsWith('.svelte')) {
      results.files++;
      const issues = await scanFile(fullPath);
      
      if (issues.length > 0) {
        console.log(`\n📄 ${entry.name}`);
        issues.forEach(issue => {
          console.log(`   Línea ${issue.line}: "${issue.text}"`);
        });
        results.issues += issues.length;
      }
    }
  }
  
  return results;
}

// Ejecutar
const routesPath = './src/routes';

console.log('🔍 Buscando textos sin traducir...\n');

scanDirectory(routesPath)
  .then(results => {
    console.log(`\n✅ Archivos escaneados: ${results.files}`);
    console.log(`${results.issues === 0 ? '✅' : '⚠️'} Textos sin traducir: ${results.issues}\n`);
  })
  .catch(err => console.error('❌ Error:', err.message));
