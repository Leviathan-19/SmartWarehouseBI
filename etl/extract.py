import pandas as pd

def extract_data(file_path):
    print(f"Extrayendo datos desde: {file_path}")
    # Especificamos dtype explícitamente para 'ITEM CODE' para forzar que sea texto (string)
    # y evitar advertencias de tipos mixtos, lo cual soluciona el problema de pérdida de registros.
    df = pd.read_csv(file_path, dtype={'ITEM CODE': str})
    print(f"Extracción completada. Filas extraídas: {len(df)}")
    return df
