# Diseño del Modelo de Datos y Diccionario (Fase 2)

## 1. Diseño del Esquema Estrella

Basado en el dataset de ventas de retail y almacén (Warehouse and Retail Sales), el proceso de negocio central es la **Transacción de Movimiento de Inventario y Ventas**.

**Modelo Dimensional (Esquema Estrella):**

- **Tabla de Hechos (Fact Table):** `Fact_Sales`
  Almacena las métricas cuantitativas de ventas y transferencias a nivel mensual por producto y proveedor.
- **Dimensiones (Dimensions):**
  - `Dim_Time`: Dimensión de tiempo (Año y Mes).
  - `Dim_Supplier`: Dimensión de proveedores.
  - `Dim_Item`: Dimensión de productos.

---

## 2. Definición de Entidades y Atributos (Diccionario de Datos)

### Dimensión: `Dim_Time`
Permite analizar la estacionalidad y tendencias en el tiempo.
- `Time_ID` (PK, Integer, Auto-incremental): Identificador único de tiempo (Surrogate Key).
- `Year` (Integer): Año de la transacción.
- `Month` (Integer): Mes de la transacción (1-12).

### Dimensión: `Dim_Supplier`
Almacena los datos de los proveedores. Actúa como **Dato Maestro**.
- `Supplier_ID` (PK, Integer, Auto-incremental): Identificador único del proveedor (Surrogate Key).
- `Supplier_Name` (Varchar): Nombre del proveedor del producto.

### Dimensión: `Dim_Item`
Almacena la información de los productos. Actúa como **Dato Maestro**.
- `Item_ID` (PK, Integer, Auto-incremental): Identificador único del producto (Surrogate Key).
- `Item_Code` (Varchar): Código original del producto del sistema fuente.
- `Item_Description` (Varchar): Descripción completa del producto.
- `Item_Type` (Varchar): Tipo o categoría del producto.

### Tabla de Hechos: `Fact_Sales`
Contiene las métricas del negocio. Nivel de granularidad: Mensual por proveedor y producto.
- `Fact_ID` (PK, BigInt, Auto-incremental): Identificador de la transacción.
- `Time_ID` (FK, Integer): Referencia a `Dim_Time`.
- `Supplier_ID` (FK, Integer): Referencia a `Dim_Supplier`.
- `Item_ID` (FK, Integer): Referencia a `Dim_Item`.
- `Retail_Sales` (Numeric/Decimal): Ventas en tiendas (unidades o valor).
- `Retail_Transfers` (Numeric/Decimal): Transferencias a tiendas (inventario movido).
- `Warehouse_Sales` (Numeric/Decimal): Ventas desde el almacén.

---

## 3. Gobierno de Datos (COBIT APO11 - Planificación)

### Políticas de Calidad de Datos (Reglas a implementar en ETL)
- **Completitud:** Ya que el dataset ha sido pre-limpiado y validado, no existen nulos ni valores vacíos. Sin embargo, por buenas prácticas de gobierno (APO11), la base de datos mantendrá las restricciones `NOT NULL` para asegurar que futuras ingestas mantengan la calidad.
- **Validez:** 
  - `Year` debe ser un año válido.
  - `Month` debe estar entre 1 y 12.
  - Las métricas cuantitativas (`Retail_Sales`, `Retail_Transfers`, `Warehouse_Sales`) aceptan valores negativos explícitamente, ya que representan devoluciones o ajustes de inventario.
  - Los formatos numéricos deben procesarse interpretando el punto (`.`) como separador decimal (tipo de dato `DECIMAL`).
- **Consistencia:** Garantizar integridad referencial mediante claves foráneas en la base de datos para que ninguna venta quede "huérfana" sin proveedor o producto.

### Gestión de Datos Maestros
- **Dim_Item** y **Dim_Supplier** serán tratadas como dimensiones de consolidación.
- Este catálogo oficial de productos y proveedores servirá como la única versión de la verdad (Single Source of Truth) para la analítica.
