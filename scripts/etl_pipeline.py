# scripts/etl_pipeline.py

from extract import extract_all
from validation import validate_all
from upload_bigquery import load_to_bigquery
from transform import transform_all

def run_etl():
    """
    Run the complete ETL pipeline.
    """

    print("=" * 60)
    print("STARTING DIGITAL MARKETING ETL PIPELINE")
    print("=" * 60)

    # -----------------------
    # Extract
    # -----------------------
    campaigns_df, clicks_df, conversions_df = extract_all()

    # -----------------------
    # Validate
    # -----------------------
    validate_all(
        campaigns_df,
        clicks_df,
        conversions_df
    )

    # -----------------------
    # Transform
    # -----------------------
    campaigns_df, clicks_df, conversions_df = transform_all(
    campaigns_df,
    clicks_df,
    conversions_df
    )

    load_to_bigquery(
        df=campaigns_df,
        project_id="campaign-etl-pipeline",
        dataset_id="raw_marketing_data",
        table_id="campaigns"
    )

    load_to_bigquery(
        df=clicks_df,
        project_id="campaign-etl-pipeline",
        dataset_id="raw_marketing_data",
        table_id="clicks_impressions"
    )

    load_to_bigquery(
        df=conversions_df,
        project_id="campaign-etl-pipeline",
        dataset_id="raw_marketing_data",
        table_id="conversions"
    )
    
    print("\n" + "=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    run_etl()