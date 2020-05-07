from app import db
from sqlalchemy import (Column, Integer, Float, String, DateTime)


class Client(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default='now()')