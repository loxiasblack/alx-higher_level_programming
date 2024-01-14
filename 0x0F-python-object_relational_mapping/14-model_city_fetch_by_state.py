#!/usr/bin/python3
"""Scrpits tha print all City objects
ftom the database"""

from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Mysession = Session()

    for state, city in Mysession.query(State, City).\
        filter(City.state_id == State.id).\
            order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")

Mysession.close()
