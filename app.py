import streamlit as st
import pandas as pd
from datetime import datetime
import time

# Set up the Streamlit page configuration
st.set_page_config(page_title="Advanced Attendance System", layout="wide")

# Title and Subtitle
st.title("📊 Advanced Attendance System")
st.subheader(f"Attendance Record for {datetime.now().strftime('%d-%m-%Y')}")

# Get the current timestamp and format it for date and timestamp
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# Corrected file name concatenation
filename = f"Attendance_{date}.csv"  # Using the formatted date in the file name

# Load the attendance data
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    st.error(f"File {filename} not found. Please make sure the attendance file is generated.")

# Display the DataFrame in an interactive web app with enhancements
if 'df' in locals():
    # Highlight max values and add a table style
    st.dataframe(df.style.highlight_max(axis=0).set_table_styles(
        [{
            'selector': 'thead th',
            'props': [('background-color', '#4CAF50'), ('color', 'white')]
        }, 
        {
            'selector': 'tbody tr:hover',
            'props': [('background-color', '#f5f5f5')]
        }]
    ))

    st.markdown(f"**Data last updated at:** {timestamp}")
else:
    st.warning("No data to display.")
