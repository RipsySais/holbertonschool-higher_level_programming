#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Main function to list all State objects containing the letter 'a'.
    """
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing letter 'a' ordered by id
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Print each state
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()


if __name__ == "__main__":
    main() 