# Write your MySQL query statement below
SELECT ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance i
WHERE (
    SELECT COUNT(*) FROM Insurance i1
    WHERE i1.lat = i.lat and i1.lon = i.lon
) = 1
AND (
    SELECT COUNT(*) FROM Insurance i1
    WHERE i1.tiv_2015 = i.tiv_2015
) > 1