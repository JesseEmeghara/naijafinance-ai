import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )

def save_user_profile(name, email, income_range, goal):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            income_range VARCHAR(255),
            goal TEXT
        )
    """)
    cursor.execute("INSERT INTO users (name, email, income_range, goal) VALUES (%s, %s, %s, %s)", 
                   (name, email, income_range, goal))
    conn.commit()
    cursor.close()
    conn.close()

def get_user_id_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None

def add_spending(user_id, category, amount, note):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS spending (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            category VARCHAR(255),
            amount FLOAT,
            note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("INSERT INTO spending (user_id, category, amount, note) VALUES (%s, %s, %s, %s)",
                   (user_id, category, amount, note))
    conn.commit()
    cursor.close()
    conn.close()
