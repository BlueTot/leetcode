-- Write your PostgreSQL query statement below
SELECT t.name, t.travelled_distance FROM (
    SELECT u.id, u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
    FROM Rides r
    RIGHT OUTER JOIN users u ON u.id = r.user_id
    GROUP BY u.id, u.name
) t
ORDER BY t.travelled_distance DESC, t.name ASC;