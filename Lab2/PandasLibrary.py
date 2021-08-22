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
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 