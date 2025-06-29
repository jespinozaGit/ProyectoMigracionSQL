@echo off
setlocal EnableDelayedExpansion

echo.
echo --------------------------------------------------
echo 1) Creando / actualizando estructura de carpetas
echo --------------------------------------------------
call scaffold.bat

:: 2) Instalando librerías Python
if exist requirements.txt (
  echo.
  echo ---------------------------------------
  echo 2) Instalando dependencias Python...
  echo ---------------------------------------
  python -m pip install --upgrade pip
  pip install -r requirements.txt
)

:: 3) Instalando dependencias Node (docs)
echo.
echo ---------------------------------------
echo 3) Instalando dependencias de Docs...
echo ---------------------------------------
npm install

echo.
echo --------------------------------------------------
echo Bootstrap completo. Proyecto listo para usar.
echo --------------------------------------------------
endlocal
exit /b 0
