@echo off
REM — 1) Sitúate en la raíz del proyecto
cd /d "%~dp0"

REM — 2) Activa el entorno virtual
call venv\Scripts\activate.bat

REM — 3) Menú de opciones
echo ================================
echo   PROYECTO Migracion SQL
echo ================================
echo 1) Levantar servidor Flask
echo 2) Iniciar módulo de consultas
echo 3) Salir
echo.
set /p opcion="Elige una opción [1-3]: "

if "%opcion%"=="1" goto FLASK
if "%opcion%"=="2" goto CONS
goto FIN

:FLASK
echo Arrancando servidor Flask...
cd src\app
start "Servidor Flask" cmd /k "python app.py"
goto FIN

:CONS
echo Abriendo módulo de consultas...
cd src\app
start "" cmd /k "streamlit run consultas.py"
goto FIN

:FIN
echo.
echo Pulsa una tecla para cerrar...
pause >nul
exit