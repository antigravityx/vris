# 🚀 Guía de Despliegue - VRIS

## 📋 Opciones de Despliegue

### Opción 1: Railway (⭐ Recomendado)

Railway es la forma más fácil de desplegar VRIS con despliegue automático desde GitHub.

#### Paso 1: Crear cuenta en Railway
1. Ve a https://railway.app
2. Regístrate con GitHub
3. Obtienes $5 de crédito gratis cada mes

#### Paso 2: Configurar base de datos
```bash
# En Railway dashboard:
1. Click "New Project"
2. Click "Deploy PostgreSQL"
3. Copia la DATABASE_URL
```

#### Paso 3: Desplegar aplicación
```bash
# Opción A: Desde dashboard
1. Click "New" > "GitHub Repo"
2. Selecciona el repo VRIS
3. Railway detecta automáticamente el Dockerfile

# Opción B: Desde CLI
npm i -g @railway/cli
railway login
railway init
railway up
```

#### Paso 4: Configurar variables de entorno
```bash
# En Railway dashboard > Variables
DATABASE_URL=<la URL de PostgreSQL>
SECRET_KEY=<genera una clave segura>
API_KEY_LIBRO=libro-secret-key
API_KEY_VERIXMUSIC=verixmusic-secret-key
HUGGINGFACE_API_KEY=<tu clave de HF>
ENVIRONMENT=production
DEBUG=False
```

---

### Opción 2: Render

#### Paso 1: Crear cuenta
1. Ve a https://render.com
2. Regístrate con GitHub

#### Paso 2: Crear PostgreSQL
```bash
1. Click "New" > "PostgreSQL"
2. Nombre: vris-db
3. Plan: Free
4. Copia la Internal Database URL
```

#### Paso 3: Crear Web Service
```bash
1. Click "New" > "Web Service"
2. Conecta repo GitHub
3. Configuración:
   - Name: vris
   - Environment: Docker
   - Plan: Free
```

#### Paso 4: Variables de entorno
Agrega las mismas variables que Railway

---

### Opción 3: Google Cloud Run

```bash
# 1. Instalar gcloud CLI
# 2. Autenticar
gcloud auth login

# 3. Configurar proyecto
gcloud config set project YOUR_PROJECT_ID

# 4. Build y deploy
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/vris
gcloud run deploy vris \
  --image gcr.io/YOUR_PROJECT_ID/vris \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 🗄️ Base de Datos

### Neon.tech (PostgreSQL gratis)

1. Crear cuenta: https://neon.tech
2. Crear proyecto
3. Crear database "vris_db"
4. Copiar connection string
5. Agregar a DATABASE_URL

### Supabase (Alternativa)

1. Crear cuenta: https://supabase.com
2. Nuevo proyecto
3. Settings > Database > Connection string
4. Usar modo "Session" para connection pooling

---

## 🔑 Secrets y API Keys

### Generar SECRET_KEY

```python
import secrets
print(secrets.token_urlsafe(32))
```

### Hugging Face API Key

1. Crear cuenta: https://huggingface.co
2. Settings > Access Tokens
3. Crear nuevo token
4. Copiar y agregar a HUGGINGFACE_API_KEY

---

## ✅ Verificación Post-Despliegue

```bash
# 1. Health check
curl https://your-vris-url.com/health

# 2. Docs interactivos
https://your-vris-url.com/docs

# 3. Test authentication
curl -X POST https://your-vris-url.com/api/auth/token \
  -H "Authorization: Bearer libro-api-key"
```

---

## 📊 Monitoreo

### Railway
- Logs automáticos en dashboard
- Métricas de CPU/RAM
- Alertas configurables

### Render
- Logs en tiempo real
- Auto-scaling
- Health checks

---

## 🔄 CI/CD Automático

El repositorio ya incluye GitHub Actions para deploy automático.

```yaml
# .github/workflows/deploy.yml
# Cada push a main despliega automáticamente
```

---

## 🆘 Troubleshooting

### Error: Database connection failed
```bash
# Verifica que DATABASE_URL sea correcta
# Debe ser formato: postgresql+asyncpg://...
```

### Error: Module not found
```bash
# Asegúrate que requirements.txt esté actualizado
pip freeze > requirements.txt
```

### Error: Port already in use
```bash
# Railway asigna puerto automáticamente vía $PORT
# Localmente usa: uvicorn app.main:app --port 8000
```

---

## 💡 Tips de Producción

1. **Siempre usa HTTPS** (Railway/Render lo incluyen gratis)
2. **Rota API keys** regularmente
3. **Monitorea logs** diariamente
4. **Backups de DB** semanalmente (Neon los hace automáticamente)
5. **Rate limiting** en endpoints públicos

---

## 📞 Soporte

- Docs: Ver README.md principal
- Issues: GitHub Issues
- Comunidad: [Coming Soon]

**¡VRIS listo para producción! 🚀**
