import pandas as pd
import os

DATA_PATH = "data/raw"

def load_all_data():
    files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

    for file in files:
        print(f"\nProcessing File: {file}")
        
        df = pd.read_csv(os.path.join(DATA_PATH, file))
        
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print("Missing Values:\n", df.isnull().sum())
        print("-" * 50)

if __name__ == "__main__":
    load_all_data()