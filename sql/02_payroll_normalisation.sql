SELECT
    employee_id,
    user_id,
    user_name,
    employee_name,
 
    CASE
        WHEN "is this active?" = 'yes' THEN 'Active'
        WHEN "is this active?" = 'No' THEN 'Disabled'
        ELSE 'Unknown'
    END AS status,

    access AS access_group,
    "last sign in" AS last_login_date

FROM read_csv_auto('source_data/Payroll.csv')
