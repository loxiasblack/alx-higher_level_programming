#!/usr/bin/python3
"""scripts that print State object with name"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(
        State).filter(
            State.name.contains(
                sys.argv[4])).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
