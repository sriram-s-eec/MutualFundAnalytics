import pandas as pd
import os

DATA_PATH = "data/raw"

def load_and_inspect():
    files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

    for file in files:
        print(f"\n📂 File: {file}")
        
        df = pd.read_csv(os.path.join(DATA_PATH, file))
        
        print("Shape:", df.shape)
        print("\nDtypes:\n", df.dtypes)
        print("\nHead:\n", df.head())
        print("\nMissing Values:\n", df.isnull().sum())
        
        print("-" * 60)

if __name__ == "__main__":
    load_and_inspect()