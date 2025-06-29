# Sistema Integrado de Gestión y Visualización de Datos

Este repositorio, **ProyectoMigracionSQL**, alberga un microservicio Flask contenedorizado con PostgreSQL y scripts auxiliares para facilitar el desarrollo, la documentación y el despliegue.

---

## 📁 Estructura del Proyecto

Al ejecutar `setup.bat`, se crea la siguiente estructura:

```plaintext
.
├── setup.bat
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── docs/
│   └── guia_desarrollo.md
├── sql/
│   └── migrations/
├── notebooks/
├── tests/
├── logs/
├── salidas/
├── data/
│   ├── excel_originales/
│   ├── copias_pc_farmacia/
│   ├── staging/
│   └── processed/
├── scripts/
│   ├── archivados/
│   │   ├── crear_estructura.bat
│   │   └── scaffold.bat
│   └── windows/
│       ├── bootstrap.bat
│       ├── start-app.bat
│       ├── start-system.bat
│       └── update_docs.bat
└── src/
    ├── app/
    │   ├── app.py
    │   ├── templates/
    │   │   └── index.html
    │   └── static/
    ├── config/
    ├── utils/
    └── servicios/
```

---

## ⚙️ Prerrequisitos

- Windows 10 o superior  
- [Git](https://git-scm.com/)  
- [Docker Desktop](https://www.docker.com/products/docker-desktop)  
- [Node.js](https://nodejs.org/) (opcional, para generación de docs)  
- **Python 3.9+**  
  1. Crear entorno virtual:  
     ```bat
     python -m venv venv
     ```
  2. Activar en CMD:  
     ```bat
     venv\Scripts\activate
     ```

---

## 🚀 Instalación Inicial

1. Clona el repositorio y entra en la carpeta:  
   ```bash
   git clone https://github.com/jespinozaGit/ProyectoMigracionSQL.git
   cd ProyectoMigracionSQL
   ```
2. Activa el entorno virtual:  
   ```bat
   venv\Scripts\activate
   ```
3. Ejecuta el setup:  
   ```bat
   setup.bat
   ```
   Esto creará carpetas, archivos base, `Dockerfile`, `docker-compose.yml` y un commit inicial.

---

## 🛠️ Uso de los Scripts Windows

Todos los `.bat` activos están en `scripts/windows/`:

| Script               | Descripción                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| **bootstrap.bat**    | Llama a `setup.bat` e instala dependencias de Python (`pip`) y Node.js (`npm`).                                       |
| **start-app.bat**    | Activa el `venv`, garantiza Flask y pyodbc, arranca la app Flask en modo debug y abre automáticamente el navegador.   |
| **start-system.bat** | Detiene contenedores previos y levanta el stack completo (Flask + Postgres) con `docker compose up --build`.         |
| **update_docs.bat**  | Genera/actualiza `CHANGELOG.md` desde commits y reconstruye el índice (TOC) de `README.md` y `docs/guia_desarrollo.md`. |

### Ejemplo de flujo

```bat
cd scripts\windows
bootstrap.bat
start-app.bat
start-system.bat
update_docs.bat
```

---

## 📜 Documentación

- **README.md** (este archivo): instalación, estructura y uso rápido.  
- **docs/guia_desarrollo.md**: guía técnica para desarrolladores.  
- **CHANGELOG.md** (opcional): historial de cambios cronológico.

---

## 🗂️ Archivos Archivados

En `scripts/archivados/` quedan dos versiones históricas:

- `crear_estructura.bat`  
- `scaffold.bat`  

Ya no forman parte del flujo activo.

---

## 📑 Historial de Cambios

- **2025-06-22**  
  - Estructura básica, primer `app.py` e `index.html`.  
  - `setup.bat` versión inicial.  

- **2025-06-29**  
  - Consolidación de scripts en `scripts/windows`.  
  - Documentación separada en `docs/guia_desarrollo.md`.  

---

## 🎯 Próximos Pasos

1. Integrar pruebas unitarias y de integración.  
2. Configurar pipeline CI/CD (GitHub Actions, Azure Pipelines…).  
3. Desplegar en un entorno cloud (Azure, AWS, Heroku…).  
4. Extender interfaz, añadir autenticación y monitoreo.

---

**¡Listo!** Cualquier colaborador puede clonar, preparar el entorno y empezar a desarrollar o desplegar en minutos. 🚀  

---

### Guardar en UTF-8

1. Abre este archivo en el Bloc de notas.  
2. Ve a **Archivo → Guardar como…**.  
3. Selecciona **UTF-8** en “Codificación” y haz clic en **Guardar**.
