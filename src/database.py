import sqlite3
import pandas as pd

DB_PATH = "database/sales.db"


def get_connection():
    """
    Creates and returns a SQLite connection.
    """
    return sqlite3.connect(DB_PATH)


def load_data():
    """
    Loads the sales_cleaned table into a Pandas DataFrame.
    """
    conn = get_connection()

    query = """
    SELECT *
    FROM sales_data
    """
    

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df