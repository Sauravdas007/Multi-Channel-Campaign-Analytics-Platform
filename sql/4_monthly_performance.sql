CREATE OR REPLACE VIEW raw_marketing_data.monthly_performance AS

WITH clicks_monthly AS (

    SELECT
        FORMAT_DATE('%Y-%m', DATE(timestamp)) AS month,
        SUM(impressions_count) AS impressions,
        SUM(clicks_count) AS clicks,
        SUM(cost_usd) AS spend

    FROM raw_marketing_data.clicks_impressions

    GROUP BY month

),

conversions_monthly AS (

    SELECT
        FORMAT_DATE('%Y-%m', DATE(timestamp)) AS month,
        COUNT(*) AS conversions,
        SUM(revenue_usd) AS revenue

    FROM raw_marketing_data.conversions

    GROUP BY month

)

SELECT

    c.month,

    c.impressions,

    c.clicks,

    c.spend,

    COALESCE(cv.conversions, 0) AS conversions,

    COALESCE(cv.revenue, 0) AS revenue,

    ROUND(
        100 * SAFE_DIVIDE(c.clicks, c.impressions),
        2
    ) AS CTR,

    ROUND(
        SAFE_DIVIDE(cv.revenue, c.spend),
        2
    ) AS ROAS

FROM clicks_monthly c

LEFT JOIN conversions_monthly cv

ON c.month = cv.month

ORDER BY c.month;