# Write your MySQL query statement below
SELECT q1.person_name FROM Queue q1
JOIN (
    SELECT turn, 
    SUM(weight) OVER (ORDER BY turn) AS weightSum
    FROM Queue
) q2
ON q1.turn = q2.turn
WHERE q2.weightSum <= 1000
ORDER BY q2.weightSum DESC
LIMIT 1