# Write your MySQL query statement below
WITH total_users AS (
    SELECT COUNT(*) AS total FROM USERS
)
SELECT contest_id, 
ROUND(COUNT(Users.user_id) / t.total * 100, 2) AS percentage
FROM Register
INNER JOIN Users ON Users.user_id = Register.user_id
CROSS JOIN total_users as t
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC