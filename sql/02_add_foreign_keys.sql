-- Agregar Claves Foráneas (Relaciones) a la Tabla de Hechos

ALTER TABLE fact_sales
ADD CONSTRAINT fk_sales_time
FOREIGN KEY (time_id)
REFERENCES dim_time(time_id)
ON DELETE RESTRICT;

ALTER TABLE fact_sales
ADD CONSTRAINT fk_sales_supplier
FOREIGN KEY (supplier_id)
REFERENCES dim_supplier(supplier_id)
ON DELETE RESTRICT;

ALTER TABLE fact_sales
ADD CONSTRAINT fk_sales_item
FOREIGN KEY (item_id)
REFERENCES dim_item(item_id)
ON DELETE RESTRICT;

-- Constraints adicionales (Reglas de Calidad / Validaciones)
-- El Mes siempre debe estar entre 1 y 12
ALTER TABLE dim_time
ADD CONSTRAINT chk_month_validity
CHECK (month BETWEEN 1 AND 12);
