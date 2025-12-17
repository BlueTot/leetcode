-- Write your PostgreSQL query statement below
WITH tree_info AS (
    SELECT t.id,
        EXISTS (SELECT 1 FROM Tree t1 WHERE t1.p_id = t.id) AS has_child
    FROM Tree t
)
SELECT t.id, CASE
    WHEN ti.has_child AND t.p_id IS NOT NULL
        THEN 'Inner'
    WHEN NOT ti.has_child AND t.p_id IS NOT NULL
        THEN 'Leaf'
    ELSE 'Root'
    END AS type
FROM Tree t
INNER JOIN tree_info ti ON ti.id = t.id;



