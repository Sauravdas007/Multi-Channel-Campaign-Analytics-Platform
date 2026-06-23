# scripts/load_bigquery.py

from google.cloud import bigquery
import pandas as pd


def load_to_bigquery(
    df: pd.DataFrame,
    project_id: str,
    dataset_id: str,
    table_id: str,
    credentials_path: str = "gcp_key.json",
) -> None:
    """
    Load a Pandas DataFrame into a BigQuery table.

    Args:
        df: Final transformed DataFrame.
        project_id: GCP Project ID.
        dataset_id: BigQuery Dataset ID.
        table_id: BigQuery Table ID.
        credentials_path: Path to the service account JSON key.
    """

    print("\n========== LOAD PHASE ==========\n")

    if df.empty:
        print("DataFrame is empty. Nothing to upload.")
        return

    # Authenticate
    client = bigquery.Client.from_service_account_json(
        credentials_path,
        project=project_id
    )

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=True,
    )

    print(f"Uploading {len(df):,} rows to BigQuery...")

    load_job = client.load_table_from_dataframe(
        df,
        table_ref,
        job_config=job_config
    )

    load_job.result()

    table = client.get_table(table_ref)

    print("\nUpload completed successfully!")
    print(f"Project : {project_id}")
    print(f"Dataset : {dataset_id}")
    print(f"Table    : {table_id}")
    print(f"Rows     : {table.num_rows:,}")