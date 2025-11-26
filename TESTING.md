# 🧪 Guía de Testing Local - VRIS

## 🐳 Opción 1: Docker Compose (Recomendado)

La forma más fácil de probar VRIS localmente con base de datos incluida.

### Requisitos
- Docker Desktop instalado
- 4GB RAM disponible

### Paso 1: Clonar y configurar

```bash
cd vris
copy .env.example .env
```

### Paso 2: Levantar todo con Docker

```bash
docker-compose up -d
```

Esto levanta:
- ✅ FastAPI app en http://localhost:8000
- ✅ PostgreSQL en puerto 5432
- ✅ Redis en puerto 6379

### Paso 3: Verificar

```bash
# Ver logs
docker-compose logs -f app

# Health check
curl http://localhost:8000/health

# Docs interactivos
# Abrir: http://localhost:8000/docs
```

### Comandos útiles

```bash
# Ver contenedores corriendo
docker-compose ps

# Parar todo
docker-compose down

# Parar y borrar datos
docker-compose down -v

# Rebuild después de cambios
docker-compose up -d --build
```

---

## 🐍 Opción 2: Python Virtual Environment

Para desarrollo sin Docker.

### Requisitos
- Python 3.11+
- PostgreSQL instalado localmente
- Redis instalado localmente (opcional)

### Paso 1: Instalar PostgreSQL

#### Windows
```powershell
# Descargar desde: https://www.postgresql.org/download/windows/
# Instalar con pgAdmin
# Crear base de datos "vris_db"
```

#### Linux/Mac
```bash
# Linux
sudo apt update
sudo apt install postgresql postgresql-contrib

# Mac
brew install postgresql@15
brew services start postgresql@15

# Crear base de datos
createdb vris_db
```

### Paso 2: Setup Python

```bash
# Crear entorno virtual
python -m venv venv

# Activar
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Configurar .env

```bash
# Copiar ejemplo
copy .env.example .env

# Editar .env con tus credenciales locales
# DATABASE_URL=postgresql://postgres:password@localhost:5432/vris_db
```

### Paso 4: Correr servidor

```bash
# Development mode con auto-reload
uvicorn app.main:app --reload --port 8000

# O directamente con Python
python -m app.main
```

### Paso 5: Verificar

```
✅ API: http://localhost:8000
✅ Docs: http://localhost:8000/docs
✅ ReDoc: http://localhost:8000/redoc
```

---

## 🧪 Testing de Endpoints

### 1. Health Check

```bash
curl http://localhost:8000/health
```

### 2. Autenticación

```bash
# Obtener token
curl -X POST http://localhost:8000/api/auth/token \
  -H "Authorization: Bearer libro-api-key"

# Guarda el access_token de la respuesta
```

### 3. Trackear evento

```bash
curl -X POST http://localhost:8000/api/users/track \
  -H "Authorization: Bearer <tu-access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "external_id": "user123",
    "event_type": "book_view",
    "event_data": {"book_id": "libro_1", "title": "Python ML"}
  }'
```

### 4. Obtener recomendaciones

```bash
curl -X POST "http://localhost:8000/api/recommendations/books?user_id=user123&limit=5" \
  -H "Authorization: Bearer <tu-access-token>"
```

### 5. Análisis de sentimiento

```bash
curl -X POST http://localhost:8000/api/nlp/sentiment \
  -H "Authorization: Bearer <tu-access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Este libro es excelente y muy útil"
  }'
```

### 6. Analytics

```bash
curl http://localhost:8000/api/analytics/overview \
  -H "Authorization: Bearer <tu-access-token>"
```

---

## 📊 Usar Swagger UI

La forma más fácil de probar:

1. Abrir http://localhost:8000/docs
2. Click en "Authorize" (arriba derecha)
3. Poner API key: `libro-api-key`
4. Click "Authorize"
5. Ahora puedes probar todos los endpoints desde el navegador

---

## 🔍 Inspeccionar Base de Datos

### Con pgAdmin (GUI)
```bash
# Descargar: https://www.pgadmin.org/
# Conectar a localhost:5432
# User: vris / postgres
# DB: vris_db
```

### Con psql (CLI)
```bash
# Conectar
psql -U vris -d vris_db

# Ver tablas
\dt

# Ver datos
SELECT * FROM users;
SELECT * FROM user_events LIMIT 10;

# Salir
\q
```

---

## 🐛 Troubleshooting

### Puerto 8000 ocupado
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

### No conecta a PostgreSQL
```bash
# Verificar que esté corriendo
# Windows
services.msc (buscar PostgreSQL)

# Linux
sudo systemctl status postgresql

# Mac
brew services list
```

### Errores de importación
```bash
# Reinstalar dependencias
pip install --upgrade -r requirements.txt

# O reinstalar todo
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

---

## ✅ Checklist de Testing

- [ ] Health check responde OK
- [ ] Docs accesibles en /docs
- [ ] Autenticación funciona
- [ ] Puede crear usuarios
- [ ] Tracking de eventos funciona
- [ ] Endpoints de recomendaciones responden
- [ ] Endpoints de NLP responden
- [ ] Analytics devuelve datos
- [ ] Base de datos se conecta
- [ ] Logs se ven claros

---

## 🚀 Próximos Pasos

Una vez todo funciona localmente:

1. Hacer commit de cambios
2. Push a GitHub
3. Seguir DEPLOY.md para producción

**¡Happy coding! 💻✨**
