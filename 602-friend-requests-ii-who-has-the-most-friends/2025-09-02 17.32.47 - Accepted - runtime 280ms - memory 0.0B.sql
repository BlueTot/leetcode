# Write your MySQL query statement below
SELECT r2.requester_id AS id, 
COUNT(DISTINCT r2.accepter_id) AS num
FROM (
    SELECT requester_id, accepter_id FROM RequestAccepted
    UNION ALL
    SELECT r1.accepter_id AS requester_id, 
    r1.requester_id AS accepter_id FROM RequestAccepted r1
) r2
GROUP BY r2.requester_id
ORDER BY num DESC
LIMIT 1