from sqlmodel import Session

from datetime import datetime
from app.models.db_models import FinanceSMSTable
from app.models.models import FinanceSMS
from app.db.database import sql_engine


def create_sms_record(data: FinanceSMS):
    with Session(sql_engine) as session:
        current_datetime = datetime.now()
        meta_row = FinanceSMSTable(
            creation_timestamp=current_datetime,
            sms_text=data.sms_text,
            bank_name=data.bank_name,
            balance_amount=data.balance_amount,
            balance_currency=data.balance_currency,
            amountr=data.amount,
            currency=data.currency,
            type_of_operation=data.type_of_operation,
        )
        session.add(meta_row)
        session.commit()
        session.refresh(meta_row)

    return {"message": "success"}
