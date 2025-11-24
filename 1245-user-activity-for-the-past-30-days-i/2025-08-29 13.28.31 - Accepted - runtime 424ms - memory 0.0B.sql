# Write your MySQL query statement below
SELECT
activity_date as day, 
COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY day
HAVING day BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND "2019-07-27"