"""Module de transformation et nettoyage des donnees OpenWeather.

Le JSON brut d'OpenWeather est imbrique. On extrait les champs utiles
et on les aplatit en une structure plate prete pour la base SQL.
"""

from datetime import datetime


def transform_weather(raw_data: dict) -> dict | None:
    """Transforme les donnees brutes d'OpenWeather en dictionnaire plat.

    Args:
        raw_data: Donnees JSON brutes de l'API OpenWeather.

    Returns:
        Dictionnaire avec les champs nettoyes, ou None si donnees invalides.
    """
    if not raw_data or raw_data.get("cod") != 200:
        return None

    # Extraction securisee avec .get() pour gerer les valeurs manquantes
    main = raw_data.get("main", {})
    wind = raw_data.get("wind", {})
    weather = raw_data.get("weather", [{}])[0]  # Premier element de la liste

    transformed = {
        "city": raw_data.get("name"),
        "country": raw_data.get("sys", {}).get("country"),
        "temperature": main.get("temp"),
        "feels_like": main.get("feels_like"),
        "temp_min": main.get("temp_min"),
        "temp_max": main.get("temp_max"),
        "pressure": main.get("pressure"),
        "humidity": main.get("humidity"),
        "wind_speed": wind.get("speed"),
        "wind_deg": wind.get("deg"),
        "weather_main": weather.get("main"),
        "weather_description": weather.get("description"),
        "clouds": raw_data.get("clouds", {}).get("all"),
        "visibility": raw_data.get("visibility"),
        "sunrise": _ts_to_time(raw_data.get("sys", {}).get("sunrise")),
        "sunset": _ts_to_time(raw_data.get("sys", {}).get("sunset")),
        "collected_at": datetime.now().isoformat(),  # Horodatage de collecte
    }

    # Remplace les chaines vides par None (coherence avec SQL)
    for key, value in transformed.items():
        if value == "":
            transformed[key] = None

    return transformed


def _ts_to_time(timestamp: int | None) -> str | None:
    """Convertit un timestamp Unix en heure HH:MM:SS."""
    if timestamp is None:
        return None
    return datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")


if __name__ == "__main__":
    # Test avec des donnees simulees
    sample = {
        "coord": {"lon": 2.3488, "lat": 48.8534},
        "weather": [
            {"id": 804, "main": "Clouds", "description": "nuageux", "icon": "04d"}
        ],
        "main": {
            "temp": 17.56,
            "feels_like": 16.8,
            "temp_min": 15.2,
            "temp_max": 19.1,
            "pressure": 1012,
            "humidity": 72,
        },
        "visibility": 10000,
        "wind": {"speed": 4.5, "deg": 320},
        "clouds": {"all": 85},
        "dt": 1718112000,
        "sys": {
            "country": "FR",
            "sunrise": 1718079623,
            "sunset": 1718136147,
        },
        "name": "Paris",
        "cod": 200,
    }

    result = transform_weather(sample)
    for k, v in result.items():
        print(f"  {k}: {v}")
