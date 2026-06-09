import pandas as pd
importimport joblibimport numpy as np
from xgboost import XGBRegressor

# Load sample data
df = pd.read_excel("data/sample_data.xlsx")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Aggregate
df_agg = df.groupby("Date")["Revenue_INR"].sum().reset_index()

# Features
df_agg["month"] = df_agg["Date"].dt.month
df_agg["year"] = df_agg["Date"].dt.year

df_agg["lag_1"] = df_agg["Revenue_INR"].shift(1)
df_agg["lag_2"] = df_agg["Revenue_INR"].shift(2)
df_agg["lag_3"] = df_agg["Revenue_INR"].shift(3)
df_agg["rolling_mean_3"] = df_agg["Revenue_INR"].rolling(3).mean()

df_agg = df_agg.dropna()

features = ["month","year","lag_1","lag_2","lag_3","rolling_mean_3"]

X = df_agg[features]
y = df_agg["Revenue_INR"]

# Train
model = XGBRegressor(objective='reg:squarederror')
model.fit(X, y)

joblib.dump(model, "model/xgboost_model.pkl")

print("✅ Model trained & saved")
