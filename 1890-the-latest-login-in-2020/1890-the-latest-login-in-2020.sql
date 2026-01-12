-- Write your PostgreSQL query statement below
SELECT l.user_id, MAX(l.time_stamp) AS last_stamp
FROM Logins l
WHERE EXTRACT(YEAR FROM l.time_stamp::date) = 2020
GROUP BY l.user_id;