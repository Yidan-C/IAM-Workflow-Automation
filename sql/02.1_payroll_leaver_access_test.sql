SELECT
    'Payroll' AS application_name
    e.employee_id,
    e.employee_name,
    e.department,
    e.job_title,
    e.status AS employees_status,
    e.terminated_date,
    p.user_id,
    p.user_name,
    p.access_group,
    p.status AS payroll_status,
    p.last_login_date,
    
    CASE
        WHEN p.last_login_date > e.terminated_date
            THEN p.last_login_date - e.terminated_date
            ELSE NULL
        END AS days_after_termination,
    
    CASE
        WHEN p.last_login_date > e.terminated_date
            THEN 'Post-termination login'
            ELSE 'Active account only'
    END AS exception_type,

    CASE
        WHEN p.last_login_date > e.terminated_date
            THEN 'High Risk'
            ELSE 'Medium Risk'
    END AS risk_level

FROM read_csv_auto('source_data/employees.csv') AS e
LEFT JOIN read_csv_auto('normalised_data/Payroll_normalised.csv') AS p
    ON e.employee_id = p.employee_id

WHERE e.status = 'Terminated'
    AND p.status = 'Active'

ORDER BY days_after_termination;
