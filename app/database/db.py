from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
def get_db_connection():
    return psycopg2.connect(DATABASE_URL)
