#!/usr/bin/python3
"""this updates state"""

from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """this is makes main"""

    username = argv[1]
    password = argv[2]
    database = argv[3]
    host = "localhost"
    connection = \
        f'mysql+mysqldb://{username}:{password}@{host}:3306/{database}'

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)

    session6 = Session()

    to_up = session6.query(State).filter_by(id=2)

    if to_up:
        if to_up.id == 2:
            to_up.name = 'New Mexico'
    session6.commit()
