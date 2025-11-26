# 🧠 VRIS - VerixRichon Intelligence System

**Sistema de Inteligencia Artificial & Machine Learning 100% Open Source**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)

---

## 🎯 ¿Qué es VRIS?

VRIS es el **cerebro inteligente** de VerixRichon Factory. Un microservicio de IA/ML que aprende continuamente sobre usuarios y comportamientos para potenciar todas las aplicaciones del ecosistema.

### ✨ Características Principales

- 🤖 **Machine Learning**: Recomendaciones y predicciones personalizadas
- 📊 **Analytics**: Análisis profundo de datos y comportamiento
- 🔮 **Predicciones**: Churn prediction, demand forecasting
- 💬 **NLP**: Procesamiento de lenguaje natural con Hugging Face
- 🎯 **Segmentación**: Clustering inteligente de usuarios
- 📈 **Dashboard**: Visualización de métricas en tiempo real

---

## 🏗️ Arquitectura

```
┌──────────────────────────────────────┐
│         VRIS Microservice            │
│  FastAPI + PostgreSQL + Redis + ML   │
└──────────────────────────────────────┘
                ↓ REST APIs
    ┌───────────┴────────────┐
    ↓                        ↓
[Libro]                [VerixMusic]
```

---

## 🛠️ Stack Tecnológico

- **Backend**: FastAPI, Python 3.11+, Uvicorn
- **Database**: PostgreSQL (Neon.tech), Redis (Upstash)
- **ML/AI**: Scikit-learn, Hugging Face, Pandas, NumPy
- **Deploy**: Railway / Render
- **CI/CD**: GitHub Actions

---

## 🚀 Quick Start

### Requisitos
- Python 3.11+
- PostgreSQL
- Redis (opcional para desarrollo)

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/verixrichon/vris.git
cd vris

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Correr migraciones
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

La API estará disponible en: `http://localhost:8000`

Documentación interactiva: `http://localhost:8000/docs`

---

## 📚 Documentación API

### Endpoints Principales

#### 🔐 Autenticación
```http
POST /api/auth/token
```

#### 👥 Usuarios
```http
POST   /api/users/track           # Trackear evento
GET    /api/users/{id}/insights   # Obtener insights
GET    /api/users/segments         # Segmentos
```

#### 🎯 Recomendaciones
```http
POST   /api/recommendations/books
POST   /api/recommendations/music
GET    /api/recommendations/trending
```

#### 🔮 Predicciones
```http
POST   /api/predictions/churn
POST   /api/predictions/purchase
```

#### 💬 NLP
```http
POST   /api/nlp/sentiment
POST   /api/nlp/summarize
POST   /api/nlp/chat
```

#### 📊 Analytics
```http
GET    /api/analytics/overview
GET    /api/analytics/kpis
```

---

## 🗄️ Base de Datos

### Esquema Principal

- `users` - Usuarios centralizados
- `user_events` - Tracking de comportamiento
- `user_preferences` - Preferencias aprendidas
- `ml_models` - Modelos entrenados
- `predictions` - Predicciones generadas

---

## 🔧 Configuración

### Variables de Entorno

```env
# Database
DATABASE_URL=postgresql://user:pass@host:5432/vris
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-secret-key-here
API_KEY_LIBRO=libro-api-key
API_KEY_VERIXMUSIC=verixmusic-api-key

# Hugging Face
HUGGINGFACE_API_KEY=your-hf-api-key

# Environment
ENVIRONMENT=development
```

---

## 🧪 Testing

```bash
# Correr tests
pytest

# Con coverage
pytest --cov=app tests/
```

---

## 📦 Despliegue

### Railway (Recomendado)

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

### Docker

```bash
docker-compose up -d
```

---

## 🤝 Integración

### Ejemplo: Conectar desde Libro

```javascript
const VRIS_API_URL = 'https://vris.railway.app';
const VRIS_API_KEY = 'your-api-key';

// Trackear evento
async function trackEvent(userId, eventType, data) {
  await fetch(`${VRIS_API_URL}/api/users/track`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${VRIS_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user_id: userId,
      app_source: 'libro',
      event_type: eventType,
      event_data: data
    })
  });
}

// Obtener recomendaciones
async function getRecommendations(userId) {
  const res = await fetch(
    `${VRIS_API_URL}/api/recommendations/books?user_id=${userId}`,
    {
      headers: { 'Authorization': `Bearer ${VRIS_API_KEY}` }
    }
  );
  return res.json();
}
```

---

## 📊 Roadmap

- [x] ✅ Fase 1: Fundación (FastAPI + DB)
- [ ] 🔄 Fase 2: Sistema de tracking
- [ ] 📋 Fase 3: Analytics básico
- [ ] 🤖 Fase 4: Machine Learning
- [ ] 💬 Fase 5: NLP con Hugging Face
- [ ] 🔗 Fase 6: Integración con Libro
- [ ] 🚀 Fase 7: Optimización y scaling

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto es parte de **VerixRichon Software Factory** - 100% Open Source.

Licencia MIT - ver [LICENSE](LICENSE) para detalles.

---

## 👨‍💻 Autores

**VerixRichon Factory**
- Website: [Coming Soon]
- GitHub: [@verixrichon](https://github.com/verixrichon)

---

## 🌟 Agradecimientos

- FastAPI por el increíble framework
- Hugging Face por modelos open source
- Scikit-learn por herramientas ML
- La comunidad open source

---

**Hecho con ❤️ y ☕ por VerixRichon Factory**
