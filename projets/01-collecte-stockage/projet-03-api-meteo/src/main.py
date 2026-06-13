"""Pipeline complet : collecte meteo via API + stockage SQL.

Utilisation :
    python src/main.py
"""

from fetch_weather import fetch_weather
from init_db import get_connection, init_database
from transform import transform_weather

# Villes a collecter (destinations touristiques)
CITIES = [
    "Paris",
    "Londres",
    "New York",
    "Tokyo",
    "Barcelone",
    "Dubai",
    "Sydney",
    "Rio de Janeiro",
    "Abidjan",
]


def insert_weather(cursor, data: dict):
    """Insere une ligne meteo dans la table weather."""
    cursor.execute(
        """
        INSERT OR IGNORE INTO weather (
            city, country, temperature, feels_like, temp_min, temp_max,
            pressure, humidity, wind_speed, wind_deg,
            weather_main, weather_description, clouds, visibility,
            sunrise, sunset, collected_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["city"],
            data["country"],
            data["temperature"],
            data["feels_like"],
            data["temp_min"],
            data["temp_max"],
            data["pressure"],
            data["humidity"],
            data["wind_speed"],
            data["wind_deg"],
            data["weather_main"],
            data["weather_description"],
            data["clouds"],
            data["visibility"],
            data["sunrise"],
            data["sunset"],
            data["collected_at"],
        ),
    )


def main():
    print("=== Pipeline Meteo → SQL ===\n")

    # 1. Initialisation de la base
    init_database()
    conn = get_connection()
    cursor = conn.cursor()

    # 2. Collecte + transformation + insertion pour chaque ville
    for city in CITIES:
        print(f"📡 Collecte : {city}...", end=" ")
        raw = fetch_weather(city)

        if raw is None:
            print("❌ Erreur API")
            continue

        transformed = transform_weather(raw)
        if transformed is None:
            print("❌ Donnees invalides")
            continue

        insert_weather(cursor, transformed)
        print(
            f"✅ {transformed['temperature']}°C, {transformed['weather_description']}"
        )

    conn.commit()

    # 3. Verification rapide
    cursor.execute("SELECT COUNT(*) FROM weather")
    count = cursor.fetchone()[0]
    print(f"\n📊 {count} enregistrements dans la base weather.db")

    conn.close()
    print("✅ Pipeline termine !")


if __name__ == "__main__":
    main()
