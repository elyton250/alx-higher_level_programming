#!/usr/bin/python3
"""This fetches things."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State#

if __name__ == "__main__":
    """this is makes main"""

    username = argv[1]
    password = argv[2]
    database = argv[3]
    host = 'localhost'
    port = 3306
    state_to_find = argv[4]

    connection = f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}'

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session3 = Session()

    found_state = session3.query(State)\
                        .filter(State.name == state_to_find)\
                        .order_by(State.id.asc())\
                        .first()

    if found_state:
        print(f"{found_state.id}: {found_state.name}")
    else:
        print("State not found.")
