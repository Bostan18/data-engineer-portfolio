"""Module de data quality checks pour le pipeline Olist."""

import logging
from pathlib import Path

from sqlalchemy import create_engine, text

logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent.parent / "data" / "olist_warehouse.db"


class DataQualityError(Exception):
    """Exception levee si un check de qualite echoue."""

    pass


def check_row_count(conn, expected: dict[str, int]) -> None:
    logger.info("1/5 Row count check...")
    for table, expected_count in expected.items():
        actual = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
        if actual != expected_count:
            raise DataQualityError(
                f"{table}: attendu {expected_count}, obtenu {actual}"
            )
    logger.info("  OK : %d tables avec le bon nombre de lignes", len(expected))


def check_no_nulls(conn) -> None:
    logger.info("2/5 Null check (colonnes critiques)...")
    checks = {
        "dim_customer": "customer_key",
        "dim_product": "product_key",
        "dim_seller": "seller_key",
        "dim_time": "time_key",
        "fact_sales": "order_key, customer_key, product_key, seller_key, time_key",
    }
    for table, columns in checks.items():
        for col in columns.split(", "):
            count = conn.execute(
                text(f"SELECT COUNT(*) FROM {table} WHERE {col} IS NULL")
            ).scalar()
            if count > 0:
                raise DataQualityError(f"{table}.{col}: {count} NULLs trouves")
    logger.info("  OK : 0 NULLs sur les colonnes critiques")


def check_referential_integrity(conn) -> None:
    logger.info("3/5 Referential integrity check...")
    refs = {
        "customer_key": "dim_customer",
        "product_key": "dim_product",
        "seller_key": "dim_seller",
        "time_key": "dim_time",
    }
    for fk, dim_table in refs.items():
        orphan_count = conn.execute(
            text(f"""
            SELECT COUNT(DISTINCT f.{fk}) FROM fact_sales f
            LEFT JOIN {dim_table} d ON f.{fk} = d.{fk}
            WHERE d.{fk} IS NULL
        """)
        ).scalar()
        if orphan_count > 0:
            raise DataQualityError(f"Integrite FK {fk}: {orphan_count} orphelins")
    logger.info("  OK : toutes les FK sont valides")


def check_business_rules(conn) -> None:
    logger.info("4/5 Business rules check...")
    bad_prices = conn.execute(
        text("SELECT COUNT(*) FROM fact_sales WHERE unit_price <= 0")
    ).scalar()
    if bad_prices > 0:
        raise DataQualityError(
            f"Prix invalides: {bad_prices} lignes avec unit_price <= 0"
        )
    bad_scores = conn.execute(
        text(
            "SELECT COUNT(*) FROM fact_sales WHERE avg_review_score < 1 OR avg_review_score > 5"
        )
    ).scalar()
    if bad_scores > 0:
        raise DataQualityError(f"Scores invalides: {bad_scores} lignes hors [1-5]")
    bad_delivery = conn.execute(
        text("SELECT COUNT(*) FROM fact_sales WHERE delivery_days < 0")
    ).scalar()
    if bad_delivery > 0:
        raise DataQualityError(f"Livraison negative: {bad_delivery} lignes")
    logger.info("  OK : regles metier respectees")


def check_duplicates(conn) -> None:
    logger.info("5/5 Duplicate check...")
    pk_cols = {
        "dim_customer": "customer_key",
        "dim_product": "product_key",
        "dim_seller": "seller_key",
        "dim_time": "time_key",
    }
    for table, pk in pk_cols.items():
        dupes = conn.execute(
            text(
                f"SELECT {pk}, COUNT(*) FROM {table} GROUP BY {pk} HAVING COUNT(*) > 1"
            )
        ).fetchall()
        if dupes:
            raise DataQualityError(f"{table}: {len(dupes)} doublons sur {pk}")
    logger.info("  OK : 0 doublons sur les cles primaires")


def run_quality_checks() -> None:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Base introuvable : {DB_PATH}")

    engine = create_engine(f"sqlite:///{DB_PATH}")
    conn = engine.connect()

    expected_counts = {
        "dim_customer": 99441,
        "dim_product": 32951,
        "dim_seller": 3095,
        "dim_time": 634,
        "fact_sales": 112650,
    }

    checks = [
        lambda: check_row_count(conn, expected_counts),
        lambda: check_no_nulls(conn),
        lambda: check_referential_integrity(conn),
        lambda: check_business_rules(conn),
        lambda: check_duplicates(conn),
    ]

    failures = 0
    for check in checks:
        try:
            check()
        except DataQualityError as e:
            logger.error("  ❌ %s", e)
            failures += 1

    conn.close()

    if failures == 0:
        logger.info("✅ Tous les checks de qualite sont passes !")
    else:
        logger.error("❌ %d check(s) en echec", failures)
        raise DataQualityError(f"{failures} data quality checks ont echoue")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    run_quality_checks()
