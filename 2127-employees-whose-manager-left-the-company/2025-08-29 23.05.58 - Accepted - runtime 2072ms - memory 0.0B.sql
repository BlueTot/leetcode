# Write your MySQL query statement below
SELECT e1.employee_id FROM Employees e1
WHERE NOT EXISTS(
    SELECT employee_id FROM Employees
    WHERE employee_id = e1.manager_id
) AND e1.salary < 30000 AND NOT ISNULL(e1.manager_id)
ORDER BY e1.employee_id