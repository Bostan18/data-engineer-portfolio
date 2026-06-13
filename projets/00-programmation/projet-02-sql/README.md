# Projet 02 : Aventure SQL

## Objectif

Maitriser les bases de donnees relationnelles en creant un schema pour une bibliotheque, en inserant des donnees fictives, et en ecrivant des requetes analytiques avancees.

## Technologies

Python 3.12, SQLite3

## Structure

```
├── src/
│   ├── schema.sql     # 4 tables (authors, books, borrowers, loans)
│   ├── views.sql      # Vue current_loans
│   ├── init_db.py     # Creation/reinitialisation de la base
│   ├── seed_data.py   # Insertion de donnees fictives
│   └── queries.py     # 3 requetes analytiques
├── data/
├── tests/
└── README.md
```

## Etapes cles

1. Modelisation du schema relationnel : tables, PK, FK, relations 1-N
2. Creation de la base avec `init_db.py` (PRAGMA foreign_keys = ON)
3. Insertion de donnees avec `executemany()` et parametrized queries (?)
4. Vues SQL pour simplifier les requetes frequentes
5. Requetes analytiques : JOIN multiples, GROUP BY, COUNT, ORDER BY, LIMIT

## Criteres de reussite

- [x] Code fonctionnel et teste
- [x] Documentation completee dans Notion
- [x] Commit pousse sur GitHub
