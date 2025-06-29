@echo off
setlocal EnableDelayedExpansion

::------------------------------------------------------------
:: Proyecto: Migración SQL – Estructura de carpetas + init files
:: Última actualización: 2025-06-19 (corrige app.py)
::------------------------------------------------------------

set "PROJECT_ROOT=%USERPROFILE%\Desktop\ProyectoMigracionSQL"

echo ----------------------------------------------------------
echo Verificando / creando estructura en: %PROJECT_ROOT%
echo ----------------------------------------------------------
echo.

:: 1. Carpeta raíz
if not exist "%PROJECT_ROOT%" (
    echo [+] Creando carpeta raíz...
    mkdir "%PROJECT_ROOT%"
) else (
    echo [=] Carpeta raíz ya existe.
)
echo.

pushd "%PROJECT_ROOT%" || exit /b

:: 2. Subcarpetas del proyecto
set "folders=docs sql migrations notebooks tests logs salidas data data\excel_originales data\copias_pc_farmacia data\staging data\processed src src\app src\config src\utils src\servicios src\modulos"

for %%F in (%folders%) do (
    if not exist "%%F" (
        echo [+] Creando carpeta %%F...
        mkdir "%%F"
    ) else (
        echo [=] Carpeta %%F ya existe.
    )
)
echo.

:: 3. Archivos base del proyecto
for %%A in (README.md requirements.txt) do (
    if not exist "%%A" (
        echo [+] Creando %%A...
        type nul > "%%A"
    ) else (
        echo [=] %%A ya existe.
    )
)

:: 4. Archivo de log
set "LOG_FILE=logs\registro_sesiones.log"
if not exist "%LOG_FILE%" (
    echo [+] Creando archivo de log...
    (
        echo Registro de sesiones - Proyecto MigracionSQL
        echo ---------------------------------------------
    ) > "%LOG_FILE%"
) else (
    echo [=] %LOG_FILE% ya existe.
)

:: 5. Archivos __init__.py
set "initFiles=src\__init__.py src\utils\__init__.py src\servicios\__init__.py"

for %%I in (%initFiles%) do (
    if not exist "%%I" (
        echo [+] Creando %%I...
        type nul > "%%I"
    ) else (
        echo [=] %%I ya existe.
    )
)

:: 6. Carpetas para Flask (web)
set "webFolders=src\app\templates src\app\static"
for %%W in (%webFolders%) do (
    if not exist "%%W" (
        echo [+] Creando carpeta web: %%W...
        mkdir "%%W"
    ) else (
        echo [=] Carpeta web ya existe: %%W
    )
)

:: 7. Crear archivo app.py correctamente
set "APP_MAIN=src\app\app.py"
if not exist "%APP_MAIN%" (
    echo [+] Creando archivo src\app\app.py...

    call :write_app "%APP_MAIN%"
) else (
    echo [=] src\app\app.py ya existe.
)
goto :eof

:write_app
> %1 echo from flask import Flask
>> %1 echo.
>> %1 echo app = Flask(__name__)
>> %1 echo.
>> %1 echo @app.route("/") 
>> %1 echo def home():
>> %1 echo     return "Hola desde la app web Flask"
>> %1 echo.
>> %1 echo if __name__ == "__main__":
>> %1 echo     app.run(debug=True)
goto :eof

popd
echo.
echo ----------------------------------------------------------
echo Estructura verificada / creada correctamente.
echo ----------------------------------------------------------
pause
