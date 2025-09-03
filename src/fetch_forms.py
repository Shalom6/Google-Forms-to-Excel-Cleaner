from google.oauth2.service_account import Credentials
import gspread
import pandas as pd

# print("Imports successful!")

def fetch_form_responses(sheet_id):
    # load JSON file → create credentials object → set scopes
    creds = Credentials.from_service_account_file(
        "../credentials/forms-excel-service.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]  # Fill in the Sheets API scope here
    )

    #using gspread to authorize with credientials
    client = gspread.authorize(creds)

    sheet_id = "1nkrAqoIBc6Ze841PgVlElOhpHnGbw8hL9qpGM-BSUkQ"
    spreadsheet = client.open_by_key(sheet_id)

    sheet = spreadsheet.sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    print(df.head(5))
    return df

# Checking the path to .json
# import os
# print(os.path.exists("credentials/forms-excel-service.json")) # returned false, so this is the wrong path
# print(os.path.exists("../credentials/forms-excel-service.json")) # returned true, so this is the correct path
