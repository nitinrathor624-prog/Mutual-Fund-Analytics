import pandas as pd
import os

folder = "data/raw"

if not os.path.exists(folder):
    print("raw folder not found")
else:
    files = os.listdir(folder)

    for file in files:
        if file.endswith(".csv"):
            path = os.path.join(folder, file)

            df = pd.read_csv(path)

            print("\nFile Name:", file)
            print("Shape:", df.shape)
            print("\nColumns:")
            print(df.columns)
            print("\nData Types:")
            print(df.dtypes)
            print("\nFirst 5 Rows:")
            print(df.head())