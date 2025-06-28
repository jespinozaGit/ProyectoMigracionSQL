# Guía para Desarrolladores

Esta guía describe en detalle la arquitectura, integración y aspectos técnicos del Sistema Integrado de Gestión y Visualización de Datos. Está destinada a los desarrolladores que mantendrán o extenderán el sistema.

---

## Índice

1. [Arquitectura del Sistema](#arquitectura-del-sistema)  
2. [Integración Excel-SQL](#integración-excel-sql)  
3. [Módulo Principal en Flask](#módulo-principal-en-flask)  
4. [Acceso Local al Sistema Web](#acceso-local-al-sistema-web)  
5. [Scripts Auxiliares](#scripts-auxiliares)  
6. [Buenas Prácticas y Siguientes Pasos](#buenas-prácticas-y-siguientes-pasos)  
7. [Extensiones Futuras](#extensiones-futuras)  
8. [Historial de Cambios](#historial-de-cambios)  
9. [🧭 Versión 0.3.0 (en preparación)](#-versión-030-en-preparación)

---

## Arquitectura del Sistema

El sistema se organiza en tres capas:

- **Capa de Presentación:**  
  Basada en Flask, gestiona la interfaz web y define las rutas de navegación (por ejemplo, la ruta raíz `/` renderiza `index.html`).

- **Capa de Negocio:**  
  Se encarga de la transformación y procesamiento de datos, como el módulo que convierte archivos Excel en instrucciones SQL.

- **Capa de Datos:**  
  Conecta con la base de datos relacional (SQLite, MySQL o PostgreSQL) para realizar operaciones CRUD mediante comandos SQL generados dinámicamente.

Esta distribución favorece el mantenimiento y la escalabilidad del sistema.

---

## Integración Excel-SQL

El proceso de integración funciona de la siguiente manera:

1. **Extracción de Metadatos:**  
   Se utiliza `pandas` para leer y extraer información de archivos Excel que definen la configuración de tablas y filtros.

2. **Procesamiento y Validación:**  
   Mediante el módulo `excel_processor.py`, se valida la estructura del Excel y se convierten los datos en instrucciones SQL.

3. **Actualización de la Base de Datos:**  
   Los comandos SQL generados se ejecutan para crear o modificar tablas y sincronizar los datos.

---

## Módulo Principal en Flask

El archivo `src/app/app.py` es el punto de entrada de la aplicación. Entre sus funciones destacan:

- **Definición de Rutas:**  
  La ruta raíz (`/`) carga la plantilla `index.html`. Se pueden añadir rutas adicionales para mostrar detalles, configuraciones o interacciones específicas.

- **Configuración del Ambiente:**  
  Flask se ejecuta en modo debug para facilitar la detección de errores durante el desarrollo.

---

## Acceso Local al Sistema Web

Para desarrollar y probar la aplicación de manera local, sigue estos pasos:

- **Con Flask:**  
  1. Activa el entorno virtual (consulta la sección de instalación en el README.md).  
  2. Desde la carpeta `src/app`, ejecuta:
     ```bash
     python app.py
     ```
  3. Abre [http://127.0.0.1:5000](http://127.0.0.1:5000) en tu navegador para ver la página de inicio.

- **Con HTML Estático:**  
  Simplemente abre el archivo `index.html` en tu navegador.

---

## Scripts Auxiliares

- **setup.bat:**  
  Automatiza la creación de la estructura de carpetas del proyecto.

- **excel_processor.py:**  
  Ubicado en la carpeta `scripts/`, este módulo gestiona la lectura, validación y transformación de archivos Excel en comandos SQL que se ejecutan en la base de datos.

- **update_docs.bat / update_docs.sh:**  
  Regeneran automáticamente el `CHANGELOG.md` y los índices de contenido (`TOC`) en los archivos Markdown.

---

## Buenas Prácticas y Siguientes Pasos

- **Documentación Continua:**  
  Comenta el código y mantén actualizada esta guía con cada cambio significativo.

- **Control de Versiones:**  
  Utiliza Git y sigue un flujo de trabajo basado en ramas y revisiones de código.

- **Pruebas Unitarias:**  
  Desarrolla y ejecuta pruebas en módulos críticos para detectar errores tempranamente.

- **Revisión de Código:**  
  Realiza revisiones periódicas con el equipo para asegurar altos estándares de calidad.

---

## Extensiones Futuras

- **Integración con APIs Externas:**  
  Para enriquecer los datos y ampliar la funcionalidad.

- **Seguridad y Autenticación:**  
  Implementar mecanismos robustos para controlar el acceso al sistema.

- **Monitoreo y Optimización:**  
  Incorporar herramientas para la monitorización del rendimiento.

- **Mejora en la Interfaz de Usuario:**  
  Desarrollar visualizaciones avanzadas e interactivas para mejorar la experiencia.

---

## Historial de Cambios

**2025-06-22**  
- Configuración inicial del entorno básico de Flask en `src/app/app.py`.  
- Creación de la carpeta `templates` y del archivo `index.html`.  
- Establecimiento de la estructura de carpetas y actualización de las instrucciones de instalación y ejecución en README.md.

---

## 🧭 Versión 0.3.0 (en preparación)

- [ ] Documentar endpoints REST del backend  
- [ ] Añadir validación de variables de entorno  
- [ ] Configurar `markdownlint` en CI  
- [ ] Escribir pruebas unitarias básicas  
- [ ] Definir esquema de despliegue (Heroku / Streamlit Cloud)
