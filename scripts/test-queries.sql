
-- Check data volume
SELECT COUNT(*) AS total_records
FROM daily_sales_summary;

-- Check for null or invalid values
SELECT *
FROM daily_sales_summary
WHERE date IS NULL OR total_sales IS NULL;

-- Verify daily totals match expectations
SELECT date, SUM(total_sales) AS total_sales_day
FROM daily_sales_summary
GROUP BY date
ORDER BY date DESC
LIMIT 10;

-- Compare store-level summaries
SELECT store_id, SUM(total_sales) AS total_sales
FROM store_revenue_summary
GROUP BY store_id
ORDER BY total_sales DESC
LIMIT 5;

-- Top products by revenue
SELECT product_name, SUM(total_revenue) AS revenue
FROM product_performance
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- Data freshness check (latest report date)
SELECT MAX(date) AS latest_date
FROM daily_sales_summary;

-- Sanity check - join across tables
SELECT
  p.product_id,
  p.product_name,
  s.date,
  s.total_sales
FROM product_performance p
JOIN daily_sales_summary s
  ON p.report_date = s.date
LIMIT 5;
