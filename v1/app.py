#!/usr/bin/python
import csv

import psycopg2

from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # Dataset 1
        dataset1 = """SELECT a.card_number, a.card_family, SUM(b.value), COUNT(b.id)
             FROM
                cards as a
              LEFT JOIN transactions as b ON a.card_number=b.card_number
              GROUP BY a.card_number, a.card_family;"""

        # Execute query
        cur.execute(dataset1)

        # Fetch query result
        rows = cur.fetchall()

        with open("dataset1.csv", "w") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(["card_number", "card_family", "value", "transactions"])

            for row in rows:
                writer.writerow(row)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    connect()
