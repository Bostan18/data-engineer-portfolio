# Projet 05 : Pipeline ETL Olist — Analyse des ventes e-commerce

## Contexte metier

L'entreprise bresilienne Olist souhaite centraliser ses donnees de ventes provenant de multiples sources (commandes, clients, produits, vendeurs, paiements, avis) pour identifier les produits les plus performants, les periodes de forte activite et les tendances emergentes.

## Contexte technique

Pipeline ETL complet en 4 etapes sur le dataset Olist (100k commandes, 9 fichiers CSV). Extraction multi-sources, transformation en star schema (1 table de faits + 4 dimensions), data quality checks, chargement SQLite via SQLAlchemy, orchestration Prefect, et conteneurisation Docker.

## Stack technique

| Couche | Outil |
|--------|-------|
| Extract | pandas, kagglehub |
| Transform | pandas (nettoyage, jointures, feature engineering) |
| Load | SQLAlchemy + SQLite |
| Qualite | Fonctions de validation custom |
| Orchestration | Prefect (DAG, retries, logging, schedule) |
| Analyse | Jupyter notebook + matplotlib |
| Conteneurisation | Docker, docker-compose |
| Logging | logging (structured, niveaux) |

## Architecture (Star Schema)

```
                    fact_sales
                    ────────────────────
                    order_id (PK)
                    customer_id (FK) ───► dim_customer
                    product_id (FK) ────► dim_product
                    seller_id (FK) ─────► dim_seller
                    order_date (FK) ────► dim_time
                    price
                    freight_value
                    delivery_days
                    review_score
                    is_delayed
                    payment_installments
```

## Structure

```
├── src/
│   ├── extract.py          # Telechargement + lecture des 9 CSV Olist
│   ├── transform.py        # Nettoyage, star schema, feature engineering
│   ├── load.py             # Chargement SQLite (SQLAlchemy)
│   ├── pipeline.py         # Orchestration Prefect
│   ├── quality.py          # Data quality checks
│   └── analysis.ipynb      # Insights business
├── data/
│   ├── raw/                # 9 CSV Olist bruts
│   └── olist_warehouse.db  # Base cible
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Etapes cles

1. **Extract** : Telecharger le dataset Olist via kagglehub, lire les 9 CSV
2. **Transform** : Nettoyer (doublons, nulls, types), construire le star schema (dimensions + faits), feature engineering (delivery_days, is_delayed)
3. **Load** : Creer les tables SQLite avec SQLAlchemy, inserer avec insert par lots
4. **Quality** : Valider les donnees chargees (row count, referential integrity, nulls)
5. **Orchestrate** : Construire un DAG Prefect (tasks avec retries, logging structured)
6. **Analyze** : Notebook Jupyter avec KPIs business (top produits, saisonnalite, delais livraison)

## Criteres de reussite

- [ ] Pipeline ETL fonctionnel (extract → transform → load)
- [ ] Star schema valide (1 faits, 4 dimensions)
- [ ] Data quality checks tous passants
- [ ] Orchestration Prefect fonctionnelle
- [ ] Analyse business dans un notebook
- [ ] Documentation completee dans Notion
- [ ] Commit pousse sur GitHub
