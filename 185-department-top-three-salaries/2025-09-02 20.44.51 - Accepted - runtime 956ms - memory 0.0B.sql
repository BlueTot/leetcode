# Write your MySQL query statement below
SELECT
    Department.name AS Department,
    e1.name as Employee,
    e1.salary as Salary
FROM (
    SELECT *,
    DENSE_RANK() OVER (
        PARTITION BY departmentId
        ORDER BY salary DESC
    ) AS rnk
    FROM Employee
) e1
INNER JOIN Department ON Department.id = e1.departmentId
WHERE e1.rnk <= 3
