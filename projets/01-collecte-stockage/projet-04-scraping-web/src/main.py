"""Pipeline complet : scraping → nettoyage → stockage SQL.

Utilisation :
    python src/main.py
"""

from init_db import get_connection, init_database
from scrape_books import scrape_books
from transform import clean_books


def insert_books(cursor, books: list[dict]):
    for book in books:
        cursor.execute(
            """
            INSERT OR IGNORE INTO books (title, price, in_stock, rating, image_url)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                book["title"],
                book["price"],
                1 if book["in_stock"] else 0,
                book["rating"],
                book["image_url"],
            ),
        )


def main():
    print("=== Pipeline Scraping → SQL ===\n")

    # 1. Scraping
    print("1/3 Scraping...")
    raw = scrape_books(max_pages=3)

    # 2. Nettoyage
    print("\n2/3 Nettoyage...")
    cleaned = clean_books(raw)

    # 3. Stockage
    print("\n3/3 Stockage SQL...")
    init_database()
    conn = get_connection()
    cursor = conn.cursor()
    insert_books(cursor, cleaned)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]
    print(f"\n{count} livres dans books.db")

    # Verification
    cursor.execute("SELECT title, price, rating FROM books ORDER BY price DESC LIMIT 5")
    print("\nTop 5 livres les plus chers :")
    for row in cursor.fetchall():
        print(f"  {row[0]:40s} £{row[1]:6.2f}  {row[2]}/5")

    conn.close()
    print("\nPipeline termine !")


if __name__ == "__main__":
    main()
