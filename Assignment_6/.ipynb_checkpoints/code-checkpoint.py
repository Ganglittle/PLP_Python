import pandas as pd
df = pd.read_csv('todays_data.csv')

print(df.head())

df.info()

print(df.isnull().sum())
df = df.dropna()

# Part 2
print(df.describe())

# Part 3
import matplotlib.pyplot as plt
df = pd.read_csv('todays_data.csv')
