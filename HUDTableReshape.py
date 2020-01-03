# HUDTableReshape.py

# This Python script reshapes a table of income limits provided by HUD
# It expects input as a simplified version of the table with the following structure:

# |  Income level  |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |
# |----------------|-------|-------|-------|-------|-------|-------|-------|-------|
# | Very Low       | 37450 | 42800 | 48150 | 53500 | 57800 | 62100 | 66350 | 70650 |
# | Extremely Low  | 22500 | 25700 | 28900 | 32100 | 34700 | 37250 | 39850 | 42400 |
# | Low            | 56200 | 64200 | 72250 | 80250 | 86700 | 93100 | 99550 | 105950|

# Set the number of additional columns for family you need. Positive integers only, negatives undefined.
# A value of 0 leaves the original maximum family size as 8.
ADDITIONALCOLUMNS = 1

 
# Uses Pandas
import pandas as pd

# Create DataFrame

# Import data by hand (As an alternative to using a spreadsheet)
# df = pd.DataFrame(columns = ["name", "1", "2", "3", "4", "5", "6", "7", "8"],
#                   data = [["Very Low", 37450,42800,48150,53500,57800,62100,66350,70650],
#                           ["Extremely Low", 22500,25700,28900,32100,34700,37250,39850,42400],
#                           ["Low",56200,64200,72250,80250,86700,93100,99550,105950]])

# Import Excel Spreadsheet into DataFrame
excel_file = "HUD2019.xlsx"
df = pd.read_excel(excel_file, header = None, names = ["name", "1", "2", "3", "4", "5", "6", "7", "8"])


# Define rounding to nearest 50. HUD tables seem to always round up.
def roundToNearestN(x, n, direction='Standard'):
    if x % n == 0:
        return x
    elif x % n > n / 2 and direction == 'Standard' or direction == 'Up':
        return roundToNearestN(x + 1, n)
    elif direction == 'Standard' or direction == 'Down':
        return roundToNearestN(x - 1, n)


# Define column names for later
columns = ["income", "1", "2", "3", "4", "5", "6", "7", "8"]


# Add any additional columns needed for larger family sizes
for col in range(ADDITIONALCOLUMNS + 1):
    if col != 0:

        # Add number to columns list
        columns.append(str(8 + col))

        # Define name for interim dataframe
        name = str(8 + col)

        # Limit for each row is limit for famsize 4 * 132% + 8% for every family member over 8
        vLow = int(df.iloc[0][4] * (132 + 8 * col) / 100)
        exLow = int(df.iloc[1][4] * (132 + 8 * col) / 100)
        low = int(df.iloc[2][4] * (132 + 8 * col) / 100)

        # Round each of the numbers
        vLow = roundToNearestN(vLow, 50, 'Up')
        exLow = roundToNearestN(exLow, 50, 'Up')
        low = roundToNearestN(low, 50, 'Up')

        #Create interim datafame and add it to existing one
        dfAddition = pd.DataFrame({name: [vLow, exLow, low]})
        df = pd.concat([df, dfAddition], axis=1)

# Make a sorted list of all of the income limits
incomeLevelList = []
for index, row in df.iterrows():
    for i in range(1, 9 + ADDITIONALCOLUMNS):
        incomeLevelList.append(row.iloc[i])
incomeLevelList.sort()
 

# Make a new DataFrame for the new table
result = pd.DataFrame(columns=columns)


# For each income limit amount in the list, make a row in the new DataFrame
# with the appropriate category for each family size.
loop=0
for income in incomeLevelList:
    incomeLookupList = []
    incomeLookupList.append(income)
    for i in range(1, 9 + ADDITIONALCOLUMNS):
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
