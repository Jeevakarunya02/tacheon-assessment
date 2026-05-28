from google.cloud import bigquery
from google.oauth2 import service_account
import logging

logging.basicConfig(level=logging.INFO)

PROJECT_ID = "velvety-tangent-393618"
DATASET_ID = "weather_data"
TABLE_ID = "weather_metrics"

KEY_PATH = "T2_Pipeline/service_account.json"


def load_to_bigquery(df):

    logging.info("Connecting to BigQuery...")

    credentials = service_account.Credentials.from_service_account_file(
        KEY_PATH
    )

    client = bigquery.Client(
        credentials=credentials,
        project=PROJECT_ID
    )

    table_reference = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    job = client.load_table_from_dataframe(
        df,
        table_reference
    )

    job.result()

    logging.info(f"Data loaded successfully into {table_reference}")