# Data Dictionary

## 01_fund_master.csv
- scheme_code : Unique Scheme Code
- scheme_name : Mutual Fund Scheme Name
- fund_house : Fund House Name
- category : Fund Category

## 02_nav_history.csv
- date : NAV Date
- nav : Net Asset Value

## 03_aum_by_fund_house.csv
- fund_house : Fund House
- aum_cr : Assets Under Management (Crores)

## 04_monthly_sip_inflows.csv
- month : Month
- net_inflow_cr : SIP Inflow (Crores)

## 05_category_inflows.csv
- category : Fund Category
- net_inflow_cr : Category Inflow

## 06_industry_folio_count.csv
- month : Month
- folio_count_cr : Folio Count

## 07_scheme_performance.csv
- return_1yr : 1 Year Return
- return_3yr : 3 Year Return
- return_5yr : 5 Year Return
- expense_ratio : Expense Ratio

## 08_investor_transactions.csv
- transaction_id : Transaction ID
- amount : Transaction Amount

## 09_portfolio_holdings.csv
- sector : Sector Name
- weight_percent : Holding Percentage

## 10_benchmark_indices.csv
- index_name : Benchmark Index
- close_value : Closing Value