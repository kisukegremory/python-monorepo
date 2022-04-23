from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SampleTable(Base):
    __tablename__ = "SampleTable"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)