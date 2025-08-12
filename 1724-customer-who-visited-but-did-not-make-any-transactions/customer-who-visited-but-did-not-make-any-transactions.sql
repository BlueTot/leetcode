# Write your MySQL query statement below
SELECT customer_id, SUM(Transactions.visit_id is null) AS count_no_trans
FROM Visits
LEFT JOIN Transactions ON Transactions.visit_id = Visits.visit_id
GROUP BY customer_id
HAVING count_no_trans > 0