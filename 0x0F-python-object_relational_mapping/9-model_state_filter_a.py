#!/usr/bin/python3
"""scrpits that list state object that contain letter 'a'
from the database"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(
                                State).filter(
                                    State.name.contains('a')).order_by(
                                        State.id):
        print(f"{state.id}: {state.name}")
