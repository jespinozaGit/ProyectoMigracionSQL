import pandas as pd

def recortar_con_marcadores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y recorta un DataFrame utilizando la columna '__FIN__' como marcador.

    Procedimiento:
      - Recorte horizontal: elimina columnas que estén a la derecha de la columna '__FIN__'.
      - Recorte vertical: filtra las filas conservando solo aquellas en las que el valor de '__FIN__' es True.
      - Se pueden agregar pasos adicionales de limpieza, como eliminar columnas no necesarias o renombrar columnas duplicadas.

    Parámetros:
      df (pd.DataFrame): DataFrame extraído del archivo Excel.

    Retorna:
      pd.DataFrame: DataFrame limpio y recortado según los marcadores.
    """
    # Verificar si la columna '__FIN__' existe en el DataFrame
    if '__FIN__' in df.columns:
        # Obtener el índice de la columna '__FIN__'
        indice_fin = df.columns.get_loc('__FIN__')
        
        # Recorte horizontal: conservar columnas desde inicio hasta '__FIN__' (inclusive)
        df = df.iloc[:, :indice_fin + 1]
        
        # Recorte vertical: filtrar filas donde la columna '__FIN__' tenga valor True
        df = df[df['__FIN__'] == True]
    else:
        # Si no se encuentra el marcador, se registra un aviso y se retorna el DataFrame completo.
        print("No se encontró la columna '__FIN__'. Procesando todo el DataFrame.")

    # Aquí podrías agregar pasos adicionales de limpieza, por ejemplo, eliminar columnas inútiles o renombrar duplicadas.
    return df

# Ejemplo de uso (este bloque se puede eliminar si el módulo se utiliza en otros scripts):
if __name__ == "__main__":
    # Crear un DataFrame de ejemplo
    data = {
        'Columna1': [1, 2, 3, 4],
        'Columna2': ["A", "B", "C", "D"],
        '__FIN__': [True, False, True, False],
        'Extra': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)
    print("DataFrame original:")
    print(df)
    
    df_limpio = recortar_con_marcadores(df)
    print("\nDataFrame después de aplicar recortar_con_marcadores:")
    print(df_limpio)
    