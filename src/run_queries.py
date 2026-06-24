from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///bluestock_mf.db")

# Query 1
df = pd.read_sql("SELECT * FROM fact_nav ORDER BY nav DESC LIMIT 5", engine)
print("Top NAV:\n", df)

# Query 2
df = pd.read_sql("SELECT AVG(nav) as avg_nav FROM fact_nav", engine)
print("\nAverage NAV:\n", df)