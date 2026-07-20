import os
import sys

# Asegurar que Python reconozca la carpeta actual para los imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.db import engine

def main():
    print("========================================")
    print(" INICIANDO PROCESO ETL - DATA WAREHOUSE")
    print("========================================")
    
    # Ruta al dataset
    dataset_path = os.path.join("datasets", "Warehouse_and_Retail_Sales.csv")
    
    # 1. Extracción
    raw_data = extract_data(dataset_path)
    
    # 2. Transformación
    clean_data = transform_data(raw_data)
    
    # 3. Carga
    load_data(clean_data, engine)
    
    print("========================================")
    print(" PROCESO ETL FINALIZADO CON ÉXITO")
    print("========================================")

if __name__ == "__main__":
    main()
