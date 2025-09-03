def transform(df):
    df.sort_values(by=["timestamp"], ascending=True)
    df = df[["timestamp","name", "email", "address", "phone_number"]]
    df.loc[:, "name"] = df["name"].str.title()
    df.loc[:, "email"] = df["email"].str.strip()
    df.loc[:, "address"] = df["address"].str.strip()
    df.loc[:, "phone_number"] = df["phone_number"].str.strip()
    df = df[["name", "email", "address", "phone_number"]].copy()

    return df