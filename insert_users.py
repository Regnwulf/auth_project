import psycopg2
import hashlib
import os

def generate_salt():
    return os.urandom(16)

def hash_password(password: str, salt: bytes) -> str:
    return hashlib.sha256(salt + password.encode()).hexdigest()

def insert_users(conn):
    cursor = conn.cursor()

    user_password = "L0XuwPOdS5U"
    user_salt = generate_salt()
    user_hash = hash_password(user_password, user_salt)

    cursor.execute(
        "INSERT INTO users (username, role, password_hash, salt) VALUES (%s, %s, %s, %s)",
        ('user', 'user', user_hash, user_salt.hex())
    )

    admin_password = "JKSipm0YH"
    admin_salt = generate_salt()
    admin_hash = hash_password(admin_password, admin_salt)

    cursor.execute(
        "INSERT INTO users (username, role, password_hash, salt) VALUES (%s, %s, %s, %s)",
        ('admin', 'admin', admin_hash, admin_salt.hex())
    )

    conn.commit()
    cursor.close()
    print("Usuários inseridos com sucesso!")

if __name__ == "__main__":
    # Conexão com o banco de dados
    conn = psycopg2.connect("postgresql://user:password@localhost/auth_api")
    
    # Inserir os usuários
    insert_users(conn)
    
    # Fechar a conexão
    conn.close()
