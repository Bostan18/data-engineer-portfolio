# Projet 01 : Bibliotheque Personnelle en Python

## Objectif

Creer une application de gestion de bibliotheque en Python pour apprendre la programmation orientee objet et la persistance de donnees avec JSON.

## Technologies

Python 3.12 (modules integres : json)

## Structure

```
├── src/
│   ├── book.py       # Classes Book et Library
│   └── main.py       # Demo
├── data/
├── tests/
└── README.md
```

## Etapes cles

1. Classe `Book` : attributs (title, author, year, category) + `__str__`
2. Classe `Library` : `add_book()`, `remove_book()` avec recherche insensible a la casse
3. Methodes d'affichage et recherche : `display_all()`, `search_by_title()`, `search_by_author()`
4. Tri : `sort_by_year()`, `sort_by_category()` avec `lambda`
5. Persistance JSON : `save_to_json()`, `load_from_json()` — serialisation/deserialisation

## Criteres de reussite

- [x] Code fonctionnel et teste
- [x] Documentation completee dans Notion
- [x] Commit pousse sur GitHub
