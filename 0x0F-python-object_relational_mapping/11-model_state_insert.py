#!/usr/bin/python3
"""this fetches in the database"""


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
    connection = f'mysql+mysqldb://{username}:{password}@{host}:3306/{database}'

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)

    session5 = Session()

    new_state = State(name='Louisiana')
    session5.add(new_state)
    session5.commit()
    session5.close()
