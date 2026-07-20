import pandas as pd

def load_data(df, engine):
    print("Iniciando carga al Data Warehouse (Supabase)...")
    
    # 1. Preparar las Dimensiones (Extrayendo valores únicos)
    dim_time_df = df[['year', 'month']].drop_duplicates().copy()
    dim_supplier_df = df[['supplier_name']].drop_duplicates().copy()
    dim_item_df = df[['item_code', 'item_description', 'item_type']].drop_duplicates().copy()
    
    print(f"Nuevos registros a cargar -> Tiempo: {len(dim_time_df)}, Proveedores: {len(dim_supplier_df)}, Productos: {len(dim_item_df)}")
    
    # 2. Cargar Dimensiones a Supabase
    # if_exists='append' inserta sin borrar los datos existentes. 
    # Nota: Si se ejecuta dos veces generará duplicados si la BD no tiene constraints UNIQUE.
    dim_time_df.to_sql('dim_time', engine, if_exists='append', index=False)
    dim_supplier_df.to_sql('dim_supplier', engine, if_exists='append', index=False)
    dim_item_df.to_sql('dim_item', engine, if_exists='append', index=False)
    
    print("Dimensiones cargadas. Mapeando IDs para la tabla de hechos...")
    
    # 3. Traer los IDs autogenerados (SERIAL) desde Supabase
    db_time = pd.read_sql("SELECT time_id, year, month FROM dim_time", engine)
    db_supplier = pd.read_sql("SELECT supplier_id, supplier_name FROM dim_supplier", engine)
    db_item = pd.read_sql("SELECT item_id, item_code FROM dim_item", engine)
    
    # 4. Mapear (Join) los IDs autogenerados a nuestro DataFrame principal de Hechos
    fact_df = df.merge(db_time, on=['year', 'month'], how='left')
    fact_df = fact_df.merge(db_supplier, on='supplier_name', how='left')
    fact_df = fact_df.merge(db_item, on='item_code', how='left')
    
    # Nos quedamos sólo con las columnas que van a la Fact_Sales
    fact_sales = fact_df[['time_id', 'supplier_id', 'item_id', 'retail_sales', 'retail_transfers', 'warehouse_sales']]
    
    # Validar integridad: Eliminar nulos generados en el cruce (por precaución)
    fact_sales = fact_sales.dropna()
    
    print(f"Cargando Tabla de Hechos (Fact_Sales) con {len(fact_sales)} registros...")
    
    # 5. Cargar Fact_Sales masivamente (en lotes de 10,000 para optimizar rendimiento de red en Supabase)
    fact_sales.to_sql('fact_sales', engine, if_exists='append', index=False, chunksize=10000, method='multi')
    
    print("¡Carga exitosa completada en Supabase!")
