# Write your MySQL query statement below
SELECT p.product_id,
    IFNULL(
        (
            SELECT p1.new_price
            FROM Products p1
            WHERE p1.product_id = p.product_id
            AND p1.change_date <= '2019-08-16'
            ORDER BY p1.change_date DESC
            LIMIT 1
        ), 10
    ) AS price
FROM (SELECT DISTINCT product_id FROM Products) p;