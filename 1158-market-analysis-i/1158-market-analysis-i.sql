-- Write your PostgreSQL query statement below
SELECT u.user_id AS buyer_id, u.join_date, COALESCE(t.orders_in_2019, 0) AS orders_in_2019 FROM Users u
LEFT OUTER JOIN (
    SELECT o.buyer_id, COUNT(*) AS orders_in_2019 FROM Orders o
    WHERE EXTRACT(YEAR FROM o.order_date) = 2019
    GROUP BY o.buyer_id
) t ON u.user_id = t.buyer_id;