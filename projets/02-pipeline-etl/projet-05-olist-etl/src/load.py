"""Module de chargement du star schema Olist dans SQLite via SQLAlchemy."""

import logging
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent.parent / "data" / "olist_warehouse.db"

INDEXES = {
    "fact_sales": ["customer_key", "product_key", "seller_key", "time_key"],
    "dim_customer": ["city", "state"],
    "dim_product": ["category_name_en"],
    "dim_time": ["year", "month"],
}


def create_tables(engine) -> None:
    """Cree les tables du star schema avec les bonnes colonnes."""
    with engine.begin() as conn:
        # Dimensions
        conn.execute(
            text("""
            CREATE TABLE IF NOT EXISTS dim_customer (
                customer_key TEXT PRIMARY KEY,
                customer_natural_key TEXT,
                zip_code INTEGER,
                city TEXT,
                state TEXT
            )
        """)
        )
        conn.execute(
            text("""
            CREATE TABLE IF NOT EXISTS dim_product (
                product_key TEXT PRIMARY KEY,
                name_length INTEGER,
                desc_length INTEGER,
                photos_qty INTEGER,
                category_name_pt TEXT,
                category_name_en TEXT
            )
        """)
        )
        conn.execute(
            text("""
            CREATE TABLE IF NOT EXISTS dim_seller (
                seller_key TEXT PRIMARY KEY,
                zip_code INTEGER,
                city TEXT,
                state TEXT
            )
        """)
        )
        conn.execute(
            text("""
            CREATE TABLE IF NOT EXISTS dim_time (
                time_key INTEGER PRIMARY KEY,
                date TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                day_of_week TEXT,
                quarter INTEGER,
                is_weekend INTEGER
            )
        """)
        )
        # Table de faits
        conn.execute(
            text("""
            CREATE TABLE IF NOT EXISTS fact_sales (
                rowid INTEGER PRIMARY KEY AUTOINCREMENT,
                order_key TEXT,
                customer_key TEXT REFERENCES dim_customer(customer_key),
                product_key TEXT REFERENCES dim_product(product_key),
                seller_key TEXT REFERENCES dim_seller(seller_key),
                time_key INTEGER REFERENCES dim_time(time_key),
                unit_price REAL,
                freight REAL,
                total_payment REAL,
                payment_installments INTEGER,
                avg_review_score REAL,
                delivery_days INTEGER,
                is_delayed INTEGER,
                order_status TEXT
            )
        """)
        )
    logger.info("Tables creees avec contraintes FK.")


def create_indexes(engine) -> None:
    """Cree les index sur les colonnes frequemment interrogees."""
    with engine.begin() as conn:
        for table, columns in INDEXES.items():
            for col in columns:
                idx_name = f"idx_{table}_{col}"
                conn.execute(
                    text(f"CREATE INDEX IF NOT EXISTS {idx_name} ON {table}({col})")
                )
    logger.info("Index crees pour les requetes analytiques.")


def load(star_schema: dict[str, pd.DataFrame]) -> None:
    """Charge les DataFrames du star schema dans SQLite.

    Args:
        star_schema: Dictionnaire {nom_table: DataFrame}.
    """
    engine = create_engine(f"sqlite:///{DB_PATH}")

    create_tables(engine)

    # Ordre de chargement : dimensions d'abord (contraintes FK)
    load_order = ["dim_customer", "dim_product", "dim_seller", "dim_time", "fact_sales"]

    for table in load_order:
        if table not in star_schema:
            logger.warning("Table manquante : %s", table)
            continue

        df = star_schema[table]

        # Nettoie les time_key pour SQLite (int ou str)
        if table == "dim_time":
            df["time_key"] = df["time_key"].astype(int)
        if table == "fact_sales":
            df["time_key"] = df["time_key"].astype(int)

        # Supprime la table existante et reinsere
        df.to_sql(table, engine, if_exists="replace", index=False)
        logger.info("  %s : %s lignes chargees", table, len(df))

    create_indexes(engine)

    # Verification
    with engine.begin() as conn:
        for table in load_order:
            count = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
            logger.info("  Verification : %s → %s lignes", table, count)


if __name__ == "__main__":
    from extract import extract
    from transform import transform

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    raw = extract()
    star = transform(raw)
    load(star)
