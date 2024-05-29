import pandas as pd
import glob

# Step 1: Locate the Excel Files
excel_files = glob.glob("Book.xlsx")

# Step 2: Read and Combine the Data
all_data = []

for file in excel_files:
    df = pd.read_excel(file)
    all_data.append(df)

# Step 3: Concatenate the DataFrames
combined_df = pd.concat(all_data, ignore_index=True)

# Step 4: Save the Combined Data to a New Excel File
combined_df.to_excel("combined_data.xlsx", index=False)

print("Data from multiple files combined and saved to 'combined_data.xlsx'")
