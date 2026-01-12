-- Write your PostgreSQL query statement below
SELECT t.customer_number FROM (
    SELECT o.customer_number, COUNT(*) AS count FROM Orders o
    GROUP BY o.customer_number
    ORDER BY count DESC
    LIMIT 1
) t;