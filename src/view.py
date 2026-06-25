import pandas as pd
import streamlit as st
from pathlib import Path

# Load CSV
csv_path = Path(__file__).parent.parent / 'data' / 'Telco-Customer-Churn.csv'
df = pd.read_csv(csv_path)

"""print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())"""

# Title
st.title("CSV Viewer")

# Show table
st.dataframe(df, use_container_width = True)

# Optional: basic stats
st.write("Shape:", df.shape)
st.write("Columns:", df.columns)