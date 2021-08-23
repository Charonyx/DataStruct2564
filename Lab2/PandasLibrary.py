# ------------- What is pip ? --------------
# PIP is a package manager for Python packages

# --------------- COMMANDS -----------------
# pip --version             #! check version
# pip install pandas        #! install pandas
# pip uninstall <library>   #! uninstall library

# pip list                  #! list packages

# https://pip.pypa.io/en/stable/installation/

# import pandas as pd

# data = {'Jan' : 'January', 'Feb' : 'Febuary', 'Mar' : 'March', 'Apr' : 'April'}

# print(data)
# df = pd.DataFrame(data)
# print(df)

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "name"    : ["A","B","C"]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df, end='\n------------------\n')
print(df2, end='\n------------------\n') 
# print(df.loc[0].keys)
print(df.loc[0], end='\n------------------\n')
print(df.loc[1], end='\n------------------\n')
print(df.loc[[0, 1]], end='\n------------------\n')

# df = pd.read_csv('data.csv')

# https://www.w3schools.com/python/pandas/pandas_dataframes.asp