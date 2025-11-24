# Write your MySQL query statement below
SELECT s1.id, 
(CASE WHEN s1.id % 2 = 0
THEN (
    SELECT student FROM Seat WHERE id = s1.id - 1
) ELSE (
    CASE WHEN EXISTS(SELECT student FROM Seat WHERE id = s1.id + 1)
    THEN (SELECT student FROM Seat WHERE id = s1.id + 1)
    ELSE s1.student
    END)
END)
AS student
FROM Seat s1