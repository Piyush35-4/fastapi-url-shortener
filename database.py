import sqlite3

DB_NAME = "urls.db"


def get_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            expiry_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def insert_url(original_url, short_code, expiry_date):
    conn = get_db()
    conn.execute(
        "INSERT INTO urls (original_url, short_code, expiry_date) VALUES (?, ?, ?)",
        (original_url, short_code, expiry_date)
    )
    conn.commit()
    conn.close()


def get_url(short_code):
    conn = get_db()
    row = conn.execute(
        "SELECT original_url, expiry_date FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()
    conn.close()
    return row
