@echo off
setlocal EnableDelayedExpansion
ECHO est  desactivado.
echo --------------------------------------------------
echo 1) Preparando estructura y dependencias
echo --------------------------------------------------
call ..\..\setup.bat
ECHO est  desactivado.
echo --------------------------------------------------
echo 2) Instalando dependencias Python...
echo --------------------------------------------------
python -m pip install --upgrade pip
pip install -r requirements.txt
ECHO est  desactivado.
echo --------------------------------------------------
echo 3) Instalando dependencias de DOCS (npm)...
echo --------------------------------------------------
if exist package.json (npm install)
ECHO est  desactivado.
echo ðŸš€ Bootstrap completo. Proyecto listo para usar.
endlocal
exit /b 0
