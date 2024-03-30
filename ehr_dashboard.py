import streamlit as st
import pandas as pd
import json
import plotly.express as px

# Assuming FILE_PATH is the path to your patient records file.
FILE_PATH = 'patient_records.txt'

def load_data(n_lines=100):
    """Load the latest n_lines from the patient records file."""
    try:
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()[-n_lines:]
            data = [json.loads(line.strip()) for line in lines]
            return pd.DataFrame(data)
    except FileNotFoundError:
        return pd.DataFrame()

def create_distribution_chart(data, title, column):
    """Create and return a Plotly Express bar chart for the specified column data."""
    # Count the occurrences, reset index, and rename columns for Plotly
    value_counts = data[column].value_counts().reset_index()
    value_counts.columns = [column, 'count']
    
    fig = px.bar(value_counts, 
                 x=column, y='count', 
                 labels={'count': 'Count'}, 
                 title=title)
    fig.update_layout(xaxis_title=column.title(), yaxis_title="Count")
    return fig

def main():
    st.sidebar.header("Dashboard Settings")
    # Allow user to select the number of records to display
    n_records = st.sidebar.number_input("Number of Records to Display", min_value=10, max_value=500, value=100, step=10)
    
    st.title('Hospital EHR Dashboard')
    
    df = load_data(n_records)
    
    if not df.empty:
        department_filter = st.sidebar.multiselect("Filter by Department", options=df['department'].unique(), default=df['department'].unique())
        status_filter = st.sidebar.multiselect("Filter by Status", options=df['status'].unique(), default=df['status'].unique())
        
        filtered_data = df[df['department'].isin(department_filter) & df['status'].isin(status_filter)]
        
        if not filtered_data.empty:
            st.subheader('Latest Patient Records')
            st.dataframe(filtered_data)
            
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
        st.write("No data available.")

if __name__ == '__main__':
    main()
