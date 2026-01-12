-- Write your PostgreSQL query statement below
SELECT e.employee_id, (
    CASE WHEN e.employee_id % 2 = 1 AND NOT (e.name ~ '^M') THEN e.salary ELSE 0 END
) AS bonus
FROM Employees e
ORDER BY e.employee_id;