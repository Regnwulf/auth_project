from fastapi import HTTPException
from jose import jwt
from datetime import datetime, timedelta
import hashlib
import os
import psycopg2
from app.models.user import User
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def generate_salt():
    return os.urandom(16)

def hash_password(password: str, salt: bytes) -> str:
    return hashlib.sha256(salt + password.encode()).hexdigest()

def authenticate_user(username: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, salt, role FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result is None:
        return False

    password_hash, salt, role = result
    if hash_password(password, bytes.fromhex(salt)) == password_hash:
        return User(username=username, role=role)
    return False

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_user_info(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    role = payload.get("role")
    if role != "user":
        raise HTTPException(status_code=403, detail="Acesso negado")
    return {"msg": "Você está acessando a rota do usuário!"}

def get_admin_info(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    role = payload.get("role")
    if role != "admin":
        raise HTTPException(status_code=403, detail="Acesso negado")
    return {"msg": "Você está acessando a rota do administrador!"}
