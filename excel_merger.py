# Excel Merger
# Author: Muhammad Ibrahim
# GitHub: github.com/muhammad-ibrahim-py
# Description: Merges multiple Excel files into one


import pandas as pd
from pathlib import Path

def merge_excel_files(folder: str = ".")->None:
    """Merge all Excel files in a folder into one file.

    Args:
        folder: the folder to search for Excel files(default: current folder)

    Returns:
        None. Saves merged file as merged_sales.xlsx.

    """

    # Find all Excel files in the folder, excluding the output file

    excel_files = [f for f in Path(folder).glob("*.xlsx") if f.name != "merged_sales.xlsx"]

    # Check if any files were found

    if not excel_files:
        print("No excel file found!")
        return

    # Read each Excel file and collect the data

    all_data = []
    for file in excel_files:
        data = pd.read_excel(file)
        all_data.append(data)
        print(f"Loaded: {file.name}")

    # Combine all data into one table
   
    merged = pd.concat(all_data, ignore_index=True)

    # Save the merged data to a new Excel file

    merged.to_excel("merged_sales.xlsx", index=False)

    # Show summary

    print(f"Merged {len(excel_files)} files into merged_sales.xlsx")
    print(f"Total rows: {len(merged)}")

# Run the script when executed directly

if __name__ == "__main__":
    merge_excel_files()


