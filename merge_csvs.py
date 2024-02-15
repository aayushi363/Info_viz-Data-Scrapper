import pandas as pd

# Load the two CSV files into pandas DataFrames
df1 = pd.read_csv('asplos_data.csv')
df2 = pd.read_csv('citation.csv')

# Merge the DataFrames based on the common column
merged_df = pd.merge(df1, df2, on='Title', how='inner')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('asplos_merged_file.csv', index=False)

