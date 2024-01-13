#!/usr/bin/python3
 
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

db_path = "sqlite:///database.db"

engine = create_engine(db_path)
base = declarative_base()

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


base.metadata.create_all(engine)