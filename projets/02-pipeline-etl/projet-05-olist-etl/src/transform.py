"""Module de transformation Olist : nettoyage, star schema, feature engineering.

Pipeline :
  1. Nettoyage (doublons, nulls, types)
  2. Construction des 4 dimensions
  3. Construction de la table de faits
  4. Feature engineering (delivery_days, is_delayed)
"""

import logging
from datetime import datetime

import pandas as pd

logger = logging.getLogger(__name__)

# Colonnes a supprimer dans les dimensions (gardees uniquement dans les faits)
PRODUCT_COLS_IN_FACTS = {
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm",
}
ORDER_COLS_IN_FACTS = {
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "order_status",
}


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie la table orders."""
    df = df.copy()
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["order_approved_at"] = pd.to_datetime(df["order_approved_at"])
    df["order_delivered_carrier_date"] = pd.to_datetime(
        df["order_delivered_carrier_date"]
    )
    df["order_delivered_customer_date"] = pd.to_datetime(
        df["order_delivered_customer_date"]
    )
    df["order_estimated_delivery_date"] = pd.to_datetime(
        df["order_estimated_delivery_date"]
    )
    logger.info("  orders nettoyees : %s lignes", len(df))
    return df


def clean_order_items(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie order_items : supprime les lignes sans produit."""
    df = df.copy()
    df = df.dropna(subset=["product_id"])
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["freight_value"] = pd.to_numeric(df["freight_value"], errors="coerce")
    logger.info("  order_items nettoyees : %s lignes", len(df))
    return df


def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie la table products."""
    df = df.copy()
    df["product_name_lenght"] = pd.to_numeric(
        df["product_name_lenght"], errors="coerce"
    )
    df["product_description_lenght"] = pd.to_numeric(
        df["product_description_lenght"], errors="coerce"
    )
    df["product_photos_qty"] = pd.to_numeric(df["product_photos_qty"], errors="coerce")
    for col in [
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.drop_duplicates(subset=["product_id"])
    logger.info("  products nettoyes : %s lignes", len(df))
    return df


def build_dim_customer(customers_df: pd.DataFrame) -> pd.DataFrame:
    """Construit la dimension client."""
    df = customers_df.copy()
    df = df.rename(
        columns={
            "customer_id": "customer_key",
            "customer_unique_id": "customer_natural_key",
            "customer_zip_code_prefix": "zip_code",
            "customer_city": "city",
            "customer_state": "state",
        }
    )
    df = df[["customer_key", "customer_natural_key", "zip_code", "city", "state"]]
    df = df.drop_duplicates(subset=["customer_key"])
    logger.info("  dim_customer : %s lignes", len(df))
    return df


def build_dim_product(
    products_df: pd.DataFrame, category_df: pd.DataFrame
) -> pd.DataFrame:
    """Construit la dimension produit avec traduction des categories."""
    df = products_df.copy()
    # Merge avec la traduction des categories
    df = df.merge(category_df, on="product_category_name", how="left")
    df = df.rename(
        columns={
            "product_id": "product_key",
            "product_name_lenght": "name_length",
            "product_description_lenght": "desc_length",
            "product_photos_qty": "photos_qty",
            "product_category_name": "category_name_pt",
            "product_category_name_english": "category_name_en",
        }
    )
    cols = [
        "product_key",
        "name_length",
        "desc_length",
        "photos_qty",
        "category_name_pt",
        "category_name_en",
    ]
    df = df[cols].drop_duplicates(subset=["product_key"])
    logger.info("  dim_product : %s lignes", len(df))
    return df


def build_dim_seller(sellers_df: pd.DataFrame) -> pd.DataFrame:
    """Construit la dimension vendeur."""
    df = sellers_df.copy()
    df = df.rename(
        columns={
            "seller_id": "seller_key",
            "seller_zip_code_prefix": "zip_code",
            "seller_city": "city",
            "seller_state": "state",
        }
    )
    df = df[["seller_key", "zip_code", "city", "state"]].drop_duplicates(
        subset=["seller_key"]
    )
    logger.info("  dim_seller : %s lignes", len(df))
    return df


def build_dim_time(orders_df: pd.DataFrame) -> pd.DataFrame:
    """Construit la dimension temps a partir des dates de commande."""
    dates = orders_df["order_purchase_timestamp"].dropna().unique()
    df = pd.DataFrame({"date": pd.to_datetime(dates).normalize()})
    df = df.drop_duplicates(subset=["date"])
    df["time_key"] = df["date"].dt.strftime("%Y%m%d").astype(int)
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.day_name()
    df["quarter"] = df["date"].dt.quarter
    df["is_weekend"] = df["date"].dt.dayofweek.isin([5, 6]).astype(int)
    df = df[
        [
            "time_key",
            "date",
            "year",
            "month",
            "day",
            "day_of_week",
            "quarter",
            "is_weekend",
        ]
    ]
    logger.info("  dim_time : %s dates", len(df))
    return df


def build_fact_sales(
    orders_df: pd.DataFrame,
    items_df: pd.DataFrame,
    payments_df: pd.DataFrame,
    reviews_df: pd.DataFrame,
) -> pd.DataFrame:
    """Construit la table de faits : une ligne = un item de commande enrichi.

    Joint orders + items + payments + reviews.
    """
    # Jointure orders → items
    facts = items_df.merge(
        orders_df[
            [
                "order_id",
                "customer_id",
                "order_purchase_timestamp",
                "order_delivered_customer_date",
                "order_estimated_delivery_date",
                "order_status",
            ]
        ],
        on="order_id",
        how="left",
    )

    # Agregation des paiements (total par commande)
    pay_agg = (
        payments_df.groupby("order_id")
        .agg(
            total_payment=("payment_value", "sum"),
            payment_installments=("payment_installments", "max"),
        )
        .reset_index()
    )
    facts = facts.merge(pay_agg, on="order_id", how="left")

    # Jointure reviews (score moyen par commande)
    rev_agg = reviews_df.groupby("order_id")["review_score"].mean().reset_index()
    rev_agg = rev_agg.rename(columns={"review_score": "avg_review_score"})
    facts = facts.merge(rev_agg, on="order_id", how="left")

    # Feature engineering
    facts["delivery_days"] = (
        facts["order_delivered_customer_date"] - facts["order_purchase_timestamp"]
    ).dt.days
    facts["is_delayed"] = (
        facts["order_delivered_customer_date"] > facts["order_estimated_delivery_date"]
    ).astype(int)

    # Time key depuis la date de commande
    facts["time_key"] = (
        facts["order_purchase_timestamp"].dt.strftime("%Y%m%d").astype(int)
    )

    # Renommage FK
    facts = facts.rename(
        columns={
            "order_id": "order_key",
            "product_id": "product_key",
            "seller_id": "seller_key",
            "customer_id": "customer_key",
            "price": "unit_price",
            "freight_value": "freight",
        }
    )

    # Selection des colonnes finales
    cols = [
        "order_key",
        "customer_key",
        "product_key",
        "seller_key",
        "time_key",
        "unit_price",
        "freight",
        "total_payment",
        "payment_installments",
        "avg_review_score",
        "delivery_days",
        "is_delayed",
        "order_status",
    ]
    facts = facts[cols]

    # Suppression des lignes sans customer/product/seller
    facts = facts.dropna(
        subset=["customer_key", "product_key", "seller_key", "time_key"]
    )

    logger.info("  fact_sales : %s lignes", len(facts))
    return facts


def transform(raw_data: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """Pipeline de transformation complet.

    Args:
        raw_data: DataFrames bruts issus de extract().

    Returns:
        Dictionnaire avec les 5 tables du star schema.
    """
    logger.info("Transformation des donnees Olist...")

    # Nettoyage
    logger.info("1/4 Nettoyage...")
    orders = clean_orders(raw_data["orders"])
    items = clean_order_items(raw_data["order_items"])
    products = clean_products(raw_data["products"])

    # Dimensions
    logger.info("2/4 Construction des dimensions...")
    dim_customer = build_dim_customer(raw_data["customers"])
    dim_product = build_dim_product(
        products, raw_data["product_category_name_translation"]
    )
    dim_seller = build_dim_seller(raw_data["sellers"])
    dim_time = build_dim_time(orders)

    # Faits
    logger.info("3/4 Construction de la table de faits...")
    payments = raw_data["order_payments"]
    reviews = raw_data["order_reviews"]
    fact_sales = build_fact_sales(orders, items, payments, reviews)

    logger.info("4/4 Star schema construit.")
    return {
        "dim_customer": dim_customer,
        "dim_product": dim_product,
        "dim_seller": dim_seller,
        "dim_time": dim_time,
        "fact_sales": fact_sales,
    }


if __name__ == "__main__":
    from extract import extract

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    raw = extract()
    star = transform(raw)
    for name, df in star.items():
        print(f"  {name}: {len(df)} lignes, {len(df.columns)} colonnes")
