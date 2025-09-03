import pandas as pd

def clean_responses(df):
    print(df.isnull().sum())
    df.dropna(inplace=True)
    df.fillna("Unknown", inplace=True)

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    # Drop rows with missing timestamps
    df.dropna(subset=["timestamp"], inplace=True)

    # Fill text columns with "Unknown"
    text_cols = df.select_dtypes(include="object").columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    # Fill numeric columns with 0
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].fillna(0)

    return df