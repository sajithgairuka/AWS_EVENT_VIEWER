import pandas as pd
csv_file_path = 'event.csv'

try:  
    df = pd.read_csv(csv_file_path)
    for idx, col_name in enumerate(df.columns):
        print(f"Column {idx}: {col_name}")

except IOError:
    print(f"File '{csv_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# In This Program Read the CloudTrail CSV file into a pandas DataFrame and List the column names and their indices