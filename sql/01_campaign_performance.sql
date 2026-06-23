CREATE OR REPLACE VIEW raw_marketing_data.campaign_performance AS

WITH clicks AS (
    SELECT
        campaign_id,
        sum(impressions_count) as total_impressions,
        sum(clicks_count) as total_clicks,
        sum(cost_usd) as total_cost

    FROM raw_marketing_data.clicks_impressions

    GROUP BY campaign_id    

),

conversions AS(
    SELECT
        campaign_id,
        COUNT(conversion_id) AS total_conversions,
        SUM(revenue_usd) AS total_revenue

    FROM raw_marketing_data.conversions

    GROUP BY campaign_id
)

SELECT
    c.campaign_id,
    c.campaign_name,
    c.channel,
    c.campaign_objective,
    c.target_audience,
    c.budget,
    c.start_date,
    c.end_date,


    COALESCE(cl.total_impressions,0) total_impressions,
    COALESCE(cl.total_clicks,0) total_clicks,
    COALESCE(conv.total_conversions,0) total_conversions,
    COALESCE(cl.total_cost,0) total_cost,
    COALESCE(conv.total_revenue,0) total_revenue,

    ROUND(100*SAFE_DIVIDE(cl.total_clicks, cl.total_impressions),2) CTR,

    ROUND(100*SAFE_DIVIDE(conv.total_conversions, cl.total_clicks),2) Conversion_Rate,
    
    ROUND(SAFE_DIVIDE(cl.total_cost, cl.total_clicks),2) CPC,
    
    ROUND(1000*SAFE_DIVIDE(cl.total_cost, cl.total_impressions),2) CPM,
    
    ROUND(SAFE_DIVIDE(cl.total_cost, conv.total_conversions),2) CPA,
    
    ROUND(SAFE_DIVIDE(conv.total_revenue, cl.total_cost),2) ROAS,
    
    ROUND(conv.total_revenue - cl.total_cost,2) Profit

    FROM raw_marketing_data.campaigns c

    LEFT JOIN clicks cl
    ON c.campaign_id = cl.campaign_id

    LEFT JOIN conversions conv
    ON c.campaign_id = conv.campaign_id
    
    