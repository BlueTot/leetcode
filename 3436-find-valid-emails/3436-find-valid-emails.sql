-- Write your PostgreSQL query statement below
SELECT * FROM Users u
WHERE u.email ~ '^[0-9A-Za-z_]+@[A-Za-z]+\.com$'
ORDER BY u.user_id ASC;