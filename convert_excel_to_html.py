import os
import pandas as pd

# Function to convert Excel files to CSV
def convert_excel_to_csv(excel_file):
    # Read the Excel file
    xls = pd.ExcelFile(excel_file)

    # Create a directory for the CSV files if it doesn't exist
    csv_dir = os.path.splitext(excel_file)[0]
    os.makedirs(csv_dir, exist_ok=True)

    # Iterate through each sheet and save it as a CSV file
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        csv_file = os.path.join(csv_dir, f'{sheet_name}.html')
        df.to_html(csv_file, index=False)
        print(f'Saved {sheet_name} from {excel_file} to {csv_file}')

# Directory to search for Excel files
root_directory = 'Reports'

# Walk through the directory and all subdirectories
for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        if file.endswith('.xlsx') or file.endswith('.xls'):
            excel_file = os.path.join(subdir, file)
            convert_excel_to_csv(excel_file)
            os.rename(excel_file, os.path.join('excels', file))
