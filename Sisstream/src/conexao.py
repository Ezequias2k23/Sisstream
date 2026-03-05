import psycopg2

def conectar():
    conn = psycopg2.connect(
        host="localhost",
        database="sisstream",
        user="postgres",
        password="12345",
        port=5432
    )
    return conn