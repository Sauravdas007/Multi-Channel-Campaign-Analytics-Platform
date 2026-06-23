# scripts/extract.py

import os
import pandas as pd


def extract_campaigns(data_dir: str = "data") -> pd.DataFrame:
    """
    Read campaigns.csv into a Pandas DataFrame.

    Args:
        data_dir (str): Directory containing the CSV files.

    Returns:
        pd.DataFrame: Campaigns DataFrame.
    """
    file_path = os.path.join(data_dir, "campaigns.csv")

    print(f"Reading {file_path}...")

    campaigns_df = pd.read_csv(file_path)

    print(f"Loaded {len(campaigns_df):,} campaign records.")

    return campaigns_df


def extract_clicks(data_dir: str = "data") -> pd.DataFrame:
    """
    Read clicks_impressions.csv into a Pandas DataFrame.

    Args:
        data_dir (str): Directory containing the CSV files.

    Returns:
        pd.DataFrame: Clicks & Impressions DataFrame.
    """
    file_path = os.path.join(data_dir, "clicks_impressions.csv")

    print(f"Reading {file_path}...")

    clicks_df = pd.read_csv(file_path)

    print(f"Loaded {len(clicks_df):,} click/impression records.")

    return clicks_df


def extract_conversions(data_dir: str = "data") -> pd.DataFrame:
    """
    Read conversions.csv into a Pandas DataFrame.

    Args:
        data_dir (str): Directory containing the CSV files.

    Returns:
        pd.DataFrame: Conversions DataFrame.
    """
    file_path = os.path.join(data_dir, "conversions.csv")

    print(f"Reading {file_path}...")

    conversions_df = pd.read_csv(file_path)

    print(f"Loaded {len(conversions_df):,} conversion records.")

    return conversions_df


def extract_all(data_dir: str = "data"):
    """
    Read all datasets and return them.

    Args:
        data_dir (str): Directory containing the CSV files.

    Returns:
        tuple:
            campaigns_df,
            clicks_df,
            conversions_df
    """

    print("\n========== EXTRACT PHASE ==========\n")

    campaigns_df = extract_campaigns(data_dir)
    clicks_df = extract_clicks(data_dir)
    conversions_df = extract_conversions(data_dir)

    print("\nExtraction completed successfully.\n")

    return campaigns_df, clicks_df, conversions_df


if __name__ == "__main__":

    campaigns, clicks, conversions = extract_all()

    print("Campaigns Shape:", campaigns.shape)
    print("Clicks Shape:", clicks.shape)
    print("Conversions Shape:", conversions.shape)