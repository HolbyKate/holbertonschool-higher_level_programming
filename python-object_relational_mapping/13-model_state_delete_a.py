#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()
    #delete all State objects with a name containing the letter a
    states_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    if states_delete:
        for state in states_delete:
            session.delete(state)
        session.commit()
        
    session.close()
