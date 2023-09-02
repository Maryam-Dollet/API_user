import psycopg2
from psycopg2.extras import DictCursor, RealDictCursor
import os
import time
from dotenv import load_dotenv

load_dotenv()


def db_connection():
    while True:
        try:
            connection = psycopg2.connect(
                host=os.getenv("HOST"),
                database=os.getenv("DATABASE"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                port=os.getenv("PORT"),
            )
            cursor_dict = connection.cursor(cursor_factory=DictCursor)
            cursor_realdict = connection.cursor(cursor_factory=RealDictCursor)
            # cursor = connection.cursor()
            print("Database connection was succeful \U0001F44C !")
            return connection, cursor_dict, cursor_realdict
        except (Exception, psycopg2.Error) as error:
            print("Connecting to Database failed...")
            print("Error : ", error)
            time.sleep(2)
