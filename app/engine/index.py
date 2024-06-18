"""SMS info extraction program."""

# import logging
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.engine.prompts import EXTRACTION_PROMPT, ANSWER_PROMPT
from app.models.models import FinanceSMS
from app.db.database import SQLITE_DATABASE_URL


# global default
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_key")


db = SQLDatabase.from_uri(SQLITE_DATABASE_URL)


def extract_sms_info():
    llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=OPENAI_API_KEY)
    runnable = EXTRACTION_PROMPT | llm.with_structured_output(schema=FinanceSMS)

    return runnable


def chain_sql_qa():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=OPENAI_API_KEY)
    execute_query = QuerySQLDataBaseTool(db=db)
    write_query = create_sql_query_chain(llm, db)
    chain = create_sql_query_chain(llm, db)

    chain = (
        RunnablePassthrough.assign(query=write_query).assign(
            result=itemgetter("query") | execute_query
        )
        | ANSWER_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain
