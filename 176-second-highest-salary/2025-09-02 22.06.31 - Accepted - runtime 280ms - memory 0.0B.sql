# Write your MySQL query statement below
SELECT (CASE WHEN EXISTS(
    SELECT DISTINCT e.salary AS SecondHighestSalary FROM (
    SELECT *,
    DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
    FROM Employee
) e WHERE e.rnk = 2
) THEN (
    SELECT DISTINCT e.salary AS SecondHighestSalary FROM (
    SELECT *,
    DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
    FROM Employee
) e WHERE e.rnk = 2
) ELSE NULL END) AS SecondHighestSalary