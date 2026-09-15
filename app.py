import streamlit as st
import pandas as pd

st.title("IAM Controls Automation") #page title
st.write("Leaver controls dashboard") #dashborad description

exceptions = pd.read_csv('output/01_leaver_access_exceptions.csv') #read leaver exception output
total_exceptions = len(exceptions) #count total active leaver accounts
post_termination_logins = len(exceptions[exceptions['exception_type'] == 'Post-termination login']) #exceptions['exception_type']:get exception_type from exceptions
active_account_only = len(exceptions[exceptions["exception_type"] == 'Active account only'])

col1, col2, col3 = st.columns(3)
col1.metric("Total active leaver accounts",total_exceptions)
col2.metric("Post termination logins",post_termination_logins)
col3.metric("Active account only", active_account_only)

application_breakdown = (exceptions.groupby('application_name').size().reset_index(name='exception_count'))
st.subheader("Exceptions by application")
st.write(application_breakdown)

st.dataframe(exceptions) #exception details

