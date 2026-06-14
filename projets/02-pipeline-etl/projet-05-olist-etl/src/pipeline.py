"""Pipeline ETL Olist — Orchestrateur maison.

Equivalent a un DAG Prefect mais sans serveur externe :
  - Retries automatiques avec backoff exponentiel
  - Logging structure avec duree de chaque etape
  - Gestion d'erreurs avec pipeline qui s'arrete proprement
"""

import logging
import time
import traceback
from datetime import datetime

from extract import extract
from load import load
from quality import run_quality_checks
from transform import transform

logger = logging.getLogger(__name__)

# Configuration
MAX_RETRIES = 2
RETRY_DELAY_BASE = 5  # secondes (backoff exponentiel : 5s, 25s, 125s)


class PipelineError(Exception):
    """Erreur fatale dans le pipeline."""

    pass


def run_step(name: str, func, *args, **kwargs):
    """Execute une etape du pipeline avec retry automatique.

    Args:
        name: Nom de l'etape (pour le logging).
        func: Fonction a executer.
        *args, **kwargs: Arguments passes a la fonction.

    Returns:
        La valeur de retour de func, ou leve PipelineError si tous les retries echouent.
    """
    last_error = None

    for attempt in range(MAX_RETRIES + 1):
        attempt_label = (
            f"[attempt {attempt + 1}/{MAX_RETRIES + 1}]" if attempt > 0 else ""
        )
        start = time.time()

        try:
            logger.info("▶ %s %s", name, attempt_label)
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            logger.info("✔ %s — %.1fs", name, elapsed)
            return result

        except Exception as e:
            elapsed = time.time() - start
            last_error = e
            logger.warning("✘ %s — %.1fs — %s: %s", name, elapsed, type(e).__name__, e)

            if attempt < MAX_RETRIES:
                delay = RETRY_DELAY_BASE ** (attempt + 1)
                logger.info("⏳ Retry dans %ds...", delay)
                time.sleep(delay)
            else:
                logger.error("✘ %s — ECHEC APRES %d TENTATIVES", name, MAX_RETRIES + 1)
                traceback.print_exc()

    raise PipelineError(f"Etape '{name}' echouee : {last_error}")


def run_pipeline():
    """Execute le pipeline ETL complet avec orchestration."""
    logger.info("=" * 60)
    logger.info(
        "🚀 PIPELINE ETL OLIST — %s", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    logger.info("=" * 60)

    pipeline_start = time.time()

    try:
        # Phase 1 : ETL
        logger.info("─" * 40)
        logger.info("📥 PHASE 1/2 : EXTRACT → TRANSFORM → LOAD")
        logger.info("─" * 40)

        raw_data = run_step("Extract (Kaggle → 9 DataFrames)", extract)
        star_schema = run_step("Transform (Star Schema)", transform, raw_data)
        run_step("Load (SQLite + Index)", load, star_schema)

        # Phase 2 : Quality
        logger.info("─" * 40)
        logger.info("🔍 PHASE 2/2 : DATA QUALITY")
        logger.info("─" * 40)

        run_step("Quality Checks (5 verifications)", run_quality_checks)

        # Succes
        total_elapsed = time.time() - pipeline_start
        logger.info("=" * 60)
        logger.info("🏁 PIPELINE TERMINE AVEC SUCCES — %.1fs", total_elapsed)
        logger.info("=" * 60)

    except PipelineError:
        total_elapsed = time.time() - pipeline_start
        logger.error("=" * 60)
        logger.error("💥 PIPELINE EN ECHEC — %.1fs", total_elapsed)
        logger.error("=" * 60)
        raise SystemExit(1)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
    )
    run_pipeline()
