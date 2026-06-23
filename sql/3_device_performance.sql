CREATE OR REPLACE VIEW raw_marketing_data.device_performance AS

SELECT
    device_type,

    SUM(impressions_count) impressions,

    SUM(clicks_count) clicks,

    SUM(cost_usd) spend,

    ROUND(100*SAFE_DIVIDE(SUM(clicks_count), SUM(impressions_count)),2) CTR,

    ROUND(SAFE_DIVIDE(SUM(cost_usd), SUM(clicks_count)),2) CPC,

    ROUND(1000*SAFE_DIVIDE(SUM(cost_usd), SUM(impressions_count)),2) CPM

    FROM raw_marketing_data.clicks_impressions

    GROUP BY device_type

    ORDER BY spend DESC;