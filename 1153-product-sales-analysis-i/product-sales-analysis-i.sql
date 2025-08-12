# Write your MySQL query statement below
SELECT product_name, year, price FROM Product
INNER JOIN Sales ON Product.product_id = Sales.product_id