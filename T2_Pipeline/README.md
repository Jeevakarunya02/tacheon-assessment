# Task 2 - Weather Data Pipeline

## Overview

This project implements a simple end-to-end ETL pipeline using the Open-Meteo public API and Google BigQuery.

The pipeline extracts weather data, transforms it into a structured format using pandas, and loads it into BigQuery for analytical querying.

---

## Pipeline Flow

Open-Meteo API
→ Extract Layer
→ Transformation Layer
→ Pandas DataFrame
→ BigQuery
→ SQL Analysis

---

## Technologies Used

- Python
- Pandas
- Requests
- Google BigQuery
- SQL

---

## Files Description

### src/extract.py
Handles API data extraction and orchestrates pipeline execution.

### src/transform.py
Transforms nested JSON into a structured pandas DataFrame and creates derived analytical fields.

### src/load_bigquery.py
Uploads transformed dataframe into BigQuery.

### sql/weather_analysis.sql
SQL query for analyzing hot weather conditions.

---

## Derived Field

The pipeline creates a derived boolean column:

- `is_hot_day`

This field becomes `True` when the temperature exceeds 35°C.

---

## BigQuery Table

Dataset:
`weather_data`

Table:
`weather_metrics`

---

## Sample Analysis

The SQL query filters days where temperature exceeds 35°C and sorts results by temperature.