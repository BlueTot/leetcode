# Write your MySQL query statement below
SELECT Signups.user_id, ROUND(
    IFNULL((
        SUM(CASE 
        WHEN c1.action = "confirmed" THEN 1 
        ELSE 0 END) / COUNT(c1.action)
    ), 0), 2) 
AS confirmation_rate FROM Signups
LEFT JOIN Confirmations as c1
ON Signups.user_id = c1.user_id
GROUP BY Signups.user_id