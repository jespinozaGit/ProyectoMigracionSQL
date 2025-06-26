import os
import sys
import pandas as pd

# ----- importar util de log ----------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)
from utils.logger_util import registrar_evento
# -------------------------------------------------------------------

# Ruta al archivo
archivo = "data/copias_pc_farmacia/tu_archivo.xlsm"  # ajustá si es necesario

with pd.ExcelFile(archivo, engine="openpyxl") as xls:
    print("📑 Hojas disponibles:", xls.sheet_names)
    hoja = xls.sheet_names[0]          # o elegí otro índice
    print(f"\n🔍 Inspeccionando hoja: {hoja}")
    df = pd.read_excel(xls, sheet_name=hoja)

registrar_evento(f"Inspección de {archivo} | Hoja {hoja}")

# Recorte por EOF si existe
if "__FIN__" in df.columns:
    eof_index = df[df["__FIN__"] == "EOF"].index.min()
    if pd.notnull(eof_index):
        print(f"\n✂️ Recortando en índice EOF (fila {eof_index + 1})...")
        df = df.loc[:eof_index]
    df = df.drop(columns="__FIN__")
    registrar_evento(f"Recorte por __FIN__: quedan {len(df)} filas")

# Eliminar columnas basura
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Limpiar nombres raros
df.columns = (
    df.columns.astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.replace("\n", " ")
    .str.strip()
)

# Mostrar resumen
print(f"\n🧾 Columnas limpias ({len(df.columns)}):")
for col in df.columns:
    print(f"- {col!r}")

print(f"\n🔢 Filas después del recorte: {len(df)}")
print("\n📊 Tipos de columnas:")
print(df.dtypes)

print("\n🧪 Vista previa:")
print(df.head(10))

registrar_evento("Fin de inspección_excel.py")
