-- 1. Dimensión de Tiempo (Dim_Time)
CREATE TABLE dim_time (
    time_id SERIAL PRIMARY KEY,
    year INT NOT NULL,
    month INT NOT NULL
);

-- 2. Dimensión de Proveedores (Dim_Supplier)
CREATE TABLE dim_supplier (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL
);

-- 3. Dimensión de Productos (Dim_Item)
CREATE TABLE dim_item (
    item_id SERIAL PRIMARY KEY,
    item_code VARCHAR(100) NOT NULL,
    item_description VARCHAR(500) NOT NULL,
    item_type VARCHAR(100) NOT NULL
);

-- 4. Tabla de Hechos de Ventas (Fact_Sales)
CREATE TABLE fact_sales (
    fact_id BIGSERIAL PRIMARY KEY,
    time_id INT NOT NULL,
    supplier_id INT NOT NULL,
    item_id INT NOT NULL,
    -- Tipo DECIMAL con separación por punto nativo de SQL. (15, 2) soporta números muy grandes con 2 decimales
    retail_sales DECIMAL(15, 2) NOT NULL,
    retail_transfers DECIMAL(15, 2) NOT NULL,
    warehouse_sales DECIMAL(15, 2) NOT NULL
);
