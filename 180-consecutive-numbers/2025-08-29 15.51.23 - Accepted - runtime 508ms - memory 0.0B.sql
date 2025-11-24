# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums FROM Logs l1
INNER JOIN Logs l2 ON l1.num = l2.num AND l2.id = l1.id + 1
INNER JOIN Logs l3 ON l2.num = l3.num AND l3.id = l2.id + 1
