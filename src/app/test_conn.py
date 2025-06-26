from sqlalchemy import create_engine, text

# Cadena apuntando a tu instancia y base FarmaciaSQL usando Windows Auth
DATABASE_URL = (
    "mssql+pyodbc://JC-PC\\SQLEXPRESS/FarmaciaSQL"
    "?trusted_connection=yes"
    "&driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    result = conn.execute(text("SELECT TOP 1 * FROM tInventario"))
    print("✅ Conexión OK. Fila de prueba:\n", result.fetchall())