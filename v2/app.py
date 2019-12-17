#!/usr/bin/python
import csv

import pandas as pd
import psycopg2

from config import config

def main():
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
        sql = """SELECT a.card_number, a.card_family, SUM(b.value) as sum, COUNT(b.id) as transactions
            FROM
                cards as a
            LEFT JOIN transactions as b ON a.card_number=b.card_number
            GROUP BY a.card_number, a.card_family;"""

        result = pd.read_sql_query(sql, conn)

        # close the communication with the PostgreSQL

        df = pd.DataFrame(result)

        df.to_csv("dataframe1.csv")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
