import duckdb
import pandas as pd

# Singleton pattern for DuckDB connection
import os

def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'my_database.duckdb')
    if 'con' not in globals():
        globals()['con'] = duckdb.connect(db_path)
    return globals()['con']

def register_dataframe(name, df):
    con = get_connection()
    con.register(name, df)

def run_query(query):
    con = get_connection()
    return con.execute(query).df()

def close_connection():
    if 'con' in globals():
        globals()['con'].close()
        del globals()['con']

# --- Additional Database Utilities ---
def import_csv_to_table(csv_path, table_name, header=True):
    con = get_connection()
    header_option = 'HEADER' if header else ''
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{csv_path}', {header_option});")

def import_parquet_to_table(parquet_path, table_name):
    con = get_connection()
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_parquet('{parquet_path}');")

def export_table_to_csv(table_name, csv_path):
    con = get_connection()
    con.execute(f"COPY (SELECT * FROM {table_name}) TO '{csv_path}' (FORMAT CSV, HEADER);")

def export_table_to_parquet(table_name, parquet_path):
    con = get_connection()
    con.execute(f"COPY (SELECT * FROM {table_name}) TO '{parquet_path}' (FORMAT PARQUET);")

def list_tables():
    con = get_connection()
    return con.execute("SHOW TABLES;").df()

def describe_table(table_name):
    con = get_connection()
    return con.execute(f"DESCRIBE {table_name};").df()
