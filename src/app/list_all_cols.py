from sqlalchemy import create_engine, inspect

# Cadena de conexión igual a tu test_conn.py
DATABASE_URL = (
    "mssql+pyodbc://JC-PC\\SQLEXPRESS/FarmaciaSQL"
    "?trusted_connection=yes"
    "&driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

tablas = ["tInventario", "tVentas", "tCompras"]

for t in tablas:
    print(f"\nColumnas en {t}:")
    for col in inspector.get_columns(t):
        print("  -", col["name"])