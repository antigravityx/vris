# 🎯 GUÍA VISUAL - Deploy VRIS a Railway

## 🌟 PASO 1: Crear Cuenta GitHub (Si no tienes)

```
┌─────────────────────────────────────────┐
│         🌐 github.com/signup            │
│                                         │
│  1. Email: tu-email@ejemplo.com         │
│  2. Password: ************              │
│  3. Username: tu-usuario                │
│  4. Verificar email                     │
│  5. ¡Listo!                             │
└─────────────────────────────────────────┘
```

## 🚀 PASO 2: Crear Repositorio en GitHub

### Ve a: https://github.com/new

```
┌────────────────────────────────────────────┐
│  Create a new repository                   │
│                                            │
│  Repository name *                         │
│  ┌──────────────────┐                      │
│  │ vris             │                      │
│  └──────────────────┘                      │
│                                            │
│  Description (optional)                    │
│  ┌──────────────────────────────────────┐  │
│  │ VerixRichon Intelligence System -    │  │
│  │ AI/ML Microservice                   │  │
│  └──────────────────────────────────────┘  │
│                                            │
│  ○ Public  ⬤ Private                       │
│                                            │
│  ☐ Add a README file                       │
│  ☐ Add .gitignore                          │
│  ☐ Choose a license                        │
│                                            │
│     [Create repository]                    │
└────────────────────────────────────────────┘
```

**⚠️ IMPORTANTE**: 
- Selecciona **PUBLIC**
- **NO marques** ningún checkbox (ya tenemos README, .gitignore, LICENSE)

## 📤 PASO 3: Subir Código a GitHub

Una vez creado el repo, GitHub te mostrará comandos. Usa estos:

```powershell
# En PowerShell
cd c:\Users\Public\antigravity\vris

# Agregar el remote (CAMBIA tu-usuario por tu username de GitHub)
git remote add origin https://github.com/tu-usuario/vris.git

# Cambiar a rama main
git branch -M main

# Subir código
git push -u origin main
```

### ✅ Verificación
Deberías ver en GitHub:
```
vris/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app/
└── ... (25 archivos en total)
```

---

## ☁️ PASO 4: Railway - Crear Cuenta

### Ve a: https://railway.app

```
┌─────────────────────────────────────────┐
│                                         │
│         🚂 Railway                      │
│                                         │
│   Bring your code,                      │
│   we'll handle the rest.                │
│                                         │
│   [🔗 Login with GitHub]                │
│                                         │
│         [Start a New Project]           │
│                                         │
└─────────────────────────────────────────┘
```

**Haz click en**: `Login with GitHub`

### Autorizar Railway
```
┌─────────────────────────────────────────┐
│  Authorize Railway                      │
│                                         │
│  Railway by Railway Corp                │
│  wants to access your GitHub account    │
│                                         │
│  This application will be able to:      │
│  ✓ Read your repositories              │
│  ✓ Deploy from your repos              │
│                                         │
│     [Authorize Railway]                 │
└─────────────────────────────────────────┘
```

---

## 🎯 PASO 5: Crear Proyecto en Railway

### En el Dashboard de Railway:

```
┌─────────────────────────────────────────┐
│  Railway Dashboard                      │
│                                         │
│   Your Projects                         │
│                                         │
│   [➕ New Project]  ← CLICK AQUÍ        │
│                                         │
└─────────────────────────────────────────┘
```

### Selecciona "Deploy from GitHub repo"

```
┌─────────────────────────────────────────┐
│  New Project                            │
│                                         │
│  ○ Empty Project                        │
│  ● Deploy from GitHub repo ← SELECCIONA │
│  ○ Deploy from template                 │
│                                         │
│     [Continue]                          │
└─────────────────────────────────────────┘
```

### Selecciona el repo `vris`

```
┌─────────────────────────────────────────┐
│  Select Repository                      │
│                                         │
│  🔍 Search repositories...              │
│                                         │
│  ☐ tu-usuario/vris  ← SELECCIONA ESTE  │
│     VerixRichon Intelligence System     │
│                                         │
│  ☐ tu-usuario/otro-repo                 │
│                                         │
│     [Deploy Now]                        │
└─────────────────────────────────────────┘
```

**Railway detectará automáticamente el Dockerfile y empezará a hacer deploy!** 🎉

---

## 🗄️ PASO 6: Agregar PostgreSQL

### En el proyecto, click en "➕ New"

```
┌─────────────────────────────────────────┐
│  Project: vris                          │
│                                         │
│  ┌──────────┐                           │
│  │  vris    │  ← Tu servicio            │
│  │ (Building)                           │
│  └──────────┘                           │
│                                         │
│   [➕ New] ← CLICK AQUÍ                 │
│                                         │
└─────────────────────────────────────────┘
```

### Selecciona "Database" → "Add PostgreSQL"

```
┌─────────────────────────────────────────┐
│  Add Service                            │
│                                         │
│  Database                               │
│  ├─ PostgreSQL  ← CLICK                 │
│  ├─ MySQL                               │
│  ├─ MongoDB                             │
│  └─ Redis                               │
│                                         │
└─────────────────────────────────────────┘
```

**Railway creará automáticamente una base de datos PostgreSQL!** 📊

---

## ⚙️ PASO 7: Configurar Variables de Entorno

### 1. Click en tu servicio `vris`

```
┌─────────────────────────────────────────┐
│  Project: vris                          │
│                                         │
│  ┌──────────┐   ┌────────────┐         │
│  │  vris    │   │ PostgreSQL │         │
│  │ (Active) │   │  (Active)  │         │
│  └──────────┘   └────────────┘         │
│       ↑                                 │
│    CLICK AQUÍ                           │
└─────────────────────────────────────────┘
```

### 2. Ve a la pestaña "Variables"

```
┌─────────────────────────────────────────┐
│  vris                                   │
│                                         │
│  Settings | Variables | Deployments     │
│              ↑↑↑↑↑↑↑↑                   │
│           CLICK AQUÍ                    │
└─────────────────────────────────────────┘
```

### 3. Agregar cada variable:

Click en "➕ New Variable" y agrega una por una:

```
┌─────────────────────────────────────────┐
│  Variables                              │
│                                         │
│  Key                   Value            │
│  ┌──────────────┐    ┌──────────────┐  │
│  │ SECRET_KEY   │    │ OJXt7vH3Pq...│  │
│  └──────────────┘    └──────────────┘  │
│                                         │
│  Key                   Value            │
│  ┌──────────────┐    ┌──────────────┐  │
│  │ ENVIRONMENT  │    │ production   │  │
│  └──────────────┘    └──────────────┘  │
│                                         │
│  [➕ New Variable]                      │
└─────────────────────────────────────────┘
```

**VARIABLES A AGREGAR:**

```plaintext
1. SECRET_KEY
   Valor: OJXt7vH3PqKLm9nR4sT8uB2wC5xD6yE1fG0hI3jK4lM7nP9qR

2. API_KEY_LIBRO
   Valor: libro-secret-vris-2025

3. API_KEY_VERIXMUSIC
   Valor: verixmusic-secret-vris-2025

4. API_KEY_DASHBOARD
   Valor: dashboard-secret-vris-2025

5. ENVIRONMENT
   Valor: production

6. DEBUG
   Valor: False

7. CORS_ORIGINS
   Valor: http://localhost:3000,https://libro.github.io

8. LOG_LEVEL
   Valor: INFO
```

### 4. Conectar DATABASE_URL

**⚠️ IMPORTANTE**: Para DATABASE_URL:

1. Click en el servicio **PostgreSQL** (no vris)
2. En la pestaña "Connect" verás algo como:
   ```
   DATABASE_URL
   postgresql://postgres:password@host:5432/railway
   ```
3. **Copia ese valor EXACTAMENTE**
4. Vuelve al servicio `vris`
5. En Variables, agrega:
   ```
   Key: DATABASE_URL
   Value: <pegar el valor que copiaste>
   ```

**🔧 MODIFICACIÓN**: Cambia `postgresql://` por `postgresql+asyncpg://`
```
Ejemplo:
postgresql+asyncpg://postgres:abc123@containers-us-west.railway.app:5432/railway
```

---

## 🚀 PASO 8: Deploy!

Railway despliega automáticamente cuando agregas las variables.

### Ver el progreso:

```
┌─────────────────────────────────────────┐
│  vris → Deployments                     │
│                                         │
│  🔵 Building...                         │
│  ├─ Fetching source                     │
│  ├─ Building Docker image               │
│  └─ Deploying...                        │
│                                         │
│  ⏱️ ~2-3 minutos                        │
└─────────────────────────────────────────┘
```

### Cuando termine:

```
┌─────────────────────────────────────────┐
│  vris → Deployments                     │
│                                         │
│  ✅ Success!                            │
│                                         │
│  🌐 https://vris-production.up.        │
│     railway.app                         │
│                                         │
│     [Open App]                          │
└─────────────────────────────────────────┘
```

---

## ✅ PASO 9: Verificar que funciona

### 1. Obtener la URL

En Railway, tu servicio `vris` tendrá un botón "Settings" → "Generate Domain"

```
Tu URL será algo como:
https://vris-production-abc123.up.railway.app
```

### 2. Health Check

Abre en el navegador:
```
https://TU-URL.railway.app/health
```

Deberías ver:
```json
{
  "status": "healthy",
  "environment": "production",
  "database": "connected",
  "cache": "disabled"
}
```

### 3. Ver Documentación

Abre:
```
https://TU-URL.railway.app/docs
```

Verás la interfaz Swagger con todos los endpoints! 🎉

---

## 🎊 ¡ÉXITO!

```
     ✨ VRIS ESTÁ EN ÓRBITA ✨

  🌍 → 🛰️ → ☁️ → 🚀 → ✨

   Tu API está VIVA en la nube!
```

### 📝 Guarda esta información:

```
URL de VRIS: https://<tu-url>.railway.app
API Key Libro: libro-secret-vris-2025
API Key VerixMusic: verixmusic-secret-vris-2025
Docs: https://<tu-url>.railway.app/docs
```

---

## 🧪 Probar la API

### Desde PowerShell:

```powershell
# Health check
curl https://TU-URL.railway.app/health

# Obtener token
curl -X POST https://TU-URL.railway.app/api/auth/token `
  -H "Authorization: Bearer libro-secret-vris-2025"

# Trackear evento
curl -X POST https://TU-URL.railway.app/api/users/track `
  -H "Authorization: Bearer TU-TOKEN-AQUI" `
  -H "Content-Type: application/json" `
  -d '{"external_id":"user001","event_type":"test","event_data":{}}'
```

---

## 💰 Costos

Railway te da **$5 USD/mes GRATIS** 🎉

Esto alcanza para:
- ~450 horas de compute
- Perfecto para desarrollo
- Suficiente para empezar

---

## 🆘 Si algo falla

### Build Error
- Ver logs en Railway Deployments
- Verificar que todas las variables estén configuradas
- DATABASE_URL debe incluir `+asyncpg`

### Database Connection Error
- Verificar DATABASE_URL
- Debe empezar con `postgresql+asyncpg://`

### 404 No encontrado
- Esperar 1-2 minutos más
- Railway puede tardar en propagar DNS

---

## ✅ Checklist Final

- [ ] Repo creado en GitHub
- [ ] Código subido
- [ ] Cuenta Railway creada
- [ ] Proyecto desplegado
- [ ] PostgreSQL agregado
- [ ] Variables configuradas
- [ ] Deploy exitoso
- [ ] Health check OK
- [ ] Docs accesibles

**¡VRIS ESTÁ FLOTANDO EN LA NUBE! 🚀✨**
