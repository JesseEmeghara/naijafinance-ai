import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_NAME')
}

def get_connection():
    return mysql.connector.connect(**db_config)

def save_user_profile(name, email, income_range, financial_goal):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO users (name, email, income_range, financial_goal)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE income_range = VALUES(income_range), financial_goal = VALUES(financial_goal)
    """
    cursor.execute(query, (name, email, income_range, financial_goal))
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

def add_spending(user_id, category, amount, note=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO spending (user_id, category, amount, note)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, category, amount, note))
    conn.commit()
    cursor.close()
    conn.close()

def save_recommendation(user_id, recommendation):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO recommendations (user_id, recommendation)
        VALUES (%s, %s)
    """
    cursor.execute(query, (user_id, recommendation))
    conn.commit()
    cursor.close()
    conn.close()

def get_recommendations(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT recommendation, created_at
        FROM recommendations
        WHERE user_id = %s
        ORDER BY created_at DESC
    """
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
