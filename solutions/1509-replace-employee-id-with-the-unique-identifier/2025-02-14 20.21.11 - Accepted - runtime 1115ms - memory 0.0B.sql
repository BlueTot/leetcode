# Write your MySQL query statement below
SELECT unique_id, name FROM employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id