#!/usr/bin/python3
"""class definition of a State and an instance
Base = declarative_base()"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)






