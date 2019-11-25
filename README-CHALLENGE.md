# Data Analyst Challenge

This is Stone's data analyst challenge. The objective is to extract and process data from a database. 

The solution can be developed in any programming language and the code **must** be hosted in a Github or Gitlab repository. 

## Instructions

Access the PostgreSQL database using the following credentials:

```
host: 
port: 5432
user: read-only-user
password: stone123
```

The database contains credit card transactional data in 4 tables:

- customers
- cards
- transactions
- frauds

Develop code to extract 2 kinds of datasets and export them to csv files. The required datasets are the following:

1. The number of transactions and the total value purchased of each credit card grouped by card number and card family.
2. All the customer ids that have "Diamond" segment and made at least 40 transactions.

## Extras

The following extra tasks are not required, but can give your solution bonus points.

1. The table _frauds_ shows all the transaction ids that were proven to be fraudulent. Analyze the data to find a correlation between the fraudulent transactions and the other features of the dataset. Explain your results.

2. Develop a Dockerfile and/or a docker-compose file to automate your data processing application.
