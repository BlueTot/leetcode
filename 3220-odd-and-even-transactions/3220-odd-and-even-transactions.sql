-- Write your PostgreSQL query statement below
WITH 
    evens AS (
        SELECT t.transaction_date, SUM(t.amount) AS amount
        FROM transactions t
        WHERE t.amount % 2 = 0
        GROUP BY t.transaction_date
    ),
    odds AS (
        SELECT t.transaction_date, SUM(t.amount) AS amount
        FROM transactions t
        WHERE t.amount % 2 = 1
        GROUP BY t.transaction_date
    )
SELECT 
    t.transaction_date, 
    COALESCE(o.amount, 0) AS odd_sum, 
    COALESCE(e.amount, 0) AS even_sum
FROM (SELECT DISTINCT transaction_date FROM transactions) t
LEFT OUTER JOIN evens e ON t.transaction_date = e.transaction_date
LEFT OUTER JOIN odds o ON t.transaction_date = o.transaction_date
ORDER BY t.transaction_date ASC;