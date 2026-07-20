-- Índices para optimizar el rendimiento (Escalabilidad a millones de registros)
-- y mejorar los tiempos de respuesta del Dashboard / BI

-- 1. Índices en la Tabla de Hechos (Especialmente en las Foreign Keys para los JOINs)
CREATE INDEX idx_fact_time_id ON fact_sales(time_id);
CREATE INDEX idx_fact_supplier_id ON fact_sales(supplier_id);
CREATE INDEX idx_fact_item_id ON fact_sales(item_id);

-- 2. Índices en las Dimensiones para búsquedas rápidas (Ej. al usar segmentadores en Power BI)
CREATE INDEX idx_dim_supplier_name ON dim_supplier(supplier_name);
CREATE INDEX idx_dim_item_code ON dim_item(item_code);
CREATE INDEX idx_dim_item_type ON dim_item(item_type);
CREATE INDEX idx_dim_time_year_month ON dim_time(year, month);
