"""Module de scraping des livres sur http://books.toscrape.com."""

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com"


def scrape_books(max_pages: int = 3) -> list[dict]:
    """Scrape les livres du catalogue, page par page.

    Args:
        max_pages: Nombre de pages a scraper.

    Returns:
        Liste de dictionnaires contenant les infos de chaque livre.
    """
    all_books = []

    for page_num in range(1, max_pages + 1):
        url = f"{BASE_URL}/catalogue/page-{page_num}.html"
        print(f"  Scraping page {page_num}/{max_pages}...")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"    Erreur: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod")

        for book in books:
            # Titre
            title_tag = book.select_one("h3 a")
            title = title_tag["title"] if title_tag else None

            # Prix
            price_tag = book.select_one("p.price_color")
            price = (
                float(price_tag.text.replace("£", "").replace("Â", ""))
                if price_tag
                else None
            )

            # Disponibilité
            stock_tag = book.select_one("p.instock.availability")
            stock = "In stock" in stock_tag.text if stock_tag else False

            # Note (le rating est dans la classe CSS : "star-rating One", "star-rating Two", etc.)
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating_tag = book.select_one("p.star-rating")
            rating = None
            if rating_tag:
                for cls in rating_tag.get("class", []):
                    if cls in rating_map:
                        rating = rating_map[cls]
                        break

            # URL image
            img_tag = book.select_one("img")
            img_url = f"{BASE_URL}/{img_tag['src'].lstrip('/')}" if img_tag else None

            all_books.append(
                {
                    "title": title,
                    "price": price,
                    "in_stock": stock,
                    "rating": rating,
                    "image_url": img_url,
                }
            )

    return all_books


if __name__ == "__main__":
    books = scrape_books(max_pages=2)
    print(f"\n{len(books)} livres scrapes.")
    for b in books[:5]:
        print(f"  {b['title']} — £{b['price']} — {b['rating']}/5")
