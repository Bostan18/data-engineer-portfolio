# Projet 03 : Systeme de collecte de donnees API et stockage SQL

## Contexte metier

Une entreprise dans le secteur du tourisme souhaite automatiser la collecte de donnees meteo pour ses differentes destinations afin d'optimiser ses recommandations aux clients. Ces donnees doivent etre structurees et accessibles aux equipes pour integrer des previsions dans leurs applications mobiles.

## Contexte technique

Collecter des donnees via une API publique (OpenWeather API) pour les donnees meteo. Les donnees collectees sont nettoyees, normalisees, et stockees dans une base SQL.

## Technologies

Python 3.12, SQLite3, `requests`

## Structure

```
├── src/
│   ├── fetch_weather.py    # Connexion API, recupération JSON
│   ├── transform.py        # Nettoyage et transformation
│   ├── init_db.py          # Création des tables SQL
│   └── main.py             # Orchestration complète
├── data/
│   └── raw/                # Données brutes JSON
├── tests/
└── README.md
```

## Etapes cles

1. Se connecter a l'API OpenWeather avec une cle d'acces (`requests`)
2. Recuperer les donnees au format JSON
3. Nettoyer et transformer les donnees (normalisation, gestion des valeurs manquantes)
4. Creer une base de donnees relationnelle et concevoir les tables necessaires (SQLite)
5. Inserer les donnees dans la base SQL

## Criteres de reussite

- [x] Code fonctionnel et teste
- [x] Documentation completee dans Notion
- [x] Commit pousse sur GitHub
