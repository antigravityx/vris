#!/bin/bash
# 🚀 Script de Deploy Rápido - VRIS
# Ejecutar desde: c:\Users\Public\antigravity\vris

echo "🚀 VRIS - Deploy a GitHub"
echo "=========================="
echo ""

# 1. Verificar que estamos en el directorio correcto
if [ ! -f "app/main.py" ]; then
    echo "❌ Error: No estás en el directorio VRIS"
    echo "   Ejecuta: cd c:\Users\Public\antigravity\vris"
    exit 1
fi

echo "✅ Directorio correcto"
echo ""

# 2. Verificar Git status
echo "📋 Estado actual de Git:"
git status --short
echo ""

# 3. Mostrar instrucciones
echo "📝 PASOS A SEGUIR:"
echo ""
echo "1️⃣  Crear repo en GitHub:"
echo "   👉 https://github.com/new"
echo "   - Nombre: vris"
echo "   - Público"
echo "   - Sin README/gitignore/license"
echo ""

echo "2️⃣  Configurar remote (CAMBIA 'TU-USUARIO'):"
echo ""
echo "   git remote add origin https://github.com/TU-USUARIO/vris.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""

echo "3️⃣  Desplegar en Railway:"
echo "   👉 https://railway.app"
echo "   - Login with GitHub"
echo "   - New Project > Deploy from GitHub repo"
echo "   - Selecciona: vris"
echo "   - Add PostgreSQL"
echo "   - Configura variables (ver RAILWAY_VISUAL_GUIDE.md)"
echo ""

echo "✨ ¡Listo para flotar! 🚀"
