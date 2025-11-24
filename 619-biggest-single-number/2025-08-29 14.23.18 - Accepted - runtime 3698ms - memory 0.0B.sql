# Write your MySQL query statement below
SELECT MAX(t.num) AS num FROM (
    SELECT num FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS t