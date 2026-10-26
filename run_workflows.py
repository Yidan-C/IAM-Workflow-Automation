import duckdb

duckdb.sql(open('sql/02_payroll_normalisation.sql').read()).write_csv('normalised_data/Payroll_normalised.csv')
duckdb.sql(open('sql/01_leaver_access_test.sql').read()).write_csv('output/01_leaver_access_exceptions.csv')
duckdb.sql(open('sql/01.1_leaver_access_summary.sql').read()).write_csv('output/01.1_leaver_access_summary.csv')

print('Leaver Workflow completed.')