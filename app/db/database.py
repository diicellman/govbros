from sqlmodel import create_engine, SQLModel
from app.models.db_models import FinanceSMSTable

SQLITE_DATABASE_URL = "sqlite:///./sql_app.db"
sql_engine = create_engine(SQLITE_DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(sql_engine, tables=[FinanceSMSTable.__table__])
