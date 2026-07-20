import pandas as pd

def extract_data(file_path):
    print(f"Extrayendo datos desde: {file_path}")
    df = pd.read_csv(file_path)
    print(f"Extracción completada. Filas extraídas: {len(df)}")
    return df
