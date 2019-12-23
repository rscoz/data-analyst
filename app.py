#!/usr/bin/python

import pandas as pd

import sqlalchemy
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine(
    "postgresql://read_only_user:banking123@db-stone-challenge.cjepwwjnksng.us-east-1.rds.amazonaws.com:5432/postgres"
)

sql1 = """SELECT a.card_number, a.card_family, SUM(b.value) as sum, COUNT(b.id) as transactions
    FROM
        cards as a
    LEFT JOIN transactions as b ON a.card_number=b.card_number
    GROUP BY a.card_number, a.card_family;"""


sql2 = """SELECT a.id as customer_id, a.segment, COUNT(c.id) as transactions
    FROM
        customers as a
    LEFT JOIN cards as b ON a.id=b.customer_id
    LEFT JOIN transactions as c ON b.card_number=c.card_number
    WHERE a.segment='Diamond'
    GROUP BY a.id
    HAVING COUNT(c.id) > 40;"""


def generate_csv(query, conn):

    result = pd.read_sql_query(query, conn)

    df = pd.DataFrame(result)

    json = df.to_json(orient="split")
    return json


@app.route("/sql1")
def result1():
    return generate_csv(sql1, engine)


@app.route("/sql2")
def result2():
    return generate_csv(sql2, engine)


app.run()
