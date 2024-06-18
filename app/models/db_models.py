from datetime import datetime
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4


class FinanceSMSTable(SQLModel, table=True):
    sms_id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    creation_timestamp: datetime = Field(description="Creation timestamp.")
    sms_text: str | None = Field(description="Text of the sms.")
    sms_type: str | None = Field("Type of sms: info or warning.")
    bank_name: str | None = Field(
        description="Title of the bank (ex. Bank of America)."
    )
    balance_amount: float | None = Field(
        description="Amount of current balance if available."
    )
    balance_currency: str | None = Field(description="Currency of transfer.")
    amount: float | None = Field(description="Amount.")
    currency: str | None = Field(description="Currecny.")
    type_of_operation: str | None = Field(description="Type of the transfer.")
