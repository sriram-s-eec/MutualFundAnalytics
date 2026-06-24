import pandas as pd

# load file
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Before Cleaning:", df.shape)

# convert date
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# remove duplicates
df = df.drop_duplicates()

# fill missing NAV
df['nav'] = df['nav'].ffill()

# remove invalid NAV
df = df[df['nav'] > 0]

print("After Cleaning:", df.shape)

# save cleaned file
df.to_csv("data/processed/nav_cleaned.csv", index=False)

print("✅ Cleaning completed")