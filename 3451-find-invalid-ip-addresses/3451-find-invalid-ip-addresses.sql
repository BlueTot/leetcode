-- Write your PostgreSQL query statement below
WITH 
    components AS (
        SELECT l.ip,
        (regexp_matches(l.ip, '^([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)$'))[1]::INTEGER AS one,
        (regexp_matches(l.ip, '^([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)$'))[2]::INTEGER AS two,
        (regexp_matches(l.ip, '^([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)$'))[3]::INTEGER AS three,
        (regexp_matches(l.ip, '^([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)$'))[4]::INTEGER AS four
        FROM logs l
        WHERE l.ip ~ '^([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)\.([1-9][0-9]*)$'
    ),
    valid_ips AS (
        SELECT c.ip FROM components c
        WHERE c.one >= 0 AND c.one <= 255
        AND c.two >= 0 AND c.two <= 255
        AND c.three >= 0 AND c.three <= 255
        AND c.four >= 0 AND c.four <= 255
    )
    SELECT l.ip, COUNT(l.ip) AS invalid_count FROM logs l
    WHERE l.ip NOT IN (SELECT * FROM valid_ips)
    GROUP BY l.ip
    ORDER BY invalid_count DESC, ip DESC;

