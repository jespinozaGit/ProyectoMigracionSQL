@echo off
setlocal EnableDelayedExpansion

:: --------------------------------------------------------
:: scaffold.bat – Crea y actualiza la estructura del proyecto
:: --------------------------------------------------------

:: Define aquí tus carpetas “canon”
set "folders=\
  docs \
  sql\migrations \
  notebooks \
  tests \
  logs \
  salidas \
  data \
  data\excel_originales \
  data\copias_pc_farmacia \
  data\staging \
  data\processed \
  src \
  src\app \
  src\config \
  src\utils \
  src\servicios \
  src\modulos
"

:: Archivos base
set "baseFiles=\
  README.md \
  requirements.txt
"

:: __init__.py
set "initFiles=\
  src\__init__.py \
  src\utils\__init__.py \
  src\servicios\__init__.py
"

:: Carpetas web (Flask)
set "webFolders=\
  src\app\templates \
  src\app\static
"

:: Archivo de log
set "logFile=logs\registro_sesiones.log"

echo.
echo --------------------------------------------------------
echo Escaneando / actualizando estructura de carpetas...
echo --------------------------------------------------------

for %%D in (%folders%) do (
  if not exist "%%D" (
    echo [+] Creando carpeta %%D
    mkdir "%%D"
  ) else (
    echo [=] Carpeta existe: %%D
  )
)

echo.
echo --------------------------------------------------------
echo Escaneando / creando archivos base...
echo --------------------------------------------------------

for %%F in (%baseFiles%) do (
  if not exist "%%F" (
    echo [+] Creando archivo %%F
    type nul > "%%F"
  ) else (
    echo [=] Archivo existe: %%F
  )
)

echo.
echo --------------------------------------------------------
echo Escaneando / creando archivos __init__.py...
echo --------------------------------------------------------

for %%I in (%initFiles%) do (
  if not exist "%%I" (
    echo [+] Creando archivo %%I
    type nul > "%%I"
  ) else (
    echo [=] %%I ya existe
  )
)

echo.
echo --------------------------------------------------------
echo Escaneando / creando carpetas web (Flask)...
echo --------------------------------------------------------

for %%W in (%webFolders%) do (
  if not exist "%%W" (
    echo [+] Creando carpeta web: %%W
    mkdir "%%W"
  ) else (
    echo [=] Carpeta web existe: %%W
  )
)

echo.
echo --------------------------------------------------------
echo Escaneando / creando archivo de log...
echo --------------------------------------------------------

if not exist "%logFile%" (
  echo [+] Creando %logFile%
  (
    echo Registro de sesiones - Proyecto MigracionSQL
    echo ---------------------------------------------
  ) > "%logFile%"
) else (
  echo [=] %logFile% ya existe
)

echo.
echo --------------------------------------------------------
echo Estructura actualizada correctamente.
echo --------------------------------------------------------

endlocal
exit /b 0
