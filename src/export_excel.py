# src/export_excel.py

import os
from openpyxl import load_workbook

def export_to_excel(df, filename="form_responses.xlsx"):
    """
    Save a DataFrame to Excel in the 'outputs' folder with adjusted column widths.
    """
    # 1️⃣ Ensure outputs folder exists
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)

    # 2️⃣ Full path to save the file
    filepath = os.path.join(output_folder, filename)

    # 3️⃣ Export DataFrame to Excel
    df.to_excel(filepath, index=False, sheet_name="Responses")
    print(f"Excel file created at: {filepath}")

    # 4️⃣ Adjust column widths using openpyxl
    wb = load_workbook(filepath)
    ws = wb.active

    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Get column letter
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[column].width = max_length + 2  # Add padding

    # 5️⃣ Save workbook with updated column widths
    wb.save(filepath)
    print("Column widths adjusted successfully!")
