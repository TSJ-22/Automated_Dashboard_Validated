import pandas as pdimport pandas as pd():
    # ✅ Simulated ERP (use Excel now)
    df = pd.read_excel("data/sample_data.xlsx")

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    return df
