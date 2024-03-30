import streamlit as st
import pandas as pd
import json
import plotly.express as px

# Assuming FILE_PATH is the path to your patient records file.
FILE_PATH = 'patient_records.txt'

def load_data(n_lines=100):
    """Load the latest n_lines from the patient records file, handling potential errors."""
    data = []
    try:
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()[-n_lines:]
            for line in lines:
                try:
                    record = json.loads(line.strip())
                    data.append(record)
                except json.JSONDecodeError:
                    # Log the problematic line or handle it as needed
                    #st.warning(f"Skipping invalid JSON line: {line.strip()}")
                    continue
    except FileNotFoundError:
        st.error("File not found. Ensure the file path is correct.")
        return pd.DataFrame()

    return pd.DataFrame(data)

def create_distribution_chart(data, title, column):
    """Create and return a Plotly Express bar chart for the specified column data."""
    value_counts = data[column].value_counts().reset_index()
    value_counts.columns = [column, 'count']
    fig = px.bar(value_counts, x=column, y='count', title=title, labels={'count': 'Count'})
    fig.update_layout(xaxis_title=column.title(), yaxis_title="Count")
    return fig

def main():
    st.sidebar.header("Dashboard Settings")
    # User input for the number of records to display
    n_records = st.sidebar.number_input("Number of Records to Display (Maximum: 1000)", min_value=10, max_value=1000, value=100, step=10)
    
    st.title('Hospital EHR Dashboard')

    # Load data and display dataframe if data is available
    df = load_data(n_records)
    if not df.empty:
        department_filter = st.sidebar.multiselect("Filter by Department", options=df['department'].unique(), default=df['department'].unique())
        status_filter = st.sidebar.multiselect("Filter by Status", options=df['status'].unique(), default=df['status'].unique())
        
        # Apply filters to data
        filtered_data = df[df['department'].isin(department_filter) & df['status'].isin(status_filter)]
        
        if not filtered_data.empty:
            st.subheader('Latest Patient Records')
            st.dataframe(filtered_data)
            
            # Create and display charts
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(create_distribution_chart(filtered_data, "Diagnosis Distribution", "diagnosis"), use_container_width=True)
            with col2:
                st.plotly_chart(create_distribution_chart(filtered_data, "Status Distribution", "status"), use_container_width=True)
                
            col3, col4 = st.columns(2)
            with col3:
                st.plotly_chart(create_distribution_chart(filtered_data, "Medication Distribution", "medication"), use_container_width=True)
            with col4:
                st.plotly_chart(create_distribution_chart(filtered_data, "Department Distribution", "department"), use_container_width=True)
        else:
            st.write("No data available for the selected filters.")
    else:
        st.write("No data available. Please check the data file.")

if __name__ == '__main__':
    main()
