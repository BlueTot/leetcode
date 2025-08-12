# Write your MySQL query statement below
SELECT w.id FROM Weather w
WHERE w.temperature > (
    SELECT w2.temperature FROM Weather w2
    WHERE w2.recordDate = w.recordDate - INTERVAL 1 DAY
)