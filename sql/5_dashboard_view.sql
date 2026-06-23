CREATE OR REPLACE VIEW raw_marketing_data.dashboard_view AS

SELECT

campaign_name,

channel,

campaign_objective,

target_audience,

budget,

start_date,

end_date,

total_impressions,

total_clicks,

total_conversions,

total_cost,

total_revenue,

CTR,

Conversion_Rate,

CPC,

CPM,

CPA,

ROAS,

Profit

FROM raw_marketing_data.campaign_performance;