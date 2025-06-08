import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": {50,40, 45}
}

#load data into a DataFrame object
df = pd.DataFrame(data)

print(df)

# Locata Row use the "loc" attribute
print(df.loc[0])

print(df.loc[[0, 1]])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

print(df.loc["day2"])

# Load files int a DataFrame
df = pd.read_csv('data.csv')
print(df)

