from fetch_forms import fetch_form_responses
from clean_data import clean_responses
from transform import transform
from export_excel import export_to_excel
if __name__ == "__main__":
    sheet_id = "1nkrAqoIBc6Ze841PgVlElOhpHnGbw8hL9qpGM-BSUkQ"
    df = fetch_form_responses(sheet_id)
    print(df.head())

df = fetch_form_responses(sheet_id)
cleaned_df = clean_responses(df)
print(cleaned_df.head())



df = fetch_form_responses(sheet_id)
cleaned_df = clean_responses(df)
transformed_df = transform(cleaned_df)
print(transformed_df.head())

df = fetch_form_responses(sheet_id)
cleaned_df = clean_responses(df)
transformed_df = transform(cleaned_df)

export_to_excel(transformed_df, "form_responses.xlsx")
print("Excel file created successfully!")
