import pandas as pd
import pandas


#version Check
print(pd.__version__)

# 1
df = pd.read_csv('data.csv')
print(df.to_string)

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3,7,2]
}

myvar1 = pandas.DataFrame(mydataset)

print(myvar1)


# 2
mydataset2 = {
    'cars': ["AUDI", "Range Rover", "Tata"],
    'passings': [3, 7,2]
}

myvar2 = pd.DataFrame(mydataset2)

print(myvar2)

# Series
a = [1, 7, 2]
myvar3 = pd.Series(a)
print(myvar3)

print(myvar3[0])

# Creata Lables wht iht "index" argument
myvar4 = pd.Series(a, index = ["x", "y", "z"])
print(myvar4)


print(myvar4["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar5 = pd.Series(calories)
print(myvar5)

myvar5 = pd.Series(calories, index = ["day1", "day2"])
print(myvar5)


data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)