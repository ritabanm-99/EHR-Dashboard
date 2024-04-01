# EHR-Dashboard
Streaming analytics for Simulated Electronic Health Record Data. 

### <Objective:> 
To simulate a Electronic Health Record Database system, and perform streaming analytics like a hospital administrator would to track operations.

## V1.0 Features:

1. Streaming artificial data from a script to simulate a real-time streaming process in a hospital of incoming patients.
2. Filters to categorize patients by department and status.
3. Minimalistic Bar Charts to visualize Distributions for diagnosis, status, medication and department.

### Trying the app: 

1. To run this app, star the repository as it initiates the data stream generation script and visit the App: https://ehrdashboard.streamlit.app/ 

2. To test the app locally, you may clone the repository and run the command:

`streamlit run ehr_dashboard.py`

#### note:

* If you run into any issues with streamlit, try creating a virtual environment in the project directory and installing streamlit using the following commands:

1. `python3 -m venv .venv`

2. `source .venv/bin/activate`
