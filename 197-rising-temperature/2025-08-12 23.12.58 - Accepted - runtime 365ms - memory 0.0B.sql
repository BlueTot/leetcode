# Write your MySQL query statement below
SELECT w.id FROM Weather w
JOIN Weather w2
ON w2.recordDate = w.recordDate - INTERVAL 1 DAY
WHERE w.temperature > w2.temperature