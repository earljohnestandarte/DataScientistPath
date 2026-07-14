
import pandas as pd

# Input of data
temp = pd.Series([-0.8, -0.1, 7.7, 13.8, 18.0, 22.4,
                  25.9, 25.3, 21.0, 14.0, 9.6, -1.4])

temp.index = ['Jan', 'Feb', 'Mar', 'Apr',
              'May', 'Jun', 'Jul', 'Aug',
              'Sep', 'Oct', 'Nov', 'Dec']

# print(temp.iloc[0:3]);
# print(temp.loc[:])

# march = temp.loc['Mar']
# print(temp.loc[temp < march])

# print(temp.where(temp < 20).dropna().index)

# print(temp * 5)

# print(temp.loc[temp >= 15] + 1)

# this returns basic statistical information
# print(temp.describe())

# this returns the sum of temp
# print(temp.sum())

# Changing, adding, and deleting values for a Series object

# temp.loc[['Mar', "Sep"]] = 69.000
# print(temp)


# temp.loc['Vikendi'] = 33

# print(temp)

next = pd.Series({"Erangel": 96.00})

temp = pd.concat([temp, next])
print(temp)

temp2 = pd.Series([10, 20, 30, 40])
temp2 = pd.concat([temp2, pd.Series({4:66})])
print(temp2)

temp2 = temp2.drop(4)
print(f"Dropped: \n{temp2}")