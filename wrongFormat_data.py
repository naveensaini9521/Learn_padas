import pandas as pd

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

# Remove the  Row by using the dropna() method.
df.dropna(subset=['Data'], inplace=True)

# Replacing Values
df.loc[7, 'Duration'] = 45

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
        
# Removing Rows

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)