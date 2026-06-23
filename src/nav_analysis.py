import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/02_nav_history.csv")


df['date'] = pd.to_datetime(df['date'], errors='coerce')


df = df.sort_values(by='date')


plt.figure()
plt.plot(df['date'], df['nav'])
plt.title("NAV Trend Over Time")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.xticks(rotation=45)

plt.show()