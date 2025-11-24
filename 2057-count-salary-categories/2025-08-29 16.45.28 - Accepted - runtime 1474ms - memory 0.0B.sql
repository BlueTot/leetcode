# Write your MySQL query statement below
SELECT a3.category, 
IFNULL(accounts_count, 0) AS accounts_count
FROM (
    SELECT "Low Salary" AS category
    UNION ALL
    SELECT "Average Salary"
    UNION ALL
    SELECT "High Salary"
) AS a3
LEFT JOIN (
    SELECT a1.category, COUNT(*) AS accounts_count
    FROM (
        SELECT 
        (CASE
            WHEN income < 20000 THEN "Low Salary"
            WHEN income >= 2000 AND income <= 50000 THEN "Average Salary"
            ELSE "High Salary"
        END) AS category
        FROM Accounts
    ) AS a1
    GROUP BY a1.category
) AS a2
ON a3.category = a2.category