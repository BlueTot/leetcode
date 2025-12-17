-- Write your PostgreSQL query statement below
SELECT s2.score, t.rank FROM Scores s2 INNER JOIN (
    SELECT s.score, ROW_NUMBER() OVER (ORDER BY score DESC) AS rank FROM (
        SELECT DISTINCT score FROM Scores ORDER BY score DESC
    ) s
) t ON t.score = s2.score
ORDER BY s2.score DESC;