from sqlalchemy import create_engine
import pandas as pd

# create database
engine = create_engine("sqlite:///bluestock_mf.db")

# load cleaned data
df = pd.read_csv("data/processed/nav_cleaned.csv")

# push to database
df.to_sql("fact_nav", engine, if_exists='replace', index=False)

print("✅ Data inserted into database")