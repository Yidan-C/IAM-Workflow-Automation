> Note: All data used in this project is synthetic and created for demonstration purposes only.

# IAM Controls Automation

A personal project exploring how SQL, Python and automation can be used to perform and report IAM control testing.

## Current Functionality

### Leaver Controls
- Normalises application access data from different source formats
- Reconciles HR leaver data against multiple application access listings
- Identifies active accounts belonging to terminated employees
- Identifies post-termination login activity
- Consolidates exceptions across FinanceCore and Payroll
- Automates control execution and CSV reporting using Python
- Provides Streamlit reporting for key control metrics and exception details

## Dashboard Preview
![IAM Controls Automation Dashboard](dashboard_screenshot.jpg)

## Technology

- SQL / DuckDB
- Python
- pandas
- Streamlit

## Current Workflow

HR and application data  
→ Data normalisation  
→ SQL control testing  
→ Consolidated exceptions  
→ Python automation  
→ Streamlit reporting

## Project Status

Completed:
- Leaver Controls V1

Planned:
- Joiner Controls, including access approval evidence processing and planned AI-assisted evidence extraction
- Mover Controls
- Periodic User Access Review
- Privileged Access Controls