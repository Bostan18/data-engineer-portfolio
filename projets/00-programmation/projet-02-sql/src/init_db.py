import sqlite3


def init_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # Supprime les tables existantes (ordre inverse des dependances)
    cursor.executescript("DROP TABLE IF EXISTS loans")
    cursor.executescript("DROP TABLE IF EXISTS books")
    cursor.executescript("DROP TABLE IF EXISTS borrowers")
    cursor.executescript("DROP TABLE IF EXISTS authors")
    cursor.executescript("DROP VIEW IF EXISTS current_loans")

    # Re-cree le schema
    with open("src/schema.sql", "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    # Cree les vues
    with open("src/views.sql", "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Base reinitialisee avec succes !")

    print("Base reinitialisee avec succes !")

if __name__ == "__main__":
    init_database()
