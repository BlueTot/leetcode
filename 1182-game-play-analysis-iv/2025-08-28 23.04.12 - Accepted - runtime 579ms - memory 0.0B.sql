# Write your MySQL query statement below
SELECT
ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity AS d1
JOIN (
    SELECT player_id, MIN(event_date) AS first_login FROM Activity
    GROUP BY player_id
) AS d2
ON d1.player_id = d2.player_id
AND d1.event_date = DATE_ADD(d2.first_login, INTERVAL 1 DAY)