# Low Calories 🥗

Tu asistente personal de nutrición que te ayuda a mantener un estilo de vida saludable.

## ¿Qué hace el proyecto?

**Low Calories** es una aplicación web de nutrición que permite a los usuarios:

- 📷 **Escanear alimentos**: Toma fotos de tu comida para conocer las calorías al instante
- 🤖 **Asistente IA**: Recibe recomendaciones personalizadas sobre qué comer
- 📊 **Seguimiento de estadísticas**: Visualiza tu progreso diario y semanal de calorías
- 👤 **Perfil personalizado**: Configura tu meta calórica diaria y preferencias
- ⚙️ **Ajustes personalizables**: Adapta la aplicación a tus necesidades

La aplicación incluye:
- **Dashboard principal** con acceso rápido a todas las funciones
- **Página de estadísticas** con progreso semanal y macronutrientes
- **Perfil de usuario** con metas personalizadas
- **Panel de ajustes** para configurar preferencias

## ¿Por qué el proyecto es útil?

- **Simplifica el conteo de calorías**: No más búsquedas manuales en bases de datos
- **Tecnología avanzada**: Utiliza reconocimiento de imágenes para identificar alimentos
- **Seguimiento visual**: Gráficos y estadísticas fáciles de entender
- **Asistente inteligente**: Ayuda personalizada para tomar mejores decisiones alimentarias
- **Acceso multiplataforma**: Funciona en cualquier dispositivo con navegador web

## Arquitectura del Proyecto

- **Frontend**: SvelteKit con Vite (Puerto 5173)
- **Backend**: Django REST Framework (Puerto 8000)
- **Base de datos**: MySQL 8.0 (Puerto 3306)
- **Contenedorización**: Docker y Docker Compose
- **Iconos**: Lucide Svelte

## Cómo comenzar con el proyecto

### Prerrequisitos

- Docker y Docker Compose instalados
- Git
- Puerto 3306, 5173 y 8000 disponibles

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/ElRayoRapido09/Low-Calories.git
   cd Low-Calories
   ```

2. **Configurar el entorno**
   ```bash
   # Crear archivo de dependencias para Django
   echo "Django>=4.2.0
   mysqlclient>=2.1.0
   django-cors-headers>=4.0.0" > Backend/requirements.txt
   ```

3. **Iniciar los servicios con Docker**
   ```bash
   # Iniciar base de datos
   docker-compose up mysql_db -d
   
   # Esperar a que MySQL esté listo y luego iniciar todos los servicios
   docker-compose up
   ```

4. **Acceder a la aplicación**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - Base de datos: localhost:3306

### Comandos útiles

```bash
# Ver logs de servicios
docker-compose logs frontend
docker-compose logs backend

# Ejecutar comandos en contenedores
docker-compose exec backend python manage.py migrate
docker-compose exec frontend npm install

# Detener servicios
docker-compose down
```

## Estructura del Proyecto

```
Low-Calories/
├── Frontend/                 # Aplicación SvelteKit
│   ├── src/
│   │   ├── routes/
│   │   │   ├── +page.svelte         # Página principal
│   │   │   ├── estadisticas/        # Estadísticas y progreso
│   │   │   ├── perfil/              # Perfil de usuario
│   │   │   └── ajustes/             # Configuraciones
│   │   └── lib/                     # Componentes y utilidades
│   └── package.json
├── Backend/                  # API Django
│   ├── lowcalories/
│   │   ├── settings.py              # Configuración Django
│   │   └── urls.py                  # Rutas de la API
│   └── manage.py
├── docker-compose.yml        # Configuración de contenedores
└── README.md                # Este archivo
```

## Dónde recibir ayuda

### Documentación y recursos

- **Documentación oficial de SvelteKit**: https://kit.svelte.dev/docs
- **Documentación de Django**: https://docs.djangoproject.com/
- **Docker Compose**: https://docs.docker.com/compose/

### Soporte del proyecto

- **Issues de GitHub**: [Reportar problemas o solicitar funciones](https://github.com/ElRayoRapido09/Low-Calories/issues)
- **Discusiones**: [Preguntas generales y discusiones](https://github.com/ElRayoRapido09/Low-Calories/discussions)

### Problemas comunes

1. **Puerto ocupado**: Verifica que los puertos 3306, 5173 y 8000 estén libres
2. **MySQL no inicia**: Espera a que el healthcheck pase antes de acceder
3. **Frontend lento**: Usa `docker-compose up frontend --no-deps` para desarrollo

## Quién mantiene y contribuye con el proyecto

### Mantenedor principal

- **ElRayoRapido09** - Creador y mantenedor principal
  - GitHub: [@ElRayoRapido09](https://github.com/ElRayoRapido09)

### Cómo contribuir

1. **Fork** el repositorio
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### Estado del proyecto

- 🚧 **En desarrollo activo**
- 📱 **Versión móvil**: Planificada
- 🤖 **IA avanzada**: En desarrollo
- 📊 **Analytics**: Por implementar

---

**Low Calories** - Tu compañero en el camino hacia una vida más saludable 🌱