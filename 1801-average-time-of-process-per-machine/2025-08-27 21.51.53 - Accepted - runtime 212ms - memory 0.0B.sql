# Write your MySQL query statement below
SELECT t1.machine_id, ROUND(AVG(t2.timestamp - t1.timestamp), 3) AS processing_time 
FROM Activity as t1
INNER JOIN Activity as t2 
ON t1.machine_id = t2.machine_id AND t1.process_id = t2.process_id
WHERE t1.activity_type = "start" and t2.activity_type = "end"
GROUP BY t1.machine_id