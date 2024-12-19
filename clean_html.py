import os
import pandas as pd

def clean_html(html_file):
    try:
        df = pd.read_html(html_file)[0]
    except Exception as e:
        print(f"Error reading {html_file}: {e}")
        os.remove(html_file)
        return
    before_len = len(df)
    df = df.dropna(axis=0, how='all')
    df = df.iloc[:df.last_valid_index() + 1]
    after_len = len(df)
    if before_len != after_len:
        print(f'Cleaned {html_file} from {before_len} to {after_len}')
        df.to_html(html_file, index=True)

root_directory = 'Reports'

# Walk through the directory and all subdirectories
for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        if file.endswith('.html'):
            html_file = os.path.join(subdir, file)
            clean_html(html_file)
            # os.rename(excel_file, os.path.join('excels', file))
