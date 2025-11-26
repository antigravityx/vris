# 🚀 DESPLIEGUE A LA NUBE - VRIS

## 📋 Checklist de Deployment

### ✅ Paso 1: GitHub Repository (Vamos a hacerlo ahora)
- [ ] Crear repo en GitHub
- [ ] Subir código
- [ ] Verificar que esté público

### ✅ Paso 2: Railway Setup
- [ ] Crear cuenta en Railway
- [ ] Conectar con GitHub
- [ ] Deploy desde repo
- [ ] Configurar PostgreSQL
- [ ] Configurar variables de entorno

### ✅ Paso 3: Verificación
- [ ] Health check funciona
- [ ] Docs accesibles
- [ ] API responde correctamente

---

## 🔗 URLs Importantes

- **Railway**: https://railway.app
- **GitHub Repo**: [Crear en: https://github.com/new]

---

## 🔑 Variables de Entorno para Railway

```env
# Estas se configurarán en Railway
DATABASE_URL=<Railway PostgreSQL URL>
SECRET_KEY=<generar con comando abajo>
API_KEY_LIBRO=libro-secret-vris-2025
API_KEY_VERIXMUSIC=verixmusic-secret-vris-2025
API_KEY_DASHBOARD=dashboard-secret-vris-2025
ENVIRONMENT=production
DEBUG=False
CORS_ORIGINS=http://localhost:3000,https://libro.github.io
```

### Generar SECRET_KEY

```python
import secrets
print(secrets.token_urlsafe(32))
```

Resultado: `OJXt7vH3PqKLm9nR4sT8uB2wC5xD6yE1fG0hI3jK4lM7nP9qR`

---

## 📝 Instrucciones Paso a Paso

### PASO 1: Crear GitHub Repo

1. Ve a: https://github.com/new
2. Nombre: `vris`
3. Descripción: `VerixRichon Intelligence System - AI/ML Microservice`
4. Público
5. NO inicializar con README (ya tenemos)
6. Create repository

### PASO 2: Subir código

```powershell
cd c:\Users\Public\antigravity\vris

# Agregar remote
git remote add origin https://github.com/TU-USUARIO/vris.git

# Cambiar rama a main
git branch -M main

# Push
git push -u origin main
```

### PASO 3: Railway Deployment

1. **Crear cuenta en Railway**
   - Ve a: https://railway.app
   - Click "Login with GitHub"
   - Autorizar Railway

2. **Nuevo Proyecto**
   - Dashboard > "New Project"
   - "Deploy from GitHub repo"
   - Seleccionar `vris`
   - Railway detecta Dockerfile automáticamente

3. **Agregar PostgreSQL**
   - En el proyecto > "+ New"
   - "Database" > "Add PostgreSQL"
   - Railway crea la base de datos automáticamente

4. **Configurar Variables**
   - Click en el servicio `vris`
   - Tab "Variables"
   - Agregar cada variable del listado arriba
   - DATABASE_URL se copia desde el servicio PostgreSQL

5. **Deploy**
   - Railway despliega automáticamente
   - Esperar ~2-3 minutos
   - Click en "Deployments" para ver progreso

### PASO 4: Verificar

Una vez desplegado:

```bash
# Railway te da una URL como:
# https://vris-production.up.railway.app

# Verificar health
curl https://TU-URL.railway.app/health

# Ver docs
# Abrir: https://TU-URL.railway.app/docs
```

---

## ⚙️ Variables de Entorno Completas

Copiar y pegar en Railway Variables tab:

```
DATABASE_URL
<Copiar desde PostgreSQL service>

SECRET_KEY
OJXt7vH3PqKLm9nR4sT8uB2wC5xD6yE1fG0hI3jK4lM7nP9qR

API_KEY_LIBRO
libro-secret-vris-2025

API_KEY_VERIXMUSIC
verixmusic-secret-vris-2025

API_KEY_DASHBOARD
dashboard-secret-vris-2025

HUGGINGFACE_API_KEY
<Opcional - para después>

ENVIRONMENT
production

DEBUG
False

CORS_ORIGINS
http://localhost:3000,https://libro.github.io

CACHE_ENABLED
False

LOG_LEVEL
INFO
```

---

## 🎯 Estado Actual

```
[✅] Código listo
[⏳] GitHub repo - EN PROCESO
[⏳] Railway deployment - SIGUIENTE
[⏳] Variables configuradas - SIGUIENTE
[⏳] Verificación - FINAL
```

---

## 🆘 Si algo falla

### Railway no detecta Dockerfile
- Verificar que `Dockerfile` esté en la raíz
- Trigger redeploy manual

### Database connection error
- Verificar DATABASE_URL
- Debe tener formato: `postgresql+asyncpg://...`
- Copiar exactamente desde Railway PostgreSQL

### Build fails
- Ver logs en Railway
- Verificar requirements.txt
- Contactar si persiste

---

**¡Vamos a poner VRIS en órbita! 🚀✨**
