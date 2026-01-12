-- Write your PostgreSQL query statement below
SELECT DISTINCT s.product_id, p.product_name FROM Sales s
INNER JOIN Product p ON s.product_id = p.product_id
GROUP BY s.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01'::date AND MAX(s.sale_date) <= '2019-03-31';