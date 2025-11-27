@echo off
echo 🌌 INICIANDO CONEXION INTERGALACTICA VRIS...
echo =============================================

set GH_PATH="C:\Program Files\GitHub CLI\gh.exe"

echo.
echo [PASO 1] AUTENTICACION
echo Se abrira tu navegador. Por favor autoriza el acceso.
echo.
%GH_PATH% auth login -h github.com -p https -w

echo.
echo [PASO 2] CREANDO REPO Y SUBIENDO
echo.
call %GH_PATH% repo create vris --public --source=. --remote=origin
call git branch -M main
call git push -u origin main

echo.
echo =============================================
echo ✅ PROCESO FINALIZADO
echo =============================================
pause
