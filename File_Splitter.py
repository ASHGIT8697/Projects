import os
import sys
import pandas as pd

def split_excel_by_column(file_path, split_column, mapping_sheet, mapping_column_key, mapping_column_value, output_dir):
    #Read the Excel File
    df_main = pd.read_excel(file_path, sheet_name=0, engine='openpyxl')

    #Read the mapping sheet
    df_mapping = pd.read_excel(file_path, sheet_name=mapping_sheet, engine='openpyxl')

    #Create a dictionary
    mapping_dict = pd.Series(df_mapping[mapping_column_value].values, index=df_mapping[mapping_column_key]).to_dict()

    #Get unique values in the specified column
    unique_values = df_main[split_column].unique()

    #output directory existance
    os.makedirs(output_dir, exist_ok=True)

    #Create and Save
    for value in unique_values:
        df_split = df_main[df_main[split_column] == value]

        rename_value = mapping_dict.get(value, value)

        output_file = os.path.join(output_dir, f"{rename_value}.xlsx")

        df_split.to_excel(output_file, index=False, engine='openpyxl')

        print(f"Saved file : {output_file}")

if __name__ == "__main__":
    file_path = input("Enter the Excel File Path : ")
    split_column = input("Enter the Column To Split by : ")
    mapping_sheet = input("Enter the Sheet Name containing the Renaming ID's : ")
    mapping_column_key = input("Enter the Vendor Code Column Name: ")
    mapping_column_value = input("Enter the Column to which the Files has to be Renamed : ")
    output_dir = input("Enter the Output Path to be Saved : ")

split_excel_by_column(file_path, split_column, mapping_sheet, mapping_column_key, mapping_column_value, output_dir)
