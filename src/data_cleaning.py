import pandas as pd
import os

DATA_PATH = "data/raw"

def clean_data():
    print("Function started...")
    for file in os.listdir(DATA_PATH):
        if file.endswith(".csv"):
            print(f"\nCleaning: {file}")
            
            df = pd.read_csv(os.path.join(DATA_PATH, file))
            
            # Remove duplicates
            df = df.drop_duplicates()
            
            # Try converting date columns
            for col in df.columns:
                if "date" in col.lower():
                    df[col] = pd.to_datetime(df[col], errors='coerce')
            
            # Fill missing values
            df = df.fillna(method='ffill')
            
            print("After Cleaning Shape:", df.shape)
            print(df.head())

if __name__ == "__main__":
    clean_data()