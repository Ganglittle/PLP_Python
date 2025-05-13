import pandas as pd

df_data = pd.read_csv('COVID Data/owid-covid-data.csv')

print(df_data.head())

print(df_data.columns)


missing_values = df_data.isnull().sum()
print(missing_values)