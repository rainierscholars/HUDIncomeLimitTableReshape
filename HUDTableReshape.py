# HUDTableReshap.py

# This Python script reshapes a table of income limits provided by HUD
# It expects input as a simplified version of the table with the following structure:

# |  Income level  |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |
# |----------------|-------|-------|-------|-------|-------|-------|-------|-------|
# | Very Low       | 37450 | 42800 | 48150 | 53500 | 57800 | 62100 | 66350 | 70650 |
# | Extremely Low  | 22500 | 25700 | 28900 | 32100 | 34700 | 37250 | 39850 | 42400 |
# | Low            | 56200 | 64200 | 72250 | 80250 | 86700 | 93100 | 99550 | 105950|

 
# Uses Pandas and xlrd which I thought was bundled with pandas, but isn't?
import pandas as pd

# Create DataFrame

# Import data by hand
# df = pd.DataFrame(columns = ["name", "1", "2", "3", "4", "5", "6", "7", "8"],
#                   data = [["Very Low", 37450,42800,48150,53500,57800,62100,66350,70650],
#                           ["Extremely Low", 22500,25700,28900,32100,34700,37250,39850,42400],
#                           ["Low",56200,64200,72250,80250,86700,93100,99550,105950]])

# Import Excel Spreadsheet into DataFrame
excel_file = "C:\\Users\\croberts\\Documents\\Python Scripts\\HUD2019.xlsx"
df = pd.read_excel(excel_file, header = None, names = ["name", "1", "2", "3", "4", "5", "6", "7", "8"])


# Make a sorted list of all of the income limits
incomeLevelList = []
for index, row in df.iterrows():
    for i in range(1,9):
        incomeLevelList.append(row.iloc[i])
incomeLevelList.sort()
 

# Make a new DataFrame for the new table
result = pd.DataFrame(columns=["income", "1", "2", "3", "4", "5", "6", "7", "8"])


# For each income limit amount in the list, make a row in the new DataFrame
# with the appropriate category for each family size.
loop=0
for income in incomeLevelList:
    incomeLookupList = []
    incomeLookupList.append(income)
    for i in range(1,9):
        if(income<=df.iloc[1][i]):
            incomeLookupList.append(df.iloc[1][0])
        elif(income<=df.iloc[0][i]):
            incomeLookupList.append(df.iloc[0][0])
        elif(income<=df.iloc[2][i]):
            incomeLookupList.append(df.iloc[2][0])
        else:
            incomeLookupList.append('Not Low')
    result.loc[loop] = incomeLookupList
    loop = loop+1

# Save results as a csv
result.to_csv("reshapedTable.csv", index=False, encoding='utf-8', header=True)
