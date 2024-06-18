from dotenv import load_dotenv

load_dotenv()

import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.extraction import extractor_router
from app.api.routers.text_to_sql import t2sql_router
from app.db.database import create_db_and_tables


app = FastAPI(title="govbros")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set

if environment == "dev":
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
def root():
    return {"message": "thanks for playing."}


app.include_router(extractor_router, prefix="/api/extraction")
app.include_router(t2sql_router, prefix="/api/text-to-sql")


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=int("8000"),
        # reload=True,
        loop="asyncio",
    )
