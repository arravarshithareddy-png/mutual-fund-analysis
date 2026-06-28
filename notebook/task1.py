import pandas as pd
import os

folder_path = "../data/raw"

csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

datasets = {}

for file in csv_files:

    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    datasets[file] = df

    print("="*60)
    print("File:", file)

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst Five Rows")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nSummary Statistics:")
    print(df.describe(include='all'))

    print("\nUnique Values:")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")
        
    print()