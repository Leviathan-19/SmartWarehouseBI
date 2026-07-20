import pandas as pd

def transform_data(df):
    print("Iniciando transformación de datos (Políticas COBIT APO11)...")
    
    # 1. Renombrar columnas para que coincidan con la BD y facilitar manipulación
    df.rename(columns={
        'YEAR': 'year',
        'MONTH': 'month',
        'SUPPLIER': 'supplier_name',
        'ITEM CODE': 'item_code',
        'ITEM DESCRIPTION': 'item_description',
        'ITEM TYPE': 'item_type',
        'RETAIL SALES': 'retail_sales',
        'RETAIL TRANSFERS': 'retail_transfers',
        'WAREHOUSE SALES': 'warehouse_sales'
    }, inplace=True)
    
    # 2. Control de Calidad: Aunque nos confirmaste que la data está limpia,
    # el ETL DEBE tener las reglas por si ingresa nueva data sucia en el futuro.
    df['supplier_name'] = df['supplier_name'].fillna('Desconocido')
    df['item_code'] = df['item_code'].fillna('Desc')
    df['item_description'] = df['item_description'].fillna('Desconocido')
    df['item_type'] = df['item_type'].fillna('Unknown')
    
    # Asegurar tipos de datos (Validez)
    for col in ['retail_sales', 'retail_transfers', 'warehouse_sales']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)
        
    for col in ['year', 'month']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(2000).astype(int)
        
    print(f"Transformación completada. Registros listos: {len(df)}")
    return df
