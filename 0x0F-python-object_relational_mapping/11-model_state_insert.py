#!/usr/bin/python3
"""scripts that adds the state objects 'Louisiana'
to the database"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    Mysession = Session()

    new_state = State(name="Louisiana")
    Mysession.add(new_state)
    Mysession.commit()

    state = Mysession.query(State).filter_by(name="Louisiana").first()
    print(state.id)

    Mysession.close()
