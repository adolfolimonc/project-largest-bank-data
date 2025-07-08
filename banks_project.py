from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime


def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(code_log, 'a') as f:
        f.write(timestamp + ': ' + message + '\n')


def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')

    df = pd.DataFrame(columns=table_attribs)

    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            data_dict = {"Bank_name": col[1].find_all(
                'a')[1]["title"], "MC_USD_Billion": float(col[2].contents[0][:-1])}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
    return df


def transform(df, csv_path):
    exchange_rate = pd.read_csv(csv_path)
    exchange_rate = exchange_rate.set_index("Currency").to_dict()["Rate"]

    df["MC_GBP_Billion"] = [np.round(x * exchange_rate["GBP"], 2)
                            for x in df["MC_USD_Billion"]]
    df["MC_EUR_Billion"] = [np.round(x * exchange_rate["EUR"], 2)
                            for x in df["MC_USD_Billion"]]
    df["MC_INR_Billion"] = [np.round(x * exchange_rate["INR"], 2)
                            for x in df["MC_USD_Billion"]]
    return df


def load_to_csv(df, csv_output):
    df.to_csv(csv_output, index=False)


def load_to_db(df, table_name, conn):
    df.to_sql(table_name, conn, if_exists='replace', index=False)


def run_queries(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Bank_name', 'MC_USD_Billion']
code_log = './code_log.txt'
csv_path = './exchange_rate.csv'
csv_output = './banks_data.csv'
table_name = 'Largest_banks'
db_name = 'Banks.db'

# Extract function
log_progress('Initialising ETL Process...')
df = extract(url, table_attribs)
print(df)
log_progress('Data Extraction completed!\n')

# Transformation function
log_progress('Initialising transformation...')
df = transform(df, csv_path)
log_progress('Completed!\n')
print(df)

# Load to CSV
log_progress('Loading to a CSV file!')
load_to_csv(df, csv_output)
log_progress('Completed!\n')

# Load to DB
log_progress('SQL Connection initiated.')
sql_connection = sqlite3.connect(db_name)
load_to_db(df, table_name, sql_connection)
log_progress('Data loaded to Database!\n')

# Queries
log_progress('Executing queries...')
query_statement = f"SELECT MC_GBP_Billion FROM {table_name}"
run_queries(query_statement, sql_connection)
query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_queries(query_statement, sql_connection)
query_statement = f"SELECT Bank_name FROM {table_name} LIMIT 5"
run_queries(query_statement, sql_connection)
log_progress('Queries executed successfully!\n')

# Close DB connection
sql_connection.close()
log_progress("Server Connection closed")

with open(code_log, "r") as log:
    LogContent = log.read()
    print(LogContent)
