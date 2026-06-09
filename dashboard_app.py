import streamlit as stimport streamlit
import os

st.title("📊 Revenue Forecast Dashboard")

file_path = "predictions/predictions.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    st.subheader("Latest Prediction")
    st.metric("Predicted Revenue", int(df.iloc[-1]["Predicted"]))

    st.subheader("Trend (Actual vs Predicted)")
    st.line_chart(df[["Actual","Predicted"]])
else:
    st.warning("No prediction data available. Please run pipeline.")
