import pandas as pd

df = pd.read_csv('data.csv')
print(df.head(10))

print(df.head())

# Using tail(), info()
print(df.tail())

print(df.info())