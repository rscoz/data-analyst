#!/usr/bin/python

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://read_only_user:banking123@db-stone-challenge.cjepwwjnksng.us-east-1.rds.amazonaws.com:5432/postgres"
)


def main():
    csv1()
    csv2()


def csv1():

    sql = """SELECT a.card_number, a.card_family, SUM(b.value) as sum, COUNT(b.id) as transactions
        FROM
            cards as a
        LEFT JOIN transactions as b ON a.card_number=b.card_number
        GROUP BY a.card_number, a.card_family;"""

    result = pd.read_sql_query(sql, engine)

    df = pd.DataFrame(result)

    df.to_csv("dataframe1.csv")


def csv2():

    sql = """SELECT a.id as customer_id, a.segment, COUNT(c.id) as transactions
        FROM
            customers as a
        LEFT JOIN cards as b ON a.id=b.customer_id
        LEFT JOIN transactions as c ON b.card_number=c.card_number
        WHERE a.segment='Diamond'
        GROUP BY a.id
        HAVING COUNT(c.id) > 40;"""

    result = pd.read_sql_query(sql, engine)

    df = pd.DataFrame(result)

    if df.empty == True:
        print("Dataframe 2 is empty")
    else:
        df.to_csv("dataframe2.csv")


if __name__ == "__main__":
    main()
