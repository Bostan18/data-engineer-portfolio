import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# 1. Insertion des auteurs
authors = [
    ("George Orwell", 1903),
    ("Frank Herbert", 1920),
    ("Isaac Asimov", 1920),
    ("Antoine de Saint-Exupery", 1900),
    ("J.K. Rowling", 1965),
]
cursor.executemany("INSERT INTO authors (name, birth_year) VALUES (?, ?)", authors)

# 2. Insertion des livres
books = [
    ("1984", 1949, "Science-Fiction", 1),  # Orwell
    ("Dune", 1965, "Science-Fiction", 2),  # Herbert
    ("Fondation", 1951, "Science-Fiction", 3),  # Asimov
    ("Le Petit Prince", 1943, "Conte", 4),  # Saint-Exupery
    ("Harry Potter", 1997, "Fantasy", 5),  # Rowling
    ("La Ferme des Animaux", 1945, "Satire", 1),  # Orwell
]
cursor.executemany(
    "INSERT INTO books (title, year, category, author_id) VALUES (?, ?, ?, ?)", books
)

# 3. Insertion des emprunteurs
borrowers = [
    ("Alice Dupont", "alice@email.com"),
    ("Bob Martin", "bob@email.com"),
    ("Claire Bernard", "claire@email.com"),
]
cursor.executemany("INSERT INTO borrowers (name, email) VALUES (?, ?)", borrowers)

# 4. Insertion des emprunts
loans = [
    (1, 1, "2026-06-01", None),  # Alice a emprunte 1984
    (2, 2, "2026-06-03", None),  # Bob a emprunte Dune
    (4, 1, "2026-05-20", "2026-05-28"),  # Alice a rendu Le Petit Prince
    (5, 3, "2026-06-05", None),  # Claire a emprunte Harry Potter
]
cursor.executemany(
    "INSERT INTO loans (book_id, borrower_id, loan_date, return_date) VALUES (?, ?, ?, ?)",
    loans,
)

conn.commit()
conn.close()
print("Donnees inserees avec succes !")
