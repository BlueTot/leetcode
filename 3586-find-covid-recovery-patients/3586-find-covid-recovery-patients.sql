-- Write your PostgreSQL query statement below
WITH 
    positive AS (
        SELECT ct.patient_id, MIN(ct.test_date) AS first_positive
        FROM covid_tests ct
        WHERE result = 'Positive'
        GROUP BY ct.patient_id
    ),
    negative AS (
        SELECT p.patient_id, MIN(ct.test_date) AS first_negative
        FROM covid_tests ct
        INNER JOIN positive p ON p.patient_id = ct.patient_id
        WHERE ct.test_date > p.first_positive
        AND result = 'Negative'
        GROUP BY p.patient_id
    )
    SELECT 
        pt.patient_id, 
        pt.patient_name, 
        pt.age,
        (n.first_negative::date - p.first_positive::date) AS recovery_time
    FROM positive p
    INNER JOIN negative n ON p.patient_id = n.patient_id
    INNER JOIN patients pt ON pt.patient_id = p.patient_id
    ORDER BY recovery_time ASC, patient_name ASC;