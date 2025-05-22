import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )


def save_user_profile(name, email, income_range, goal):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            income_range VARCHAR(50),
            goal TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("INSERT INTO user_profiles (name, email, income_range, goal) VALUES (%s, %s, %s, %s)",
                   (name, email, income_range, goal))
    conn.commit()
    cursor.close()
    conn.close()


def get_user_id_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user_profiles WHERE email = %s", (email,))
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
            category VARCHAR(50),
            amount FLOAT,
            note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user_profiles(id)
        )
    """)
    cursor.execute("INSERT INTO spending (user_id, category, amount, note) VALUES (%s, %s, %s, %s)",
                   (user_id, category, amount, note))
    conn.commit()
    cursor.close()
    conn.close()


def save_recommendation(user_id, recommendation_text):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            recommendation TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user_profiles(id)
        )
    """)
    cursor.execute("INSERT INTO recommendations (user_id, recommendation) VALUES (%s, %s)",
                   (user_id, recommendation_text))
    conn.commit()
    cursor.close()
    conn.close()
