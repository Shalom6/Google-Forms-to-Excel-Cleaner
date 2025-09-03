from fetch_forms import fetch_form_responses

if __name__ == "__main__":
    sheet_id = "1nkrAqoIBc6Ze841PgVlElOhpHnGbw8hL9qpGM-BSUkQ"
    df = fetch_form_responses(sheet_id)
    print(df.head())

