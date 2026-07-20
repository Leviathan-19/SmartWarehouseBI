-- VISTAS PARA ALIMENTAR EL BALANCED SCORECARD EN POWER BI

-- 1. Perspectiva Financiera: Ingresos totales mensuales
CREATE OR REPLACE VIEW v_bsc_financial AS
SELECT 
    t.year, 
    t.month,
    SUM(f.retail_sales) AS total_retail_sales,
    SUM(f.warehouse_sales) AS total_warehouse_sales,
    SUM(f.retail_sales + f.warehouse_sales) AS total_revenue
FROM fact_sales f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.year, t.month
ORDER BY t.year DESC, t.month DESC;

-- 2. Perspectiva Clientes: Top Proveedores históricos
CREATE OR REPLACE VIEW v_bsc_customers_top_suppliers AS
SELECT 
    s.supplier_name,
    SUM(f.retail_sales + f.warehouse_sales) AS total_revenue
FROM fact_sales f
JOIN dim_supplier s ON f.supplier_id = s.supplier_id
GROUP BY s.supplier_name
ORDER BY total_revenue DESC;

-- 3. Perspectiva Procesos Internos: Eficiencia Logística (Transfers vs Sales)
CREATE OR REPLACE VIEW v_bsc_internal_processes AS
SELECT 
    t.year, 
    t.month,
    SUM(f.retail_transfers) AS total_inventory_transferred,
    CASE 
        WHEN SUM(f.retail_sales) = 0 THEN 0 
        ELSE SUM(f.retail_transfers) / SUM(f.retail_sales) 
    END AS transfer_to_sales_ratio
FROM fact_sales f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.year, t.month
ORDER BY t.year DESC, t.month DESC;

-- 4. Perspectiva Aprendizaje y Crecimiento: Crecimiento Mensual (MoM %)
CREATE OR REPLACE VIEW v_bsc_learning_growth AS
WITH monthly_revenue AS (
    SELECT 
        t.year, 
        t.month,
        SUM(f.retail_sales + f.warehouse_sales) AS total_revenue
    FROM fact_sales f
    JOIN dim_time t ON f.time_id = t.time_id
    GROUP BY t.year, t.month
)
SELECT 
    year, 
    month, 
    total_revenue,
    LAG(total_revenue, 1) OVER (ORDER BY year, month) AS previous_month_revenue,
    CASE 
        WHEN LAG(total_revenue, 1) OVER (ORDER BY year, month) = 0 THEN 0
        ELSE ((total_revenue - LAG(total_revenue, 1) OVER (ORDER BY year, month)) / LAG(total_revenue, 1) OVER (ORDER BY year, month)) * 100 
    END AS mom_growth_percentage
FROM monthly_revenue;
