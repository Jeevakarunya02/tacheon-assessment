import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def transform_weather_data(api_data):

    logging.info("Transforming API data...")

    current_data = api_data["current"]

    transformed_data = {
        "time": current_data["time"],
        "temperature_celsius": current_data["temperature_2m"],
        "humidity_percent": current_data["relative_humidity_2m"],
        "wind_speed_kmh": current_data["wind_speed_10m"]
    }

    df = pd.DataFrame([transformed_data])

    # Derived field
    df["is_hot_day"] = df["temperature_celsius"] > 35

    logging.info("Transformation completed")

    return df