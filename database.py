from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER").replace("\\", "\\\\")
DB_NAME = os.getenv("DB_NAME")

# Windows Auth with pyodbc
connection_string = (
    f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
    f"?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

engine = create_engine(connection_string)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
