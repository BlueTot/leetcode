-- Write your PostgreSQL query statement below
SELECT s.name FROM SalesPerson s
INNER JOIN (
    SELECT s.sales_id FROM SalesPerson s
    EXCEPT
    SELECT DISTINCT o.sales_id FROM Orders o
    INNER JOIN Company c ON c.com_id = o.com_id
    WHERE c.name = 'RED'
) t ON s.sales_id = t.sales_id;