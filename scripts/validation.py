# scripts/validation.py

import pandas as pd


def check_missing_values(df: pd.DataFrame, name: str) -> None:
    """
    Check for missing values in a DataFrame.
    """
    missing = df.isnull().sum()

    if missing.sum() == 0:
        print(f"✅ {name}: No missing values found.")
    else:
        print(f"\n⚠️ {name}: Missing Values")
        print(missing[missing > 0])


def check_duplicates(df: pd.DataFrame, name: str) -> None:
    """
    Check for duplicate rows.
    """
    duplicates = df.duplicated().sum()

    if duplicates == 0:
        print(f"✅ {name}: No duplicate rows found.")
    else:
        print(f"⚠️ {name}: {duplicates} duplicate rows found.")


def validate_campaigns(df: pd.DataFrame) -> None:
    """
    Validate campaigns dataset.
    """
    print("\n========== Validating Campaigns ==========")

    check_missing_values(df, "Campaigns")
    check_duplicates(df, "Campaigns")


def validate_clicks(df: pd.DataFrame) -> None:
    """
    Validate clicks/impressions dataset.
    """
    print("\n========== Validating Clicks & Impressions ==========")

    check_missing_values(df, "Clicks & Impressions")
    check_duplicates(df, "Clicks & Impressions")


def validate_conversions(df: pd.DataFrame) -> None:
    """
    Validate conversions dataset.
    """
    print("\n========== Validating Conversions ==========")

    check_missing_values(df, "Conversions")
    check_duplicates(df, "Conversions")


def validate_all(campaigns_df, clicks_df, conversions_df) -> None:
    """
    Run validation on all datasets.
    """
    print("\n================ DATA VALIDATION ================\n")

    validate_campaigns(campaigns_df)
    validate_clicks(clicks_df)
    validate_conversions(conversions_df)

    print("\n✅ Validation completed.\n")