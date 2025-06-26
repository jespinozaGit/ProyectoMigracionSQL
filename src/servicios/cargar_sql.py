import os
import sys
import pandas as pd
from sqlalchemy import create_engine
import urllib

# ------------------------------------------------------------------
#  Logger
#  (Ubicado en: src/utils/logger_util.py; función: registrar_evento)
# ------------------------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)  # Agrega 'src' al sys.path
from utils.logger_util import registrar_evento
# ------------------------------------------------------------------

# 1. Configurar rutas
BASE_DIR    = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUTA_COPIAS = os.path.join(BASE_DIR, "data", "copias_pc_farmacia")

# Verificar la existencia de la carpeta de copias
if not os.path.exists(RUTA_COPIAS):
    print(f"❌ Carpeta no encontrada: {RUTA_COPIAS}")
    registrar_evento(f"ERROR – Carpeta faltante: {RUTA_COPIAS}")
    sys.exit()

# 2. Buscar un archivo .xlsm en la carpeta
archivos = [f for f in os.listdir(RUTA_COPIAS) if f.endswith(".xlsm")]
if not archivos:
    print("⚠️  No se encontraron archivos .xlsm.")
    registrar_evento("ADVERTENCIA – Sin .xlsm en copias_pc_farmacia")
    sys.exit()

archivo_excel = os.path.join(RUTA_COPIAS, archivos[0])
print(f"📄 Archivo seleccionado: {archivo_excel}")
registrar_evento(f"cargar_sql.py – Archivo: {archivo_excel}")

# 3. Cargar el libro Excel y la hoja "Metadatos"
with pd.ExcelFile(archivo_excel, engine="openpyxl") as xls:
    hojas = xls.sheet_names
    if "Metadatos" not in hojas:
        print("❌ No se encontró la hoja 'Metadatos' en el libro.")
        registrar_evento("ERROR – Hoja 'Metadatos' no encontrada")
        sys.exit()

    meta_df = pd.read_excel(xls, sheet_name="Metadatos", engine="openpyxl")
    registrar_evento(f"Se encontraron {len(meta_df)} registros en Metadatos")

    # 4. Por cada registro en Metadatos se extrae el rango y se crea la tabla en SQL
    for idx, meta in meta_df.iterrows():
        try:
            # Leer parámetros de Metadatos
            hoja        = str(meta["Hoja"]).strip()
            tabla       = str(meta["Tabla"]).strip()
            fila_enc    = int(meta["Fila encabezado"])
            primera_fi  = int(meta["Primera fila"])
            ultima_fi   = int(meta["Ultima fila"])
            primera_col = int(meta["Primera columna"])
            ultima_col  = int(meta["Ultima columna"])

            print(f"\nProcesando configuración #{idx+1}:")
            print(f"   Hoja: {hoja} | Tabla destino: {tabla}")
            print(f"   Rango: Encabezado en fila {fila_enc}, datos de la fila {primera_fi} a {ultima_fi}")
            print(f"   Columnas: de la {primera_col} a la {ultima_col}")

            registrar_evento(f"Metadato #{idx+1} – Hoja: {hoja}, Tabla: {tabla}")

            # Verificar que la hoja exista en el libro
            if hoja not in hojas:
                mensaje = f"❌ La hoja '{hoja}' no existe en el libro."
                print(mensaje)
                registrar_evento(mensaje)
                continue

            # Leer la hoja de datos sin encabezados para extraer el rango exacto
            df_completo = pd.read_excel(xls, sheet_name=hoja, header=None, engine="openpyxl")

            # Conversión de índices (Excel es 1-based; pandas es 0-based)
            header_idx     = fila_enc - 1
            first_data_idx = primera_fi - 1
            last_data_idx  = ultima_fi    # En iloc, el final es exclusivo. Como Excel es inclusivo, usamos 'ultima_fi' directamente.
            first_col_idx  = primera_col - 1
            last_col_idx   = ultima_col   # lst: en slicing este valor es exclusivo.

            # Extraer el encabezado y el rango de datos
            header = df_completo.iloc[header_idx, first_col_idx:last_col_idx].tolist()
            df_tabla = df_completo.iloc[first_data_idx:last_data_idx, first_col_idx:last_col_idx].copy()
            df_tabla.columns = header

            # Opcional: limpieza de encabezados (remover saltos de línea y espacios redundantes)
            df_tabla.columns = (
                pd.Series(df_tabla.columns)
                .astype(str)
                .str.replace(r"\s+", " ", regex=True)
                .str.replace("\n", " ")
                .str.strip()
                .tolist()
            )

            print(f"   Filas leídas: {df_tabla.shape[0]} | Columnas: {df_tabla.shape[1]}")
            registrar_evento(f"{tabla} – Datos extraídos: {df_tabla.shape[0]} filas x {df_tabla.shape[1]} columnas")

            # Corrección de tipos en función del nombre de la columna
            for col in df_tabla.columns:
                c = col.strip().lower()
                if "fecha" in c:
                    df_tabla[col] = pd.to_datetime(df_tabla[col], errors="coerce")
                elif any(k in c for k in ["precio", "costo", "total", "monto"]):
                    df_tabla[col] = pd.to_numeric(df_tabla[col], errors="coerce")
                elif any(k in c for k in ["cantidad", "existencia", "stock"]):
                    df_tabla[col] = pd.to_numeric(df_tabla[col], errors="coerce")
            registrar_evento(f"{tabla} – Tipos corregidos automáticamente")

            # Conexión a SQL utilizando SQLAlchemy
            param = urllib.parse.quote_plus(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=JC-PC\\SQLEXPRESS;"
                "DATABASE=FarmaciaSQL;"
                "Trusted_Connection=yes"
            )
            CADENA = f"mssql+pyodbc:///?odbc_connect={param}"
            engine = create_engine(CADENA)

            # Crear / reemplazar la tabla en SQL con el nombre indicado
            with engine.begin() as con:
                df_tabla.to_sql(tabla, con=con, if_exists="replace", index=False)

            print(f"   ✅ Tabla '{tabla}' cargada correctamente en SQL.")
            registrar_evento(f"Carga exitosa → tabla {tabla}")

        except Exception as ex:
            error_msg = f"❌ Error procesando registro {idx+1} en Metadatos: {ex}"
            print(error_msg)
            registrar_evento(error_msg)