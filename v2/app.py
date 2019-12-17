#!/usr/bin/python

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://read_only_user:banking123@db-stone-challenge.cjepwwjnksng.us-east-1.rds.amazonaws.com:5432/postgres"
)


def main():
    csv1()


def csv1():

    sql = """SELECT a.card_number, a.card_family, SUM(b.value) as sum, COUNT(b.id) as transactions
        FROM
            cards as a
        LEFT JOIN transactions as b ON a.card_number=b.card_number
        GROUP BY a.card_number, a.card_family;"""

    result = pd.read_sql_query(sql, engine)

    df = pd.DataFrame(result)

    df.to_csv("dataframe1.csv")


if __name__ == "__main__":
    main()
