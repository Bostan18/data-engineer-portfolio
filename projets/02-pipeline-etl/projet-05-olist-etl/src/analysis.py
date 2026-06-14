"""Analyse Olist — KPIs business (standalone)."""

import sqlite3
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

DB_PATH = Path(__file__).parent.parent / "data" / "olist_warehouse.db"
OUT_DIR = Path(__file__).parent.parent / "data"

conn = sqlite3.connect(str(DB_PATH))
df = pd.read_sql_query(
    """
    SELECT f.*, d.year, d.month, d.day_of_week, d.is_weekend,
           c.state as customer_state,
           p.category_name_en as category
    FROM fact_sales f
    JOIN dim_time d ON f.time_key = d.time_key
    JOIN dim_customer c ON f.customer_key = c.customer_key
    JOIN dim_product p ON f.product_key = p.product_key
""",
    conn,
)
conn.close()

print(f"{len(df):,} lignes chargees\n")

# --- 1. CA mensuel ---
df["year_month"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2)
monthly = df.groupby("year_month")["total_payment"].sum()

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(monthly.index, monthly.values, marker="o", linewidth=1.5, markersize=3)
ax.set_title("CA mensuel")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x / 1e6:.1f}M"))
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.savefig(OUT_DIR / "kpi_ca_mensuel.png")
plt.close()
print(f"CA total : R$ {monthly.sum():,.0f}")

# --- 2. Top 10 categories ---
top_cat = (
    df.groupby("category")["total_payment"].sum().sort_values(ascending=False).head(10)
)
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(top_cat.index[::-1], top_cat.values[::-1], color="steelblue")
for bar, val in zip(bars, top_cat.values[::-1]):
    ax.text(
        bar.get_width() + 2000,
        bar.get_y() + bar.get_height() / 2,
        f"R$ {val:,.0f}",
        va="center",
        fontsize=9,
    )
ax.set_title("Top 10 categories par CA")
plt.tight_layout()
plt.savefig(OUT_DIR / "kpi_top_categories.png")
plt.close()

# --- 3. Delai livraison ---
delivery = df.groupby("customer_state")["delivery_days"].mean().sort_values().head(15)
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(delivery.index, delivery.values, color="coral")
ax.axhline(
    df["delivery_days"].mean(),
    color="red",
    linestyle="--",
    label=f"National: {df['delivery_days'].mean():.0f}j",
)
ax.set_title("Delai livraison par etat (15 plus rapides)")
ax.legend()
plt.tight_layout()
plt.savefig(OUT_DIR / "kpi_delivery_state.png")
plt.close()
print(
    f"Delai moyen : {df['delivery_days'].mean():.0f} jours | Retard : {df['is_delayed'].mean() * 100:.1f}%"
)

# --- 4. Notes ---
scores = df["avg_review_score"].value_counts().sort_index()
colors = ["gray", "tomato", "orange", "gold", "limegreen"]
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar([f"{int(k)}*" for k in scores.index], scores.values, color=colors)
for bar, val in zip(bars, scores.values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 500,
        f"{val:,}",
        ha="center",
    )
ax.set_title("Notes clients")
plt.tight_layout()
plt.savefig(OUT_DIR / "kpi_reviews.png")
plt.close()
print(f"Note moyenne : {df['avg_review_score'].mean():.2f}/5")

# --- 5. CA par jour de la semaine ---
dow_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
dow = df.groupby("day_of_week")["total_payment"].sum().reindex(dow_order)
dow_colors = [
    "skyblue" if d not in ["Saturday", "Sunday"] else "lightcoral" for d in dow_order
]
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(dow.index, dow.values, color=dow_colors)
ax.set_title("CA par jour de la semaine")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x / 1e6:.1f}M"))
plt.tight_layout()
plt.savefig(OUT_DIR / "kpi_ca_dow.png")
plt.close()

# --- 6. Prix par categorie ---
cat_price = (
    df.groupby("category")["unit_price"].mean().sort_values(ascending=False).head(10)
)
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(cat_price.index[::-1], cat_price.values[::-1], color="mediumseagreen")
for bar, val in zip(bars, cat_price.values[::-1]):
    ax.text(
        bar.get_width() + 5,
        bar.get_y() + bar.get_height() / 2,
        f"R$ {val:.0f}",
        va="center",
    )
ax.set_title("Prix moyen par categorie (Top 10)")
plt.tight_layout()
plt.savefig(OUT_DIR / "kpi_price_category.png")
plt.close()

print("\n6 graphiques sauvegardes dans data/")
