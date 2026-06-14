"""Module d'extraction des donnees Olist (Brazilian E-Commerce).

Telecharge le dataset depuis Kaggle via kagglehub et charge
les 9 fichiers CSV dans des DataFrames pandas.
"""

import logging
import os
import shutil
from pathlib import Path

import kagglehub
import pandas as pd

logger = logging.getLogger(__name__)

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
DATASET_PATH = "olistbr/brazilian-ecommerce"

CSV_FILES = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "product_category_name_translation.csv",
]


def download_dataset() -> Path:
    """Telecharge le dataset Olist via kagglehub et le copie dans data/raw/.

    Returns:
        Chemin du dossier contenant les CSV.

    Raises:
        RuntimeError: Si le telechargement echoue.
    """
    logger.info("Telechargement du dataset Olist depuis Kaggle...")
    try:
        kaggle_dir = kagglehub.dataset_download(DATASET_PATH)
        logger.info("Dataset telecharge dans : %s", kaggle_dir)
    except Exception as e:
        raise RuntimeError(f"Echec du telechargement Kaggle : {e}") from e

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Copie les CSV (evite de re-telecharger si deja presents)
    copied = 0
    for csv_file in CSV_FILES:
        src = Path(kaggle_dir) / csv_file
        dst = RAW_DIR / csv_file
        if not dst.exists() and src.exists():
            shutil.copy2(src, dst)
            copied += 1

    logger.info("%d/%d CSV copies dans %s", copied, len(CSV_FILES), RAW_DIR)
    return RAW_DIR


def extract() -> dict[str, pd.DataFrame]:
    """Extrait et charge tous les CSV du dataset Olist.

    Returns:
        Dictionnaire {nom_fichier: DataFrame}.
    """
    raw_dir = download_dataset()

    dataframes = {}
    for csv_file in CSV_FILES:
        path = raw_dir / csv_file
        if not path.exists():
            logger.warning("Fichier manquant : %s", csv_file)
            continue

        # Nom de la table = nom du fichier sans prefix/suffix
        table_name = (
            csv_file.replace("olist_", "").replace("_dataset", "").replace(".csv", "")
        )

        df = pd.read_csv(path)
        dataframes[table_name] = df
        logger.info(
            "  %s : %s lignes, %s colonnes", table_name, len(df), len(df.columns)
        )

    return dataframes


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    data = extract()
    print(f"\n{len(data)} DataFrames charges avec succes.")
