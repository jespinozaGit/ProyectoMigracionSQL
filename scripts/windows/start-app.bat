@echo off
cd /d "%~dp0src\app"
call ..\..\venv\Scripts\activate.bat
pip show flask >nul || pip install flask
pip show pyodbc >nul || pip install pyodbc
start "Servidor Flask" cmd /k "python app.py"
timeout /t 3 >nul
start "" http://127.0.0.1:5000/
exit