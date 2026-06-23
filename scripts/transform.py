# scripts/transform.py

import pandas as pd
import numpy as np


# ============================================================
# CAMPAIGNS
# ============================================================

def transform_campaigns(campaigns_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform campaigns dataset.
    """

    print("\nTransforming campaigns...")

    campaigns_df = campaigns_df.copy()

    # Remove duplicate campaigns
    campaigns_df.drop_duplicates(inplace=True)

    # Convert dates
    campaigns_df["start_date"] = pd.to_datetime(campaigns_df["start_date"])
    campaigns_df["end_date"] = pd.to_datetime(campaigns_df["end_date"])

    # Budget datatype
    campaigns_df["budget"] = campaigns_df["budget"].astype(float)

    # Remove invalid budgets
    campaigns_df = campaigns_df[campaigns_df["budget"] > 0]

    campaigns_df.reset_index(drop=True, inplace=True)

    print(f"Campaign records: {len(campaigns_df):,}")

    return campaigns_df


# ============================================================
# CLICKS
# ============================================================

def transform_clicks(clicks_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform clicks dataset.
    """

    print("\nTransforming clicks...")

    clicks_df = clicks_df.copy()

    # Remove rows without campaign_id
    clicks_df = clicks_df.dropna(subset=["campaign_id"])

    # Timestamp
    clicks_df["timestamp"] = pd.to_datetime(clicks_df["timestamp"])

    # Fill missing browser
    clicks_df["browser"] = clicks_df["browser"].fillna("Unknown")

    # Fill missing operating system
    clicks_df["operating_system"] = clicks_df["operating_system"].fillna("Unknown")

    # Remove negative costs
    clicks_df = clicks_df[clicks_df["cost_usd"] >= 0]

    # Remove impossible impressions
    clicks_df = clicks_df[
        clicks_df["impressions_count"] > 0
    ]

    # Remove impossible clicks
    clicks_df = clicks_df[
        clicks_df["clicks_count"] >= 0
    ]

    # Clicks cannot exceed impressions
    clicks_df = clicks_df[
        clicks_df["clicks_count"] <= clicks_df["impressions_count"]
    ]

    # Data types
    clicks_df["impressions_count"] = clicks_df["impressions_count"].astype(int)
    clicks_df["clicks_count"] = clicks_df["clicks_count"].astype(int)
    clicks_df["cost_usd"] = clicks_df["cost_usd"].astype(float)

    clicks_df.reset_index(drop=True, inplace=True)

    print(f"Click records: {len(clicks_df):,}")

    return clicks_df


# ============================================================
# CONVERSIONS
# ============================================================

def transform_conversions(conversions_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform conversions dataset.
    """

    print("\nTransforming conversions...")

    conversions_df = conversions_df.copy()

    # Remove duplicates
    conversions_df.drop_duplicates(inplace=True)

    # Timestamp
    conversions_df["timestamp"] = pd.to_datetime(
        conversions_df["timestamp"]
    )

    # Revenue datatype
    conversions_df["revenue_usd"] = conversions_df[
        "revenue_usd"
    ].astype(float)

    # Remove negative revenue
    conversions_df = conversions_df[
        conversions_df["revenue_usd"] >= 0
    ]

    # Cap extreme revenue outliers
    upper_limit = conversions_df["revenue_usd"].quantile(0.99)

    conversions_df["revenue_usd"] = np.where(
        conversions_df["revenue_usd"] > upper_limit,
        upper_limit,
        conversions_df["revenue_usd"]
    )

    conversions_df.reset_index(drop=True, inplace=True)

    print(f"Conversion records: {len(conversions_df):,}")

    return conversions_df


# ============================================================
# TRANSFORM ALL
# ============================================================

def transform_all(
    campaigns_df: pd.DataFrame,
    clicks_df: pd.DataFrame,
    conversions_df: pd.DataFrame
):
    """
    Transform all datasets.
    """

    print("\n========== TRANSFORM PHASE ==========\n")

    campaigns_df = transform_campaigns(campaigns_df)

    clicks_df = transform_clicks(clicks_df)

    conversions_df = transform_conversions(conversions_df)

    print("\nTransformation completed successfully.\n")

    return (
        campaigns_df,
        clicks_df,
        conversions_df
    )





# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    from extract import extract_all

    campaigns, clicks, conversions = extract_all()

    campaigns, clicks, conversions = transform_all(
        campaigns,
        clicks,
        conversions
    )

    print(campaigns.head())

    print(clicks.head())

    print(conversions.head())