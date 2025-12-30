-- Write your PostgreSQL query statement below
WITH
    unbanned_trips AS (
        SELECT t.id, t.client_id, t.driver_id, t.city_id, t.status, t.request_at
        FROM Trips t
        INNER JOIN Users u1 ON t.client_id = u1.users_id
        INNER JOIN Users u2 ON t.driver_id = u2.users_id
        WHERE u1.banned = 'No' AND u2.banned = 'No'
    ),
    counts AS (
        SELECT 
            u.request_at, 
            COUNT(*) AS total,
            SUM(CASE WHEN u.status <> 'completed' THEN 1 ELSE 0 END) AS cancelled
        FROM unbanned_trips u
        WHERE (u.request_at::date BETWEEN '2013-10-01' AND '2013-10-03')
        GROUP BY u.request_at
    )
SELECT 
    c.request_at AS "Day", 
    ROUND(c.cancelled::numeric / c.total, 2) AS "Cancellation Rate"
FROM counts c