## DEPLOYMENT.md

```markdown
# DEPLOYMENT.md

## 1. Streamlit Cloud (si aplica)
- URL de la app: https://proyectomigrationsql.streamlit.app
- Nombre del secreto: DATABASE_URL
- Formato de la cadena:  
  ```
  mssql+pyodbc://<USER>:<PASS>@<HOST>:<PORT>/<DB>?driver=ODBC+Driver+17+for+SQL+Server
  ```

## 2. Variables de entorno locales
- Fichero: .env
- Clave/Valor:  
  ```
  DATABASE_URL=mssql+pyodbc:///?odbc_connect=DRIVER%7BODBC+Driver+17+for+SQL+Server%7D%3BSERVER%3DJC-PC%5CSQLEXPRESS%3BDATABASE%3DFarmaciaSQL%3BTrusted_Connection%3Dyes
  ```

## 3. Túnel ngrok (si usas)
- Archivo de config: ~/.ngrok2/ngrok-config.yml  
- Comandos:  
  ```
  ngrok authtoken <TU_TOKEN>
  ngrok tcp 1433 --region us
  ```

## 4. Parámetros de conexión a SQL Server
- Servidor: JC-PC\SQLEXPRESS  
- Base de datos: FarmaciaSQL  
- Autenticación: Trusted_Connection=yes  

## 5. Pendientes/Tareas
- [ ] Actualizar secreto en Streamlit Cloud  
- [ ] Probar consultas “Misceláneos” en la web  
- [ ] Revisar firewall LAN  
- [ ] Configurar acceso público (Ngrok/DNS)  

## 6. Cómo arrancar mañana
1. git clone https://github.com/jespinozaGit/ProyectoMigracionSQL.git  
2. cd ProyectoMigracionSQL  
3. scripts\windows\bootstrap.bat  
4. scripts\windows\start-system.bat  
5. Abrir http://localhost:8000 o http://<IP_LAN>:8000  
```

---

## .env.example

```ini
DATABASE_URL=mssql+pyodbc://<USER>:<PASS>@<HOST>:<PORT>/<DB>?driver=ODBC+Driver+17+for+SQL+Server
```