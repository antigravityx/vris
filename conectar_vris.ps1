Write-Host "🌌 INICIANDO CONEXIÓN VRIS..." -ForegroundColor Cyan

# 1. Verificar GitHub CLI
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "❌ GitHub CLI no encontrado." -ForegroundColor Red
    exit
}

# 2. Autenticación
Write-Host "🔐 PASO 1: LOGIN" -ForegroundColor Yellow
Write-Host "Se abrirá el navegador. Autoriza el acceso."
gh auth login -h github.com -p https -w

# 3. Crear Repo (Ignorar error si ya existe)
Write-Host "📦 PASO 2: CREANDO REPO" -ForegroundColor Yellow
try {
    gh repo create vris --public --source=. --remote=origin
} catch {
    Write-Host "Nota: El repo ya podría existir, continuando..."
}

# 4. Subir
Write-Host "🚀 PASO 3: SUBIENDO" -ForegroundColor Yellow
git branch -M main
git push -u origin main

Write-Host "✅ PROCESO FINALIZADO." -ForegroundColor Green
Write-Host "Si ves errores rojos arriba, avísame."
Read-Host "Presiona Enter para salir"
