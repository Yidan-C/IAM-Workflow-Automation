SELECT
    COUNT(*) AS total_active_leaver_accounts,

    SUM(
        CASE
            WHEN exception_type = 'Post-terminated login'
                THEN 1
            ELSE 0
        END
    ) AS post_termination_login_count, 

    SUM(
        CASE
            WHEN exception_type = 'Active account only'
                THEN 1
            ELSE 0
        END
    ) AS active_account_only_count

FROM read_csv_auto('output/01_leaver_access_exceptions.csv');