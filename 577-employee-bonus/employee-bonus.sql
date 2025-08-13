# Write your MySQL query statement below
SELECT name, Bonus.bonus FROM Employee
LEFT JOIN Bonus ON Bonus.empId = Employee.empId
WHERE Bonus.bonus IS null OR Bonus.bonus < 1000