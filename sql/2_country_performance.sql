CREATE OR REPLACE VIEW raw_marketing_data.country_performance AS

WITH conversions_country AS (
    SELECT
        campaign_id,
        country,


        COUNT(converion_id) conversions,

        SUM(revenue_usd) revenue

    FROM raw_marketing_data.conversions
    
    GROUP BY campaign_id, country
)

SELECT
    ci.country,

    SUM(ci.impressions_count) impressions,

    SUM(ci.clicks_count) clicks,

    SUM(ci.cost_usd) spend,

    SUM(IFNULL(cc.conversions,0)) conversions,

    SUM(IFNULL(cc.revenue,0)) revenue,

    ROUND(100*SAFE_DIVIDE(SUM(ci.clicks_count),SUM(ci.impressions_count)),2) CTR,

    ROUND(100*SAFE_DIVIDE(SUM(IFNULL(cc.conversions,0)),SUM(ci.clicks_count)),2) Conversion_Rate,

    ROUND(SAFE_DIVIDE(SUM(ci.cost_usd), SUM(IFNULL(cc.conversions,0))),2) CPA,

    ROUND(SAFE_DIVIDE(SUM(IFNULL(cc.revenue,0)), SUM(ci.cost_usd)),2) ROAS

FROM raw_marketing_data.clicks_impressions ci

LEFT JOIN conversions_country cc

ON ci.campaign_id = cc.campaign_id

AND ci.country = cc.country

GROUP BY ci.country

ORDER BY revenue DESC;
    