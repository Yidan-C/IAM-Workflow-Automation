import streamlit as st
import pandas as pd

st.title("IAM Workflow Automation") #page title
st.subheader("Leaver workflow dashboard") #dashboard description

employees = pd.read_csv('source_data/employees.csv')
financecore = pd.read_csv('source_data/FinanceCore.csv')
payroll = pd.read_csv('source_data/Payroll.csv')
leavers = employees[employees['status'] == 'Terminated']
financecore_leaver_total = len(leavers.merge(financecore, on='employee_name', how='inner'))
payroll_leaver_total = len(leavers.merge(payroll, on='employee_id', how='inner'))
exceptions = pd.read_csv('output/01_leaver_access_exceptions.csv') #read leaver exception output
total_exceptions = len(exceptions) #count total active leaver accounts
post_termination_logins = len(exceptions[exceptions['exception_type'] == 'Post-termination login']) #exceptions['exception_type']:get exception_type from exceptions
active_account_only = len(exceptions[exceptions["exception_type"] == 'Active account only'])

col1, col2, col3 = st.columns(3)
col1.metric("Total active leaver accounts",total_exceptions) #put one KPI
col2.metric("Post termination logins",post_termination_logins)
col3.metric("Active account only", active_account_only)

application_breakdown = (
    exceptions.groupby('application_name')
    .size() #how many rows
    .reset_index(name='exception_count') #turn Series into dataframe
) 
leaver_totals = {'FinanceCore':financecore_leaver_total, 'Payroll': payroll_leaver_total}
application_breakdown['total_leaver_accounts'] = (application_breakdown['application_name'].map(leaver_totals))
application_breakdown['exception_rate'] = (application_breakdown['exception_count'] / application_breakdown['total_leaver_accounts']*100).round(2) #round(2):keep 2 after .
st.subheader("Exceptions by application")
st.dataframe(application_breakdown.style.format({'exception_rate': '{:.2f}%'}))

st.dataframe(exceptions) #exception details

