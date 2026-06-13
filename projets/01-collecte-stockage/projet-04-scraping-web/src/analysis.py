"""Analyse des livres scrapes - graphiques sans Jupyter."""

import sqlite3

import matplotlib

matplotlib.use("Agg")  # Mode sans interface graphique
import matplotlib.pyplot as plt

# Connexion a la base
conn = sqlite3.connect("../data/books.db")
cursor = conn.cursor()

# Recuperation des donnees
cursor.execute("SELECT price FROM books")
prices = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT rating FROM books")
ratings = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT in_stock FROM books")
stocks = [row[0] for row in cursor.fetchall()]

conn.close()

# --- 1. Distribution des prix ---
plt.figure(figsize=(10, 5))
plt.hist(prices, bins=20, color="steelblue", edgecolor="white")
plt.axvline(
    sum(prices) / len(prices),
    color="red",
    linestyle="--",
    label=f"Moyenne: £{sum(prices) / len(prices):.2f}",
)
plt.xlabel("Prix (£)")
plt.ylabel("Nombre de livres")
plt.title("Distribution des prix")
plt.legend()
plt.tight_layout()
plt.savefig("../data/prix_distribution.png", dpi=100)
plt.close()
print(
    f"Prix min: £{min(prices):.2f} | max: £{max(prices):.2f} | moyen: £{sum(prices) / len(prices):.2f}"
)

# --- 2. Repartition des notes ---
rating_counts = {r: ratings.count(r) for r in sorted(set(ratings))}
colors = ["gray", "tomato", "orange", "gold", "limegreen"]

plt.figure(figsize=(8, 5))
bars = plt.bar([f"{k}★" for k in rating_counts], rating_counts.values(), color=colors)
for bar, val in zip(bars, rating_counts.values()):
    plt.text(
        bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3, str(val), ha="center"
    )
plt.xlabel("Note")
plt.ylabel("Nombre de livres")
plt.title("Repartition des notes")
plt.tight_layout()
plt.savefig("../data/ratings_distribution.png", dpi=100)
plt.close()
print(f"Notes: {rating_counts}")

# --- 3. Disponibilite ---
in_stock = stocks.count(1)
out_stock = stocks.count(0)

plt.figure(figsize=(6, 6))
plt.pie(
    [in_stock, out_stock],
    labels=["En stock", "Rupture"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["limegreen", "tomato"],
)
plt.title("Disponibilite des livres")
plt.tight_layout()
plt.savefig("../data/stock_pie.png", dpi=100)
plt.close()
print(f"En stock: {in_stock} | Rupture: {out_stock}")

# --- 4. Prix moyen par note ---
price_by_rating = {}
for p, r in zip(prices, ratings):
    price_by_rating.setdefault(r, []).append(p)

mean_prices = {r: sum(v) / len(v) for r, v in sorted(price_by_rating.items())}

plt.figure(figsize=(8, 5))
plt.bar(
    [f"{k}★" for k in mean_prices],
    mean_prices.values(),
    color=["gray", "tomato", "orange", "gold", "limegreen"],
)
plt.xlabel("Note")
plt.ylabel("Prix moyen (£)")
plt.title("Prix moyen par note")
plt.tight_layout()
plt.savefig("../data/prix_par_note.png", dpi=100)
plt.close()
for r, p in mean_prices.items():
    print(f"{r}★: £{p:.2f}")

print("\n✅ Graphiques sauvegardes dans data/")
