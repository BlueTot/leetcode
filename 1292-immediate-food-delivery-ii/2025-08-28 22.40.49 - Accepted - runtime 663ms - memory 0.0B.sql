# Write your MySQL query statement below
SELECT ROUND(
    SUM(CASE 
        WHEN d1.order_date = d1.customer_pref_delivery_date THEN 1
        ELSE 0
        END
    ) / COUNT(*) * 100, 2
) AS immediate_percentage 
FROM Delivery AS d1
INNER JOIN (
    SELECT customer_id, MIN(order_date) AS first_date FROM Delivery
    GROUP BY customer_id
) AS d2
ON d2.first_date = d1.order_date AND d2.customer_id = d1.customer_id
