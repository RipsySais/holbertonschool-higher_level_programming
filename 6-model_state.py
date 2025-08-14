#!/usr/bin/python3
"""
Script that creates the State table in the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine


def main():
    """
    Main function to create the State table in the database.
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

    # Create all tables
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main() 