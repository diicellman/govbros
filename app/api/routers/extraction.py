"""Endpoints."""

from fastapi import APIRouter

from app.engine.index import extract_sms_info
from app.crud.crud import create_sms_record

extractor_router = APIRouter()


@extractor_router.post("/parse_sms", tags=["extraction"])
async def extraction_query(sms_text: str):
    extraction_runnable = extract_sms_info()
    response = await extraction_runnable.ainvoke({"text": sms_text})

    create_sms_record(data=response)

    return response
