# 🚀 COMANDOS COPY/PASTE - Deploy VRIS

## ⚡ COMANDO 1: Preparar GitHub

**Primero, crea el repo en**: https://github.com/new

Luego ejecuta (CAMBIA `TU-USUARIO` por tu username de GitHub):

```powershell
cd c:\Users\Public\antigravity\vris

git remote add origin https://github.com/TU-USUARIO/vris.git

git branch -M main

git push -u origin main
```

**✅ Resultado esperado:**
```
Enumerating objects: 25, done.
Counting objects: 100% (25/25), done.
Writing objects: 100% (25/25), done.
Total 25 (delta 0), reused 0 (delta 0)
To https://github.com/TU-USUARIO/vris.git
 * [new branch]      main -> main
```

---

## ☁️ PASO 2: Railway

### A. Crear cuenta y proyecto

1. **Abre**: https://railway.app
2. **Click**: "Login with GitHub"
3. **Autoriza** Railway
4. **Click**: "New Project"
5. **Selecciona**: "Deploy from GitHub repo"
6. **Elige**: `vris`
7. **Espera** ~2-3 minutos

### B. Agregar PostgreSQL

1. **Click**: ➕ New
2. **Selecciona**: Database > PostgreSQL
3. **Espera** ~30 segundos

### C. Obtener DATABASE_URL

1. **Click** en el cuadro "PostgreSQL"
2. **Tab**: "Connect"
3. **Copia** el valor de `DATABASE_URL`
4. **Modifica**: Cambia `postgresql://` por `postgresql+asyncpg://`

Ejemplo:
```
Original:
postgresql://postgres:abc123@containers.railway.app:5432/railway

Modificado:
postgresql+asyncpg://postgres:abc123@containers.railway.app:5432/railway
```

### D. Configurar Variables

1. **Click** en el cuadro `vris` (no PostgreSQL)
2. **Tab**: "Variables"
3. **Click**: "New Variable" para cada una:

```plaintext
DATABASE_URL
postgresql+asyncpg://postgres:abc123@containers.railway.app:5432/railway
(Usa el que copiaste y modificaste)

SECRET_KEY
OJXt7vH3PqKLm9nR4sT8uB2wC5xD6yE1fG0hI3jK4lM7nP9qR

API_KEY_LIBRO
libro-secret-vris-2025

API_KEY_VERIXMUSIC
verixmusic-secret-vris-2025

API_KEY_DASHBOARD
dashboard-secret-vris-2025

ENVIRONMENT
production

DEBUG
False

CORS_ORIGINS
http://localhost:3000,https://libro.github.io

LOG_LEVEL
INFO
```

### E. Generar Dominio Público

1. **En el servicio `vris`** > Settings
2. **Scroll** hasta "Networking"
3. **Click**: "Generate Domain"
4. **Copia** la URL (algo como: `vris-production-abc123.up.railway.app`)

---

## ✅ PASO 3: Verificar

### Health Check

Abre en el navegador (CAMBIA la URL por la tuya):

```
https://vris-production-abc123.up.railway.app/health
```

Deberías ver:
```json
{
  "status": "healthy",
  "environment": "production",
  "database": "connected"
}
```

### Ver Documentación API

```
https://vris-production-abc123.up.railway.app/docs
```

---

## 🧪 PASO 4: Probar API

### Desde PowerShell:

```powershell
# CAMBIA la URL por la tuya
$VRIS_URL = "https://vris-production-abc123.up.railway.app"

# 1. Health check
curl "$VRIS_URL/health"

# 2. Obtener token
$response = curl -X POST "$VRIS_URL/api/auth/token" `
  -H "Authorization: Bearer libro-secret-vris-2025"

# 3. Trackear un evento (usa el token del paso 2)
curl -X POST "$VRIS_URL/api/users/track" `
  -H "Authorization: Bearer TU-TOKEN-AQUI" `
  -H "Content-Type: application/json" `
  -d '{
    "external_id": "user_test_001",
    "event_type": "primera_prueba",
    "event_data": {
      "source": "terminal",
      "message": "VRIS en la nube!"
    }
  }'
```

---

## 📊 PASO 5: Ver Base de Datos

### Opción 1: Railway Dashboard

1. **Click** en PostgreSQL
2. **Tab**: "Data"
3. Verás las tablas: `users`, `user_events`, etc.

### Opción 2: Conectar con pgAdmin

Usa las credenciales de Railway:
- Host: `containers-us-west.railway.app`
- Port: `5432`
- Database: `railway`
- User: `postgres`
- Password: (del DATABASE_URL)

---

## 🎊 ¡FELICITACIONES!

```
     ╔═══════════════════════════╗
     ║   VRIS ESTÁ EN ÓRBITA! 🚀 ║
     ╚═══════════════════════════╝

  🌍 Local      →  💻 GitHub
     ↓                  ↓
  ☁️ Railway    →  ✨ LIVE!
```

Tu API está disponible 24/7 en la nube!

---

## 📝 Guarda esta info:

```
═══════════════════════════════════════
  VRIS - Información de Deployment
═══════════════════════════════════════

URL Principal:
https://vris-production-abc123.up.railway.app

Documentación API:
https://vris-production-abc123.up.railway.app/docs

API Keys:
- Libro: libro-secret-vris-2025
- VerixMusic: verixmusic-secret-vris-2025
- Dashboard: dashboard-secret-vris-2025

GitHub Repo:
https://github.com/TU-USUARIO/vris

Railway Dashboard:
https://railway.app/project/[tu-proyecto-id]

═══════════════════════════════════════
```

---

## 🔥 Próximos Pasos

1. ✅ Integrar VRIS con Libro
2. ✅ Implementar ML real (Fase 3)
3. ✅ Conectar Hugging Face
4. ✅ Dashboard analytics
5. ✅ VerixMusic integration

**¡VerixRichon Factory está creciendo! 🚀✨**
