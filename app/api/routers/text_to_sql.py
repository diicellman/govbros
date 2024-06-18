"""Endpoints."""

from fastapi import APIRouter

from app.engine.index import chain_sql_qa

t2sql_router = APIRouter()


@t2sql_router.post("/query", tags=["text-to-sql"])
async def t2sql_query(question: str):
    chain = chain_sql_qa()
    response = await chain.ainvoke({"question": question})

    return response
