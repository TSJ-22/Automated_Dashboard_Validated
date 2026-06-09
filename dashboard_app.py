import streamlit as st
import pandas as pd

st.title("📊 Revenue Forecast Dashboard")

df = pd.read_csv("predictions/predictions.csv")

st.subheader("Latest Prediction")
st.metric("Predicted Revenue", int(df.iloc[-1]["Predicted"]))

st.subheader("Actual vs Predicted")
st.line_chart(df[["Actual","Predicted"]])