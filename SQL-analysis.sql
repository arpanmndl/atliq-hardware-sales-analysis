-- output transactions table
SELECT * FROM sales.transactions;



-- count of no. of customers
SELECT COUNT(*) FROM sales.customers;



-- count of no. of transactions for a specific market
SELECT count(*)
FROM sales.transactions
WHERE market_code = 'Mark001';



-- distinct currency in the transaction table
SELECT DISTINCT currency
FROM sales.transactions
WHERE currency = 'USD';



-- count of no. of transactions for a specific year
SELECT COUNT(*)
FROM sales.transactions t
INNER JOIN sales.date d ON t.order_date = d.date
WHERE d.year = 2020;



-- gives distinct years of transaction
SELECT DISTINCT d.year
FROM sales.transactions t
INNER JOIN sales.date d ON t.order_date = d.date;



-- total sales in 2020 with formatting
SELECT CONCAT('₹ ', FORMAT(SUM(t.sales_amount) / 1000, 3), 'K') AS formatted_sales
FROM sales.transactions t
INNER JOIN sales.date d ON t.order_date = d.date
WHERE d.year = 2020;

-- this below queries will also convert the USD sales in INR with formatting
SELECT CONCAT('₹ ', FORMAT(SUM(
    CASE 
        WHEN t.currency = 'USD' THEN t.sales_amount * 87
        ELSE t.sales_amount
    END
) / 1000, 3), 'K') AS total_sales
FROM sales.transactions t
INNER JOIN sales.date d ON t.order_date = d.date
WHERE d.year = 2019;

-- total sales in chennai
SELECT CONCAT('₹ ', FORMAT(SUM(
    CASE 
        WHEN t.currency = 'USD' THEN t.sales_amount * 87
        ELSE t.sales_amount
    END
) / 1000, 3), 'K') AS total_sales
FROM sales.transactions t
WHERE t.market_code = 'Mark001';

-- total sales in chennai in 2020
SELECT CONCAT('₹ ', FORMAT(SUM(
    CASE 
        WHEN t.currency = 'USD' THEN t.sales_amount * 87
        ELSE t.sales_amount
    END
) / 1000, 3), 'K') AS total_sales
FROM sales.transactions t
INNER JOIN sales.date d ON t.order_date = d.date
WHERE d.year = 2020 AND t.market_code = 'Mark001';
