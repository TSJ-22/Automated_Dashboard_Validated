import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime

st.title("📦 Demand Forecast Dashboard")

file_path = "predictions/predictions.csv"

# ----------------------
# ✅ OPTION 1: Use CSV
# ----------------------
if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    if not df.empty:
        st.subheader("Latest Demand Forecast")
        st.metric("Predicted Demand", int(df.iloc[-1]["Predicted"]))

        st.subheader("Actual vs Predicted Demand")
        st.line_chart(df[["Actual", "Predicted"]])

    else:
        st.warning("⚠ Prediction file is empty")

# ----------------------
# ✅ OPTION 2: Auto Generate Demo Data
# ----------------------
else:
    st.info("📊 No data found → Generating sample demand data")

    dates = pd.date_range(end=datetime.today(), periods=50)

    np.random.seed(42)

    demand = np.random.randint(80, 200, size=len(dates))
    demand = demand + np.linspace(0, 40, len(dates))
    demand = demand + 15 * np.sin(np.linspace(0, 10, len(dates)))

    df_demo = pd.DataFrame({
        "Date": dates,
        "Actual": demand.astype(int)
    })

    df_demo["Predicted"] = df_demo["Actual"] + np.random.randint(-10, 10, len(dates))

    st.subheader("Sample Demand Forecast")

    st.metric("Predicted Demand (Latest)", int(df_demo.iloc[-1]["Predicted"]))

    st.subheader("Demand Trend")
    st.line_chart(df_demo[["Actual", "Predicted"]])

    st.dataframe(df_demo.tail())
