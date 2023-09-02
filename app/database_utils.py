import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()


def db_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432",
            cursor_factory=RealDictCursor,
        )
        cursor = connection.cursor()
        print("Database connection was succeful !")
    except Exception as error:
        print("Connecting to Database failed...")
        print("Error : ", error)
