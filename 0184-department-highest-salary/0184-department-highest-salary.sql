-- Write your PostgreSQL query statement below
WITH max_salary AS (
    SELECT e.departmentID, MAX(e.salary) AS salary FROM Employee e
    GROUP BY e.departmentID
)
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary FROM Employee e
INNER JOIN max_salary ms ON ms.departmentID = e.departmentID
AND ms.salary = e.salary
INNER JOIN Department d
ON d.id = e.departmentID;