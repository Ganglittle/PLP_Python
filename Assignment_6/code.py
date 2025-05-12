import pandas as pd
df = pd.read_csv('todays_data.csv')
# Part 1
print(df.head())

df.info()

print(df.isnull().sum())
df = df.dropna()

# Part 2
print(df.describe())

# Part 3
import matplotlib.pyplot as plt
df = pd.read_csv('todays_data.csv')


df['Academic Level'] = df['Academic Level'].str.strip().str.lower()
grouped = df.groupby('Academic Level')['GPA'].mean().sort_values()


grouped.plot(kind='line', marker='o')
plt.title("Average GPA by Academic Level")
plt.xlabel("Academic Level")
plt.ylabel("Average GPA")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()