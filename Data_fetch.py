import pandas as pdimport pandas as pd():
    # ✅ Simulated ERP (use Excel now)
    df = pd.read_csv("data/sample_data.csv")

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    return df
