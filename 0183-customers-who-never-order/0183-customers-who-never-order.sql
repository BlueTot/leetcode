-- Write your PostgreSQL query statement below
SELECT c.name AS "Customers" FROM (
    SELECT c.id FROM Customers c
    EXCEPT
    SELECT DISTINCT o.customerId FROM Orders o
) t INNER JOIN Customers c ON t.id = c.id;