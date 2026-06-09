import streamlit as st
import pandas as pd
import os
st.title("📊 Revenue Forecast Dashboard")

# ✅ Upload CSV
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("✅ Uploaded Data Preview")
    st.dataframe(df.head())

    # Example: show chart
    if "Revenue_INR" in df.columns:
        st.line_chart(df["Revenue_INR"])

else:
    st.info("Upload a CSV file to begin")
