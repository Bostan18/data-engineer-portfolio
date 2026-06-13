import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# 1. Quels sont les livres empruntes cette semaine ?
print("=== Livres empruntes cette semaine ===")
cursor.execute("""
    SELECT books.title, borrowers.name, loans.loan_date
    FROM loans
    JOIN books ON loans.book_id = books.id
    JOIN borrowers ON loans.borrower_id = borrowers.id
    WHERE loans.loan_date >= DATE('now', '-7 days')
""")
for row in cursor.fetchall():
    print(f"  {row[0]} emprunte par {row[1]} le {row[2]}")

# 2. Quel auteur a publie le plus de livres ?
print("\n=== Auteur le plus prolifique ===")
cursor.execute("""
    SELECT authors.name, COUNT(books.id) AS nb_books
    FROM authors
    JOIN books ON authors.id = books.author_id
    GROUP BY authors.id
    ORDER BY nb_books DESC
    LIMIT 1
""")
result = cursor.fetchone()
print(f"  {result[0]} avec {result[1]} livres")

# 3. Quels emprunteurs ont emprunte le plus de livres ?
print("\n=== Top emprunteurs ===")
cursor.execute("""
    SELECT borrowers.name, COUNT(loans.id) AS nb_emprunts
    FROM borrowers
    JOIN loans ON borrowers.id = loans.borrower_id
    GROUP BY borrowers.id
    ORDER BY nb_emprunts DESC
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} emprunt(s)")

conn.close()
