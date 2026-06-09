import joblib

model = joblib.load("model/xgboost_model.pkl")

def predict(df_agg):

    features = ["month","year","lag_1","lag_2","lag_3","rolling_mean_3"]

    latest = df_agg.iloc[-1:]
    X = latest[features]

    prediction = model.predict(X)[0]

    return prediction