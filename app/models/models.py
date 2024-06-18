"""Pydantic models."""

# import datetime
from typing import Optional, Literal
from langchain_core.pydantic_v1 import BaseModel, Field


class FinanceSMS(BaseModel):
    """Datamodel for finance sms message details."""

    sms_text: str = Field(description="Text of the sms.")
    sms_type: Literal["info", "warning"] = Field(
        description="Type of sms: info or warning."
    )
    bank_name: Optional[str] = Field(
        description="Title of the bank (ex. Bank of America)."
    )
    balance_amount: Optional[float] = Field(
        description="Amount of current balance if available."
    )
    balance_currency: Optional[str] = Field(description="Currency of transfer.")
    amount: Optional[float] = Field(description="Amount of operation.")
    currency: Optional[str] = Field(description="Currecny of operation.")
    type_of_operation: Literal[
        "deposit",
        "withdrawal",
        "purchase",
        "transfer",
        "send",
        "receive",
        "balance",
        "info",
    ] = Field(description="Type of the transfer.")
