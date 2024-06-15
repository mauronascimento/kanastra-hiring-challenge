import os

from databases import Database
from sqlalchemy import create_engine
from fastapi_sqlalchemy import DBSessionMiddleware
from app.models.models import Base


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


def init_db(app):
    app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    return Database(DATABASE_URL)
