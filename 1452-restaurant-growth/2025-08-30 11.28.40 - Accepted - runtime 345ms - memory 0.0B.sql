# Write your MySQL query statement below
SELECT t.visited_on, 
t.total_amount AS amount, 
ROUND(t.total_amount / 7, 2) AS average_amount
FROM (
    SELECT DISTINCT visited_on, 
    (CASE WHEN TIMESTAMPDIFF(DAY,
        MIN(visited_on) OVER (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        ),
        MAX(visited_on) OVER (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        )) = 6
        THEN SUM(amount) OVER (
            ORDER BY visited_on
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
        )
    END) AS total_amount
    FROM Customer
) t
WHERE t.total_amount IS NOT NULL