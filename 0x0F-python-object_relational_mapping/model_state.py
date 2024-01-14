#!/usr/bin/python3

"""This module uses SQLAlchemy."""
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import declarative_base

mymetadata = MetaData()

Base = declarative_base(metadata=mymetadata)


class State(Base):
    """This is the State class."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
