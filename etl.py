import requests
import pandas as pd
import psycopg2

class Extract:
    @staticmethod
    def from_api(url: str):
        response = requests.get(url)
        response.raise_for_status()  # Ensures that the request was successful
        return response.json()

    @staticmethod
    def from_csv(file_path: str):
        return pd.read_csv(file_path)

    @staticmethod
    def from_db(database: str, query: str, user: str, password: str, host: str = 'localhost', port: str = '5432'):
        # Establishing the connection to the PostgreSQL database
        connection = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        # Reading data from the database using pandas
        data = pd.read_sql_query(query, connection)
        connection.close()
        return data