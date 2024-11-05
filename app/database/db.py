import psycopg2

DATABASE_URL = "postgresql://user:password@localhost/auth_api"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)
