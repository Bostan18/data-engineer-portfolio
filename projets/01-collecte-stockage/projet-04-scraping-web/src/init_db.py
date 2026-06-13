"""Module de creation de la base de donnees SQLite pour les livres scrapes."""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "books.db")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    price REAL,
    in_stock INTEGER,
    rating INTEGER,
    image_url TEXT
);
"""


def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.executescript(SCHEMA_SQL)
    conn.commit()
    conn.close()
    print(f"Base creee : {DB_PATH}")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


if __name__ == "__main__":
    init_database()
