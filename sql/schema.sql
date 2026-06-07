CREATE TABLE fund_master (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE nav_history (
    scheme_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE scheme_performance (
    scheme_code INTEGER,
    return_1yr REAL,
    return_3yr REAL,
    return_5yr REAL,
    expense_ratio REAL
);

CREATE TABLE investor_transactions (
    transaction_id INTEGER,
    scheme_code INTEGER,
    transaction_date DATE,
    amount REAL
);