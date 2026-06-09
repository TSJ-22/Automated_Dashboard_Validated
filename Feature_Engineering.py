def prepare_features(df):

    df_agg = df.groupby("Date")["Revenue_INR"].sum().reset_index()

    df_agg["month"] = df_agg["Date"].dt.month
    df_agg["year"] = df_agg["Date"].dt.year

    df_agg["lag_1"] = df_agg["Revenue_INR"].shift(1)
    df_agg["lag_2"] = df_agg["Revenue_INR"].shift(2)
    df_agg["lag_3"] = df_agg["Revenue_INR"].shift(3)

    df_agg["rolling_mean_3"] = df_agg["Revenue_INR"].rolling(3).mean()

    return df_agg.dropna()
