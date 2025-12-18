-- Write your PostgreSQL query statement below
WITH
    valid_students AS (
        SELECT s.student_id, s.subject, MAX(exam_date) AS last_date, MIN(exam_date) AS first_date
        FROM Scores s
        GROUP BY s.student_id, s.subject
        HAVING COUNT(DISTINCT exam_date) >= 2
    ),
    last_score AS (
        SELECT s.student_id, s.subject, s.score FROM Scores s
        INNER JOIN valid_students v ON v.student_id = s.student_id AND v.subject = s.subject
        WHERE s.exam_date = v.last_date
    ),
    first_score AS (
        SELECT s.student_id, s.subject, s.score FROM Scores s
        INNER JOIN valid_students v ON v.student_id = s.student_id AND v.subject = s.subject
        WHERE s.exam_date = v.first_date
    )
    SELECT l.student_id, l.subject, f.score AS first_score, l.score AS latest_score
    FROM last_score l
    INNER JOIN first_score f ON f.student_id = l.student_id AND f.subject = l.subject
    WHERE l.score > f.score
    ORDER BY l.student_id, l.subject;
