from flask import Flask, render_template, request
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError
import urllib

app = Flask(__name__)

# Configurar la conexión a SQL Server
param = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=JC-PC\\SQLEXPRESS;"
    "DATABASE=FarmaciaSQL;"
    "Trusted_Connection=yes"
)
DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={param}"
engine = create_engine(DATABASE_URL)

@app.route("/")
def index():
    menu = {
        "Ventas": "/ventas",
        "Compras": "/compras",
        "Misceláneos": "/miscelaneos"
    }
    return render_template("index.html", menu=menu)

@app.route("/miscelaneos")
def miscelaneos():
    return render_template("miscelaneos.html")

# Consulta avanzada de tCompras por Nombre del Medicamento y Laboratorio
@app.route("/miscelaneos/consultar_tcompras", methods=["GET", "POST"])
def consultar_tcompras():
    results = []
    nombre_medicamento = ""
    laboratorio = ""
    error = None

    if request.method == "POST":
        nombre_medicamento = request.form.get("nombre_medicamento", "").strip()
        laboratorio = request.form.get("laboratorio", "").strip()

        nombre_medicamento = nombre_medicamento.replace('*', '%').replace('?', '_')
        laboratorio = laboratorio.replace('*', '%').replace('?', '_')

        query = "SELECT TOP 100 * FROM tCompras WHERE 1=1"
        params = {}
        if nombre_medicamento:
            query += " AND [Nombre del medicamento] LIKE :nombre_medicamento"
            params["nombre_medicamento"] = f"%{nombre_medicamento}%"
        if laboratorio:
            query += " AND [Laboratorio] LIKE :laboratorio"
            params["laboratorio"] = f"%{laboratorio}%"

        try:
            with engine.connect() as conn:
                result_proxy = conn.execute(text(query), params)
                results = [dict(row) for row in result_proxy.mappings()]
        except SQLAlchemyError as e:
            error = str(e)

    return render_template("consultar_tCompras.html",
                           results=results,
                           nombre_medicamento=nombre_medicamento,
                           laboratorio=laboratorio,
                           error=error)

# Consulta de medicamentos por vencer en los próximos 60 días
@app.route("/miscelaneos/por_vencer")
def por_vencer():
    results = []
    error = None
    try:
        query = """
            SELECT TOP 100 *
            FROM tCompras
            WHERE [Fecha vence] BETWEEN CAST(GETDATE() AS DATE) AND DATEADD(DAY, 60, CAST(GETDATE() AS DATE))
            ORDER BY [Fecha vence]
        """
        with engine.connect() as conn:
            result_proxy = conn.execute(text(query))
            results = [dict(row) for row in result_proxy.mappings()]
    except SQLAlchemyError as e:
        error = str(e)
    return render_template("por_vencer.html", results=results, error=error)

# Consulta genérica por tabla y filtros (opcional)
@app.route("/miscelaneos/tablas", methods=["GET"])
def tablas():
    table_name = request.args.get("table")
    column_name = request.args.get("column")
    filter_value = request.args.get("filter_value")

    results = []
    columns = []
    error = None
    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    if table_name:
        if table_name.startswith("dbo."):
            table_name = table_name[4:]
        try:
            columns_info = inspector.get_columns(table_name)
            columns = [col["name"] for col in columns_info]
            if column_name and filter_value:
                query = f"SELECT TOP 100 * FROM {table_name} WHERE {column_name} LIKE :filter"
            else:
                query = f"SELECT TOP 100 * FROM {table_name}"
            with engine.connect() as conn:
                params = {"filter": f"%{filter_value}%"} if column_name and filter_value else {}
                result_proxy = conn.execute(text(query), params)
                results = [dict(row) for row in result_proxy.mappings()]
        except SQLAlchemyError as e:
            error = str(e)

    return render_template("tablas.html",
                           table_names=table_names,
                           selected_table=table_name,
                           columns=columns,
                           results=results,
                           selected_column=column_name,
                           filter_value=filter_value,
                           error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")