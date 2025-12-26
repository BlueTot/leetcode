-- Write your PostgreSQL query statement below
WITH 
    first_half AS (
        SELECT t.driver_id, AVG(t.distance_km / t.fuel_consumed) AS avg
        FROM trips t
        WHERE EXTRACT(MONTH FROM t.trip_date) <= 6
        GROUP BY t.driver_id
    ),
    second_half AS (
        SELECT t.driver_id, AVG(t.distance_km / t.fuel_consumed) AS avg
        FROM trips t
        WHERE EXTRACT(MONTH FROM t.trip_date) > 6
        GROUP BY t.driver_id
    )
SELECT 
    d.driver_id, 
    d.driver_name, 
    ROUND(f.avg, 2) AS first_half_avg, 
    ROUND(s.avg, 2) AS second_half_avg, 
    ROUND(s.avg - f.avg, 2) AS efficiency_improvement 
FROM first_half f
INNER JOIN second_half s ON f.driver_id = s.driver_id
INNER JOIN drivers d ON d.driver_id = f.driver_id
WHERE s.avg > f.avg
ORDER BY efficiency_improvement DESC, driver_name ASC;