import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Puedes usar DATABASE_URL (estilo postgresql://user:password@host:port/dbname)
# o las variables separadas dependiendo de cómo armaste tu .env
DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", "5432")
    dbname = os.getenv("DB_NAME")
    DB_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

# Crear el motor de conexión de SQLAlchemy
engine = create_engine(DB_URL)
