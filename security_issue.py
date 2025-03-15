import psycopg2

DB_PASSWORD = "p@ssw0rd123"  # Insecure

def connect_db():
    return psycopg2.connect(
        host="localhost",
        user="admin",
        password=DB_PASSWORD  # 😱 Secrets in code
    )