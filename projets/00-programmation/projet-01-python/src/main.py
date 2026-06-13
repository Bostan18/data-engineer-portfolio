from book import Book, Library

# Création de la bibliothèque
biblio = Library()
biblio.add_book(Book("1984", "George Orwell", 1949, "Science-Fiction"))
biblio.add_book(Book("Dune", "Frank Herbert", 1965, "Science-Fiction"))
biblio.add_book(Book("Fondation", "Isaac Asimov", 1951, "Science-Fiction"))
biblio.add_book(Book("Le Petit Prince", "Antoine de Saint-Exupery", 1943, "Conte"))

print("=== Tous les livres (tries par annee) ===")
biblio.sort_by_year()
biblio.display_all()

print("\n=== Recherche auteur 'frank' ===")
biblio.search_by_author("frank")

print("\n=== Suppression de '1984' ===")
biblio.remove_book("1984")

# Sauvegarde
biblio.save_to_json()
print("\nBibliotheque sauvegardee. Nombre de livres restants :", len(biblio.books))

# Rechargement
biblio2 = Library()
biblio2.load_from_json()
print("\n=== Apres rechargement ===")
biblio2.display_all()
