import json


class Book:
    def __init__(self, title: str, author: str, year: int, category: str):
        self.title = title
        self.author = author
        self.year = year
        self.category = category

    def __str__(self):
        return f"{self.title} par {self.author} ({self.year}) - {self.category}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Livre supprimé")
                return
        print("Livre introuvable")

    def display_all(self):
        """Affiche tous les livres"""
        for book in self.books:
            print(book)

    def search_by_title(self, title):
        """Recherche un livre par titre (insensible a la casse)"""
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)

    def sort_by_year(self):
        """Trie les livres par annee de publication"""
        self.books.sort(key=lambda book: book.year)

    def save_to_json(self, filename="library.json"):
        """Sauvegarde la bibliotheque dans un fichier JSON"""
        data = []
        for book in self.books:
            data.append(
                {
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "category": book.category,
                }
            )
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self, filename="library.json"):
        """Charge les livres depuis un fichier JSON"""
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.books = []
        for item in data:
            self.books.append(
                Book(item["title"], item["author"], item["year"], item["category"])
            )

    def search_by_author(self, author):
        """Recherche les livres d'un auteur"""
        for book in self.books:
            if author.lower() in book.author.lower():
                print(book)

    def sort_by_category(self):
        """Trie les livres par categorie"""
        self.books.sort(key=lambda book: book.category)
