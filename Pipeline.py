from src.data_fetch import fetch_data
from src.feature_engineering import.predict import predictfrom src.feature_engineering import prepare_features

import pandas as pd
from datetime import datetime

def run_pipeline():

    df = fetch_data()
    df_agg = prepare_features(df)

    pred = predict(df_agg)
    actual = df_agg.iloc[-1]["Revenue_INR"]

    result = pd.DataFrame([{
        "Date": datetime.now(),
        "Actual": actual,
        "Predicted": pred
    }])

    result.to_csv("predictions/predictions.csv", mode="a", header=False, index=False)

    print("✅ Prediction saved:", pred)