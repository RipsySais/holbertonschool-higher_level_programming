#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to MySQL database and list states starting with N.
    """
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create cursor object
        cursor = db.cursor()

        # Execute query to select states with name starting with N
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main() 