
-- Drop existing tables (optional)
DROP TABLE IF EXISTS daily_sales_summary;
DROP TABLE IF EXISTS product_performance;
DROP TABLE IF EXISTS store_revenue_summary;

-- Create table for daily sales summary
CREATE TABLE daily_sales_summary (
    date DATE NOT NULL,
    store_id VARCHAR(50),
    total_sales NUMERIC(12, 2),
    num_transactions INT,
    avg_transaction_value NUMERIC(10, 2),
    PRIMARY KEY (date, store_id)
);

-- Create table for product-level performance
CREATE TABLE product_performance (
    product_id VARCHAR(50),
    product_name VARCHAR(255),
    total_units_sold INT,
    total_revenue NUMERIC(12, 2),
    avg_price NUMERIC(10, 2),
    report_date DATE,
    PRIMARY KEY (product_id, report_date)
);

-- Create table for store-level revenue tracking
CREATE TABLE store_revenue_summary (
    store_id VARCHAR(50),
    total_sales NUMERIC(12, 2),
    total_transactions INT,
    report_date DATE,
    PRIMARY KEY (store_id, report_date)
);
