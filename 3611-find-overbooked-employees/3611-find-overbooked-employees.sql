-- Write your PostgreSQL query statement below
WITH weekly_meeting_hours AS (
    SELECT 
        m.employee_id, 
        EXTRACT(WEEK FROM m.meeting_date) AS week, 
        SUM(m.duration_hours) AS weekly_hours
    FROM meetings m
    GROUP BY m.employee_id, EXTRACT(WEEK FROM m.meeting_date)
)
SELECT 
    wm.employee_id, 
    e.employee_name, 
    e.department, 
    COUNT(wm.week) AS meeting_heavy_weeks
FROM weekly_meeting_hours wm
INNER JOIN employees e ON wm.employee_id = e.employee_id
WHERE wm.weekly_hours > 20
GROUP BY wm.employee_id, e.employee_name, e.department
HAVING COUNT(wm.week) >= 2
ORDER BY meeting_heavy_weeks DESC, employee_name ASC;