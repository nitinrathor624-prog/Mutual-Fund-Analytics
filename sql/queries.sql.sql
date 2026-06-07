-- Top 5 funds by AUM
SELECT * FROM "03_aum_by_fund_house"
LIMIT 5;

-- Average NAV
SELECT AVG(nav) FROM "02_nav_history";

-- Total SIP Inflow
SELECT SUM(net_inflow_cr)
FROM "04_monthly_sip_inflows";