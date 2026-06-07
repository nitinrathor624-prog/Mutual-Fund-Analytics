import pandas as pd
import sqlite3
import os

db_path = "data/db/bluestock_mf.db"

conn = sqlite3.connect(db_path)

processed_path = "data/processed"

for file in os.listdir(processed_path):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        df = pd.read_csv(
            os.path.join(processed_path, file)
        )

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"Loaded: {table_name}")

conn.close()

print("Database created successfully")