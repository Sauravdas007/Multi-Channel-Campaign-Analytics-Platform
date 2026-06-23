# scripts/generate_data.py

import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# ============================================================
# CONFIGURATION
# ============================================================

NUM_CAMPAIGNS = 40
NUM_IMPRESSIONS = 250000
NUM_CONVERSIONS = 25000

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2026, 12, 31)

# ============================================================
# CAMPAIGN METADATA
# ============================================================

campaign_names = [
    "Summer Sale",
    "Winter Sale",
    "Product Launch",
    "Brand Awareness",
    "Loyalty Program",
    "Holiday Promo",
    "Flash Sale",
    "Retargeting",
    "Newsletter",
    "Spring Campaign",
    "Back to School",
    "Black Friday",
    "Cyber Monday",
    "Valentine Special",
    "Festival Promo",
    "New Year Blast",
    "Referral Program",
    "Discount Bonanza",
    "Clearance Sale",
    "VIP Exclusive",
    "App Install Drive",
    "Influencer Collab",
    "Content Marketing Push",
    "SEO Boost",
    "Remarketing Blitz",
    "Customer Winback",
    "Upsell Campaign",
    "Cross-Sell Drive",
    "Market Expansion",
    "Regional Promo",
    "Global Awareness",
    "Brand Relaunch",
    "Limited Edition",
    "Early Bird Offer",
    "Weekend Promo",
    "Mega Sale",
    "Anniversary Campaign",
    "Milestone Celebration",
    "Community Drive",
    "CSR Initiative"
]

channels = [
    "Facebook",
    "Google Ads",
    "Email",
    "Instagram",
    "LinkedIn",
    "Twitter"
]

campaign_objectives = [
    "Awareness",
    "Traffic",
    "Lead Generation",
    "Sales",
    "Retention"
]

target_audiences = [
    "New Users",
    "Returning Users",
    "VIP Customers"
]

# ============================================================
# WEIGHTED COUNTRY DISTRIBUTION
# ============================================================

countries = [
    "India",
    "USA",
    "UK",
    "Germany",
    "Canada"
]

country_probs = [
    0.45,
    0.20,
    0.15,
    0.10,
    0.10
]

# ============================================================
# DEVICE DISTRIBUTION
# ============================================================

devices = [
    "Mobile",
    "Desktop",
    "Tablet"
]

device_probs = [
    0.65,
    0.30,
    0.05
]

# ============================================================
# BROWSER DISTRIBUTION
# ============================================================

browsers = [
    "Chrome",
    "Safari",
    "Edge",
    "Firefox"
]

browser_probs = [
    0.60,
    0.20,
    0.10,
    0.10
]

# ============================================================
# OPERATING SYSTEM DISTRIBUTION
# ============================================================

operating_systems = [
    "Android",
    "iOS",
    "Windows",
    "macOS"
]

os_probs = [
    0.45,
    0.20,
    0.25,
    0.10
]

# ============================================================
# AD PLACEMENTS
# ============================================================

placement_map = {
    "Facebook": ["Feed", "Stories"],
    "Instagram": ["Feed", "Stories"],
    "Google Ads": ["Search", "Display"],
    "Email": ["Newsletter", "Promotion"],
    "LinkedIn": ["Feed", "Sidebar"],
    "Twitter": ["Feed", "Timeline"]
}

# ============================================================
# CAMPAIGN GENERATION
# ============================================================

campaign_rows = []

max_days = (END_DATE - START_DATE).days

for i in range(NUM_CAMPAIGNS):

    campaign_id = f"CMP{str(i+1).zfill(3)}"

    campaign_name = random.choice(campaign_names)

    channel = random.choice(channels)

    objective = random.choice(campaign_objectives)

    audience = random.choice(target_audiences)

    budget = random.randint(2000, 10000)

    start_date = START_DATE + timedelta(
        days=random.randint(0, max_days)
    )

    end_date = min(
        start_date + timedelta(days=random.randint(30, 120)),
        END_DATE
    )

    campaign_rows.append([
        campaign_id,
        campaign_name,
        channel,
        objective,
        audience,
        budget,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d")
    ])

campaigns_df = pd.DataFrame(
    campaign_rows,
    columns=[
        "campaign_id",
        "campaign_name",
        "channel",
        "campaign_objective",
        "target_audience",
        "budget",
        "start_date",
        "end_date"
    ]
)

campaigns_df.to_csv(
    "data/campaigns.csv",
    index=False
)

print("Generated campaigns.csv")


# ============================================================
# CLICKS / IMPRESSIONS GENERATION
# ============================================================

click_rows = []

for i in range(NUM_IMPRESSIONS):

    # Randomly select a campaign
    campaign = campaigns_df.sample(1).iloc[0]

    channel = campaign["channel"]

    # --------------------------------------------------------
    # Realistic CTR by marketing channel
    # --------------------------------------------------------

    if channel == "Facebook":
        ctr = np.random.uniform(0.01, 0.03)

    elif channel == "Google Ads":
        ctr = np.random.uniform(0.03, 0.07)

    elif channel == "Email":
        ctr = np.random.uniform(0.08, 0.15)

    elif channel == "Instagram":
        ctr = np.random.uniform(0.02, 0.05)

    elif channel == "LinkedIn":
        ctr = np.random.uniform(0.02, 0.04)

    else:   # Twitter
        ctr = np.random.uniform(0.01, 0.03)

    # --------------------------------------------------------
    # Impressions
    # --------------------------------------------------------

    impressions = np.random.randint(200, 5001)

    clicks = max(1, int(impressions * ctr))

    # --------------------------------------------------------
    # Country
    # --------------------------------------------------------

    country = np.random.choice(
        countries,
        p=country_probs
    )

    # --------------------------------------------------------
    # Device
    # --------------------------------------------------------

    device = np.random.choice(
        devices,
        p=device_probs
    )

    # --------------------------------------------------------
    # Browser
    # --------------------------------------------------------

    browser = np.random.choice(
        browsers,
        p=browser_probs
    )

    # --------------------------------------------------------
    # Operating System
    # --------------------------------------------------------

    operating_system = np.random.choice(
        operating_systems,
        p=os_probs
    )

    # --------------------------------------------------------
    # Ad Placement
    # --------------------------------------------------------

    placement = random.choice(
        placement_map[channel]
    )

    # --------------------------------------------------------
    # Cost (channel specific)
    # --------------------------------------------------------

    if channel == "Google Ads":
        cost = round(np.random.uniform(0.50, 5.00), 2)

    elif channel == "Facebook":
        cost = round(np.random.uniform(0.20, 2.00), 2)

    elif channel == "Instagram":
        cost = round(np.random.uniform(0.30, 3.00), 2)

    elif channel == "LinkedIn":
        cost = round(np.random.uniform(1.00, 8.00), 2)

    elif channel == "Email":
        cost = round(np.random.uniform(0.02, 0.20), 2)

    else:   # Twitter
        cost = round(np.random.uniform(0.20, 2.50), 2)

    # --------------------------------------------------------
    # Timestamp within campaign duration
    # --------------------------------------------------------

    campaign_start = datetime.strptime(
        campaign["start_date"],
        "%Y-%m-%d"
    )

    campaign_end = datetime.strptime(
        campaign["end_date"],
        "%Y-%m-%d"
    )

    timestamp = fake.date_time_between(
        start_date=campaign_start,
        end_date=campaign_end
    )

    # --------------------------------------------------------
    # Append row
    # --------------------------------------------------------

    click_rows.append([

        f"IMP{i+1}",

        campaign["campaign_id"],

        timestamp,

        impressions,

        clicks,

        country,

        device,

        browser,

        operating_system,

        placement,

        cost

    ])

# ============================================================
# CREATE CLICKS DATAFRAME
# ============================================================

clicks_df = pd.DataFrame(

    click_rows,

    columns=[

        "impression_id",

        "campaign_id",

        "timestamp",

        "impressions_count",

        "clicks_count",

        "country",

        "device_type",

        "browser",

        "operating_system",

        "ad_placement",

        "cost_usd"

    ]

)

clicks_df.to_csv(
    "data/clicks_impressions.csv",
    index=False
)

print("Generated clicks_impressions.csv")


# ============================================================
# CONVERSIONS GENERATION
# ============================================================

segments = [
    "New",
    "Returning",
    "VIP"
]

segment_probs = [
    0.60,
    0.30,
    0.10
]

conversion_rows = []

for i in range(NUM_CONVERSIONS):

    campaign = campaigns_df.sample(1).iloc[0]

    campaign_start = datetime.strptime(
        campaign["start_date"],
        "%Y-%m-%d"
    )

    campaign_end = datetime.strptime(
        campaign["end_date"],
        "%Y-%m-%d"
    )

    revenue = round(
        np.random.uniform(10, 300),
        2
    )

    country = np.random.choice(
        countries,
        p=country_probs
    )

    customer_segment = np.random.choice(
        segments,
        p=segment_probs
    )

    conversion_rows.append([

        f"CONV{i+1}",

        campaign["campaign_id"],

        fake.date_time_between(
            start_date=campaign_start,
            end_date=campaign_end
        ),

        fake.uuid4(),

        revenue,

        country,

        customer_segment

    ])

# ============================================================
# CREATE CONVERSIONS DATAFRAME
# ============================================================

conversions_df = pd.DataFrame(

    conversion_rows,

    columns=[

        "conversion_id",

        "campaign_id",

        "timestamp",

        "user_id",

        "revenue_usd",

        "country",

        "customer_segment"

    ]

)

conversions_df.to_csv(
    "data/conversions.csv",
    index=False
)

print("Generated conversions.csv")


# ============================================================
# DATA QUALITY ISSUES
# ============================================================

print("Injecting realistic data quality issues...")


# ------------------------------------------------------------
# 1. Missing campaign IDs (1%)
# ------------------------------------------------------------

missing_campaign_idx = clicks_df.sample(
    frac=0.01,
    random_state=42
).index

clicks_df.loc[
    missing_campaign_idx,
    "campaign_id"
] = None


# ------------------------------------------------------------
# 2. Duplicate conversion rows (2%)
# ------------------------------------------------------------

duplicates = conversions_df.sample(
    frac=0.02,
    random_state=42
)

conversions_df = pd.concat(
    [conversions_df, duplicates],
    ignore_index=True
)


# ------------------------------------------------------------
# 3. Revenue outliers (0.5%)
# ------------------------------------------------------------

outlier_idx = conversions_df.sample(
    frac=0.005,
    random_state=42
).index

conversions_df.loc[
    outlier_idx,
    "revenue_usd"
] *= 20


# ------------------------------------------------------------
# 4. Missing browser values (0.5%)
# ------------------------------------------------------------

browser_missing_idx = clicks_df.sample(
    frac=0.005,
    random_state=10
).index

clicks_df.loc[
    browser_missing_idx,
    "browser"
] = None


# ------------------------------------------------------------
# 5. Missing operating system values (0.5%)
# ------------------------------------------------------------

os_missing_idx = clicks_df.sample(
    frac=0.005,
    random_state=20
).index

clicks_df.loc[
    os_missing_idx,
    "operating_system"
] = None


# ------------------------------------------------------------
# 6. Negative costs (0.3%)
# Simulates refunds/accounting corrections
# ------------------------------------------------------------

negative_cost_idx = clicks_df.sample(
    frac=0.003,
    random_state=30
).index

clicks_df.loc[
    negative_cost_idx,
    "cost_usd"
] *= -1


# ------------------------------------------------------------
# 7. Extremely high impression counts (0.2%)
# Simulates bot traffic/spikes
# ------------------------------------------------------------

high_impression_idx = clicks_df.sample(
    frac=0.002,
    random_state=40
).index

clicks_df.loc[
    high_impression_idx,
    "impressions_count"
] *= 10


# ------------------------------------------------------------
# 8. Zero clicks despite impressions (0.5%)
# ------------------------------------------------------------

zero_click_idx = clicks_df.sample(
    frac=0.005,
    random_state=50
).index

clicks_df.loc[
    zero_click_idx,
    "clicks_count"
] = 0


# ============================================================
# SAVE DIRTY DATASETS
# ============================================================

clicks_df.to_csv(
    "data/clicks_impressions.csv",
    index=False
)

conversions_df.to_csv(
    "data/conversions.csv",
    index=False
)

print("Injected data quality issues successfully.")

print("\nDataset Generation Completed Successfully!")
print("-------------------------------------------")
print(f"Campaigns      : {len(campaigns_df):,}")
print(f"Clicks         : {len(clicks_df):,}")
print(f"Conversions    : {len(conversions_df):,}")

print("\nFiles created:")
print("✔ data/campaigns.csv")
print("✔ data/clicks_impressions.csv")
print("✔ data/conversions.csv")