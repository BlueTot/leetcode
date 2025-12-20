-- Write your PostgreSQL query statement below
SELECT t.id, t.visit_date, t.people FROM (
    SELECT *,
    LAG(people, 2) OVER (ORDER BY id) AS prev_2_persons,
    LAG(people, 1) OVER (ORDER BY id) AS prev_persons,
    LEAD(people, 1) OVER (ORDER BY id) AS next_persons,
    LEAD(people, 2) OVER (ORDER BY id) AS next_2_persons
    FROM Stadium
) t
WHERE 
    (t.people >= 100 AND t.next_persons >= 100 AND t.next_2_persons >= 100) OR 
    (t.prev_persons >= 100 AND t.people >= 100 AND t.next_persons >= 100) OR
    (t.prev_2_persons >= 100 AND t.prev_persons >= 100 AND t.people >= 100);
