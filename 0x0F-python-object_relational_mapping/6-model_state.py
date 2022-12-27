#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from urllib.parse import quote
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:%s@localhost/{}".format(sys.argv[1], sys.argv[3]) % quote(sys.argv[2]))
    Base.metadata.create_all(engine)
