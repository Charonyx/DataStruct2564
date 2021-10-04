# ------------- What is pip ? --------------
# PIP is a package manager for Python packages

# --------------- COMMANDS -----------------
# pip --version             #! check version
# pip install pandas        #! install pandas
# pip uninstall <library>   #! uninstall library

# pip list                  #! list packages

# https://pip.pypa.io/en/stable/installation/

import pandas as pd

data  = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "name"    : ["x","y","z"]
}

#load data into a DataFrame object:
df    = pd.DataFrame(data)
df2   = pd.DataFrame(data, index = ["data1", "data2", "data3"])

# print(df,   end='\n------------------\n')
# print(df2,  end='\n------------------\n') 

# print(df.loc[0], end='\n------------------\n')
# print(df.loc[1], end='\n------------------\n')

# print(df.loc[[1, 2]], end='\n------------------\n')

df.to_csv("Pandas/pandas.csv")          #! export to Pandas folder
# df.to_csv("t.csv")                    #! export to main folder 
print(pd.read_csv('Pandas/pandas.csv'))


# REF : https://www.w3schools.com/python/pandas/pandas_dataframes.asp