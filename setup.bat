@echo off
setlocal EnableDelayedExpansion

::------------------------------------------------------------
:: Proyecto: Migración SQL – Setup completo en una nueva PC
:: Versión final – 2025-06-29
::------------------------------------------------------------

set "PROJECT_ROOT=%~dp0"
echo ----------------------------------------------------------
echo 🛠️  Instalando estructura en: %PROJECT_ROOT%
echo ----------------------------------------------------------

:: 1. Carpetas base
set "folders=docs sql migrations notebooks tests logs salidas data data\excel_originales data\copias_pc_farmacia data\staging data\processed src src\app src\config src\utils src\servicios src\modulos src\app\templates src\app\static"

for %%F in (%folders%) do (
    if not exist "%%F" (
        echo [+] Carpeta creada: %%F
        mkdir "%%F"
    ) else (
        echo [=] Ya existe: %%F
    )
)

:: 2. Archivos base
for %%A in (README.md requirements.txt docker-compose.yml) do (
    if not exist "%%A" (
        echo [+] Archivo creado: %%A
        type nul > "%%A"
    ) else (
        echo [=] Ya existe: %%A
    )
)

:: 3. __init__.py en paquetes
set "initFiles=src\__init__.py src\utils\__init__.py src\servicios\__init__.py"
for %%I in (%initFiles%) do (
    if not exist "%%I" (
        echo [+] Init Python: %%I
        type nul > "%%I"
    )
)

:: 4. app.py básico en Flask
set "APP_FILE=src\app\app.py"
if not exist "!APP_FILE!" (
    echo [+] Creando app Flask base...
    call :write_app "!APP_FILE!"
)

:: 5. Dockerfile básico
if not exist "Dockerfile" (
    echo [+] Creando Dockerfile...
    call :write_docker "Dockerfile"
)

:: 6. docker-compose.yml
if not exist "docker-compose.yml" (
    echo [+] Generando docker-compose.yml...
    call :write_compose "docker-compose.yml"
)

:: 7. Log inicial
set "LOG_FILE=logs\registro_sesiones.log"
if not exist "!LOG_FILE!" (
    echo [+] Creando registro de sesiones...
    (
        echo Registro de sesiones - Proyecto MigracionSQL
        echo ---------------------------------------------
        echo Creado: %DATE% %TIME%
    ) > "!LOG_FILE!"
)

:: 8. Inicializar repo Git
if not exist ".git" (
    echo [+] Inicializando Git...
    git init
    git add .
    git commit -m "Setup inicial creado automáticamente"
)

echo.
echo ✅ Estructura generada con éxito en: %PROJECT_ROOT%
echo 🔁 Puedes correr: docker compose up --build
echo ----------------------------------------------------------
pause
exit /b

:write_app
> %1 echo from flask import Flask
>> %1 echo
>> %1 echo app = Flask(__name__)
>> %1 echo
>> %1 echo @app.route("/")
>> %1 echo def home():
>> %1 echo     return "Hola desde la app web Flask"
>> %1 echo
>> %1 echo if __name__ == "__main__":
>> %1 echo     app.run(debug=True)
goto :eof

:write_docker
> %1 echo FROM python:3.11-slim
>> %1 echo WORKDIR /app
>> %1 echo COPY requirements.txt ./
>> %1 echo RUN apt-get update && apt-get install -y unixodbc
>> %1 echo RUN pip install --no-cache-dir -r requirements.txt
>> %1 echo COPY ./src/app ./src/app
>> %1 echo CMD ["python", "./src/app/app.py"]
goto :eof

:write_compose
> %1 echo version: "3.8"
>> %1 echo services:
>> %1 echo   web:
>> %1 echo     build: .
>> %1 echo     ports:
>> %1 echo       - "8000:5000"
>> %1 echo     volumes:
>> %1 echo       - ./src:/app/src
>> %1 echo     depends_on:
>> %1 echo       - db
>> %1 echo   db:
>> %1 echo     image: postgres:15
>> %1 echo     ports:
>> %1 echo       - "5432:5432"
>> %1 echo     environment:
>> %1 echo       - POSTGRES_USER=admin
>> %1 echo       - POSTGRES_PASSWORD=admin
>> %1 echo       - POSTGRES_DB=mi_basededatos
goto :eof
