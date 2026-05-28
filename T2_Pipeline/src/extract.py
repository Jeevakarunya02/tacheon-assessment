import requests
import logging
from transform import transform_weather_data
from load_bigquery import load_to_bigquery

logging.basicConfig(level=logging.INFO)

API_URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.08,
    "longitude": 80.27,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

try:
    logging.info("Fetching weather data from API...")

    response = requests.get(API_URL, params=params)

    response.raise_for_status()

    data = response.json()

    logging.info("API data fetched successfully")

    df = transform_weather_data(data)

    print(df)

    load_to_bigquery(df)

except requests.exceptions.RequestException as e:
    logging.error(f"API request failed: {e}")