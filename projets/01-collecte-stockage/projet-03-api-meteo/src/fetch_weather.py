"""Module de connexion a l'API OpenWeather."""

import os

import requests
from dotenv import load_dotenv

# Charge les variables du fichier .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str) -> dict | None:
    """Recupere les donnees meteo d'une ville via l'API OpenWeather.

    Args:
        city: Nom de la ville (ex: "Paris")

    Returns:
        Dictionnaire JSON des donnees meteo, ou None si erreur.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Temperature en Celsius
        "lang": "fr",  # Descriptions en francais
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # Leve une exception si HTTP != 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur API pour '{city}': {e}")
        return None


if __name__ == "__main__":
    # Test rapide
    data = fetch_weather("Paris")
    if data:
        print(
            f"🌍 {data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
        )
