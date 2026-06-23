import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_data = pd.read_csv("data/raw/02_nav_history.csv")

# Clean column names
fund_master.columns = fund_master.columns.str.strip().str.lower().str.replace(" ", "_")
nav_data.columns = nav_data.columns.str.strip().str.lower().str.replace(" ", "_")

# Validation using amfi_code
missing = set(fund_master['amfi_code']) - set(nav_data['amfi_code'])

print("\nMissing AMFI Codes:", missing)
print("Total Missing:", len(missing))