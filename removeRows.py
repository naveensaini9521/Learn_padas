import pandas as pd

df = pd.read_csv('data.csv')
new_df = df.dropna()

print(new_df.to_string())

df.dropna(inplace = True)
print(df.to_string())

df.fillna({"Calories":130}, inplace=True)

# Replace Using Mean, Median, Mode

x = df["Calories"].mean()
df.fillna({"Calories":x}, inplace=True)


x = df["Calories"].median()
df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].mode()[0]
df.fillna({"Calories": x}, inplace=True)
