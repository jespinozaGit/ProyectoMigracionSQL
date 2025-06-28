```markdown
# Guía de Instalación

Este documento describe todo lo necesario para poner en marcha la aplicación **Flask + Streamlit + SQL Server** en Windows, desde la instalación de software hasta la configuración final.

---

## 1. Prerrequisitos del Sistema

- Windows 10 o superior (64-bit)  
- Conexión a Internet  
- Permisos de Administrador (para algunas instalaciones)  

---

## 2. Instalación de Node.js (para herramientas de documentación)

1. Descarga el instalador LTS desde  
   https://nodejs.org/es/download/  
2. Ejecuta el archivo `.msi`:  
   - Acepta los términos de licencia.  
   - Marca **“Add to PATH”** (viene marcado por defecto).  
   - Haz clic en **Install** y espera a que termine.  
3. Cierra y abre **una nueva** ventana de PowerShell.  
4. Verifica la instalación:
   ```powershell
   node -v    # → v22.17.0
   npm -v     # → 10.9.2
   ```

---

## 3. Instalación de Python 3.8+

1. Descarga el instalador desde  
   https://www.python.org/downloads/windows/  
2. Ejecuta el archivo `.exe`:  
   - Marca **“Add Python to PATH”**.  
   - Acepta los términos y finaliza la instalación.  
3. Cierra y abre **una nueva** ventana de PowerShell.  
4. Verifica Python y pip:
   ```powershell
   python --version  
   # → Python 3.13.5

   # Instala o actualiza pip:
   python -m ensurepip --upgrade
   python -m pip install --upgrade pip

   # Comprueba pip:
   python -m pip --version  
   # → pip 25.1.1 from … (python 3.13)
   ```

---

## 4. Instalación de Visual C++ Build Tools

Necesario para compilar extensiones nativas de Python (por ejemplo `pyodbc`).

```powershell
choco install visualstudio2019-workload-vctools -y
```

> Al finalizar, si el instalador lo solicita, **reinicia** tu máquina.

---

## 5. ODBC Driver 17 for SQL Server

1. Descarga el driver desde  
   https://docs.microsoft.com/sql/connect/odbc/windows/microsoft-odbc-driver-17  
2. Ejecuta el instalador y sigue los pasos.  
3. Verifica en **Panel de control → Orígenes de datos ODBC** que el driver aparezca.

---

## 6. SQL Server Express

1. Descarga “SQL Server Express” desde  
   https://www.microsoft.com/sql-server/  
2. Instálalo:  
   - Elige **Autenticación Windows**.  
   - Anota el nombre de la instancia (p.ej. `SQLEXPRESS`).  
3. (Opcional) Para acceso remoto, habilita el puerto TCP 1433 y crea un login con contraseña.

---

## 7. Git y GitHub CLI

1. Instala Git desde  
   https://git-scm.com/downloads  
2. Configura tu identidad:
   ```bash
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu@correo.com"
   ```
3. (Opcional) Instala GitHub CLI:
   ```powershell
   choco install gh -y
   ```

---

## 8. Ngrok (para exponer tu app localmente)

1. Descarga el ZIP desde  
   https://ngrok.com/download  
2. Descomprime `ngrok.exe` en `C:\Tools\ngrok` (o la carpeta que prefieras).  
3. Añade esa carpeta al **PATH** de usuario:  
   - Panel de control → Sistema → Configuración avanzada → Variables de entorno → Path (Usuario) → Editar → Nuevo → `C:\Tools\ngrok`  
4. Abre PowerShell y registra tu token (una sola vez):
   ```powershell
   ngrok authtoken TU_TOKEN_DE_NGROK
   ```

---

## 9. Dependencias Python

Desde la raíz del proyecto, instala todos los paquetes:
```bash
pip install -r requirements.txt
```

---

## 10. Instalación de herramientas de documentación

Para automatizar tu **CHANGELOG** y los índices TOC:

```powershell
npm install -g conventional-changelog-cli markdown-toc
```

Verifica:
```powershell
conventional-changelog --version   # p.ej. 4.x.x
markdown-toc --version              # p.ej. 2.x.x
```

---

## 11. Clonar el Repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
```

---

## 12. Validación Final

1. **Flask**  
   ```bash
   python app.py
   ```  
   → Abre: http://127.0.0.1:5000/

2. **Streamlit**  
   ```bash
   streamlit run consultas.py
   ```  
   → Abre: http://localhost:8501/

3. **Ngrok** (en otra terminal):
   ```bash
   ngrok http 5000   # para Flask
   ngrok http 8501   # para Streamlit
   ```  
   → Copia la URL HTTPS que Ngrok genera y pruébala desde otro dispositivo.

---

## 13. Siguientes Pasos

- Despliegue en la nube: Azure App Service, Render, Railway…  
- Dominio & SSL: Let's Encrypt, Cloudflare.  
- Autenticación: Azure AD, Auth0 o JWT con Flask-Login.  
- Dockerización: Contenedor + Kubernetes o AKS.  
- CI/CD: GitHub Actions para tests, linting y despliegue automático.

---

> _Este documento (`docs/setup.md`) se actualizará tras cada sesión de trabajo. Antes de cerrar, añade nuevas entradas al `CHANGELOG.md` y verifica que todos los pasos estén completos._  
```
