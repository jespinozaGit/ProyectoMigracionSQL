import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# —– CONFIGURACIÓN DE PÁGINA —–
st.set_page_config(
    page_title="Consultas de Farmacia",
    layout="wide",
)

# —– CADENA DE CONEXIÓN —–
DATABASE_URL = (
    "mssql+pyodbc://JC-PC\\SQLEXPRESS/FarmaciaSQL"
    "?trusted_connection=yes"
    "&driver=ODBC+Driver+17+for+SQL+Server"
)

@st.cache_resource
def get_engine():
    return create_engine(DATABASE_URL, fast_executemany=True)

@st.cache_data(ttl=300)
def run_query(sql: str, params: dict = None) -> pd.DataFrame:
    engine = get_engine()
    return pd.read_sql(text(sql), engine, params=params)

def display_df(df: pd.DataFrame):
    """Renderiza el DataFrame como HTML sin índice, ancho, y con formato numérico."""
    # Definimos formateadores para los campos de precio y costo
    fmt = {
        "Costo":           "{:,.2f}".format,
        "PrecioVenta":     "{:,.2f}".format,
        "PrecioCompra":    "{:,.2f}".format
    }
    html = df.to_html(
        index=False,
        classes="table table-striped",
        formatters=fmt,
        justify="left",
        border=0
    )
    st.markdown(html, unsafe_allow_html=True)

st.title("Consultas de Farmacia")

op = st.sidebar.selectbox("Elige consulta", [
    "Stock por producto",
    "Precio de compra/venta",
    "Ventas por fecha",
    "Compras por proveedor"
])

if op == "Stock por producto":
    prod = st.text_input("Término de búsqueda")
    modo = st.selectbox("Modo de búsqueda", [
        "Contiene",     # %texto%
        "Empieza con",  # texto%
        "Termina con",  # %texto
        "Exacto"        # texto
    ])
    if st.button("Ejecutar"):
        patrones = {
            "Contiene":    f"%{prod}%",
            "Empieza con": f"{prod}%",
            "Termina con": f"%{prod}",
            "Exacto":      prod
        }
        pat = patrones[modo]
        df = run_query(
            """
            SELECT
              Cod             AS Codigo,
              Nombre          AS Descripción,
              Laboratorio     AS Laboratorio,
              [Presentación]  AS Presentación,
              Costo           AS Costo,
              [Cant Exist]    AS Stock,
              Precio          AS PrecioVenta
            FROM tInventario
            WHERE Nombre LIKE :p OR Cod = :cod
            """,
            {"p": pat, "cod": prod}
        )
        display_df(df)

elif op == "Precio de compra/venta":
    if st.button("Cargar precios"):
        df = run_query(
            """
            SELECT
              Cod               AS Codigo,
              Nombre            AS Descripción,
              Costo             AS PrecioCompra,
              Precio            AS PrecioVenta
            FROM tInventario
            """
        )
        display_df(df)

elif op == "Ventas por fecha":
    f1 = st.date_input("Desde", pd.to_datetime("today").normalize())
    f2 = st.date_input("Hasta", pd.to_datetime("today").normalize())
    if st.button("Ver ventas"):
        df = run_query(
            """
            SELECT
              Fecha,
              Cod        AS Codigo,
              Cantidad,
              Subtotal   AS Total
            FROM tVentas
            WHERE Fecha BETWEEN :f1 AND :f2
            """,
            {"f1": f1, "f2": f2}
        )
        display_df(df)

elif op == "Compras por proveedor":
    prov = st.text_input("Proveedor")
    if st.button("Mostrar compras"):
        df = run_query(
            """
            SELECT
              [Fecha compra] AS Fecha,
              Factura       AS FacturaID,
              Proveedor,
              Total
            FROM tCompras
            WHERE Proveedor = :prov
            """,
            {"prov": prov}
        )
        display_df(df)