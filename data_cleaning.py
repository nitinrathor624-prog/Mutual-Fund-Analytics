import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

for file in os.listdir(raw_path):

    if file.endswith(".csv"):

        file_path = os.path.join(raw_path, file)

        df = pd.read_csv(file_path)

        print(f"\nProcessing {file}")

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Missing values count
        print("Missing Values:")
        print(df.isnull().sum())

        # Convert date columns
        for col in df.columns:
            if "date" in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        output_file = os.path.join(
            processed_path,
            file
        )

        df.to_csv(output_file, index=False)

        print(f"Saved: {file}")

print("\nAll files cleaned successfully")