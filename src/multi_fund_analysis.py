import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

# Print columns (just to confirm)
print("Columns:", df.columns)

# Convert date
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Sort data
df = df.sort_values(by='date')

print("Max NAV:", df['nav'].max())
print("Min NAV:", df['nav'].min())
print("Average NAV:", df['nav'].mean())

# Plot NAV
plt.figure()
plt.plot(df['date'], df['nav'])

plt.title("NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.grid(True)

# Save graph
plt.savefig("nav_trend.png")
plt.close()

print("✅ NAV graph saved successfully")