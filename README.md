# Data Warehouse & Business Intelligence (BI) - Retail & Warehouse Sales

Este repositorio contiene la arquitectura completa, el proceso ETL y la definición del modelo analítico para un **Data Warehouse** construido sobre **PostgreSQL (Supabase)**, con el objetivo de analizar un volumen de más de 300,000 registros de ventas Retail y Mayoristas.

El proyecto está diseñado bajo un modelo dimensional (Esquema Estrella) y documentado aplicando principios de calidad de datos COBIT APO11.

## Arquitectura del Proyecto

* **Origen de Datos:** Dataset CSV de Ventas (Retail y Warehouse).
* **Motor ETL:** Python (`pandas` y `SQLAlchemy`).
* **Data Warehouse:** PostgreSQL en la nube (Supabase).
* **Visualización:** Microsoft Power BI (o Metabase).

## Estructura del Repositorio

```text
📁 DataWarehouse-BI/
├── 📁 datasets/                   # Archivos fuente (CSV)
├── 📁 docs/
│   ├── 01_Data_Dictionary.md      # Diccionario de datos y modelo Estrella
│   └── 02_KPIs_and_BSC.md         # Documentación de KPIs y Balanced Scorecard
├── 📁 etl/
│   ├── db.py                      # Conexión a Supabase (vía .env)
│   ├── extract.py                 # Fase de extracción (Lectura de CSV)
│   ├── transform.py               # Transformación (Limpieza y tipos COBIT APO11)
│   ├── load.py                    # Carga al DWH (Cruce de llaves e inserción masiva)
│   └── main.py                    # Orquestador del pipeline ETL
├── 📁 sql/
│   ├── 01_create_tables.sql       # Creación del modelo físico en PostgreSQL
│   ├── 02_insert_sample_data.sql  # Datos dummy iniciales (opcional)
│   ├── 03_verify_queries.sql      # Consultas de verificación
│   ├── 04_kpis_views.sql          # Creación de vistas analíticas para Power BI
│   └── 05_reset_database.sql      # Script seguro de reinicio de datos (Truncate)
├── .env                           # Variables de entorno (ignorado en git)
├── .gitignore                     # Archivos ignorados por versionamiento
├── requirements.txt               # Dependencias (pandas, sqlalchemy, psycopg2, python-dotenv)
└── Roadmap_DataWarehouse_BI.md    # Hilo conductor y fases del proyecto
```

## Cómo ejecutar el ETL

1. Clona el repositorio e instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Configura tu archivo `.env` en la raíz del proyecto con la variable `DATABASE_URL` apuntando a tu base de datos Supabase.
3. Asegúrate de haber ejecutado los scripts de creación de tablas y vistas ubicados en `sql/01_create_tables.sql` y `sql/04_kpis_views.sql`.
4. Ejecuta el pipeline:
   ```bash
   python etl/main.py
   ```

## Dashboard y Vistas

El Data Warehouse no alimenta directamente a Power BI con tablas crudas. Hemos implementado un modelo de **Vistas Analíticas en Base de Datos** para que el servidor Postgres haga el procesamiento pesado, entregando métricas limpias para las 4 perspectivas del Balanced Scorecard:
* `v_bsc_financial`
* `v_bsc_internal_processes`
* `v_bsc_customers_top_suppliers`
* `v_bsc_learning_growth`

*(Para más detalle de cada KPI, revisa `docs/02_KPIs_and_BSC.md`)*
