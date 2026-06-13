"""Module de nettoyage des donnees scrapees."""


def clean_books(raw_books: list[dict]) -> list[dict]:
    """Nettoie la liste des livres scrapes.

    - Supprime les doublons (par titre)
    - Supprime les livres sans titre ou sans prix
    """
    seen_titles = set()
    cleaned = []

    for book in raw_books:
        # Ignore les livres incomplets
        if not book["title"] or book["price"] is None:
            continue

        # Supprime les doublons
        if book["title"] in seen_titles:
            continue
        seen_titles.add(book["title"])

        cleaned.append(book)

    print(
        f"Nettoyage : {len(raw_books)} → {len(cleaned)} livres (doublons/incomplets retires)"
    )
    return cleaned


if __name__ == "__main__":
    sample = [
        {
            "title": "A",
            "price": 10.0,
            "in_stock": True,
            "rating": 4,
            "image_url": "/img",
        },
        {
            "title": "A",
            "price": 10.0,
            "in_stock": True,
            "rating": 4,
            "image_url": "/img",
        },  # doublon
        {
            "title": None,
            "price": 5.0,
            "in_stock": True,
            "rating": 3,
            "image_url": "/img",
        },  # pas de titre
    ]
    result = clean_books(sample)
    print(f"Resultat: {len(result)} livre(s) apres nettoyage")
