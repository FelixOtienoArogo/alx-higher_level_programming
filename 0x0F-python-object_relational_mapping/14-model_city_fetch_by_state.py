#!/usr/bin/python3
"""lists all States objects from hbtn_0e_6_usa."""


import sys
from model_state import Base, State
from model_city import City
from urllib.parse import quote
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:%s@localhost/{}"
                           .format(sys.argv[1], sys.argv[3]) %
                           quote(sys.argv[2]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(State.id):
        print("{}: ({}) {}".
              format(state.name, city.id, city.name))
