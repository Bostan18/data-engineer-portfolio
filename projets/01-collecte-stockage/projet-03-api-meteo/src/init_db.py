"""Module de creation de la base de donnees SQLite pour la meteo."""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "weather.db")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    country TEXT,
    temperature REAL,
    feels_like REAL,
    temp_min REAL,
    temp_max REAL,
    pressure INTEGER,
    humidity INTEGER,
    wind_speed REAL,
    wind_deg INTEGER,
    weather_main TEXT,
    weather_description TEXT,
    clouds INTEGER,
    visibility INTEGER,
    sunrise TEXT,
    sunset TEXT,
    collected_at TEXT NOT NULL,
    UNIQUE(city, collected_at)
);
"""


def init_database():
    """Cree la base de donnees et la table weather si elles n'existent pas."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.executescript(SCHEMA_SQL)
    conn.commit()
    conn.close()
    print(f"Base creee avec succes : {DB_PATH}")


def get_connection():
    """Retourne une connexion a la base de donnees."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


if __name__ == "__main__":
    init_database()
