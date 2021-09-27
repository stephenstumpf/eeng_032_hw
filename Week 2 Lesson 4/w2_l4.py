"""
Problem: explore datasets obtained from the wild in both CSV and JSON formats.

This script performs basic data analysis on city-wide math test results of
New York City children between 3rd and 8th grade, in the years 2006-2011. Race and
ethnicity data are present, as well as mean score, std deviation, and 0th-4th
quartile data.  I attempt to plot them in a pleasing manner.

Author: Capt Stephen Stumpf
Date: 2021
Inputs: no command-line inputs, but appropriately-named files must be present in
the directory from which the script is executed.
Outputs: no return-value outputs, but the script will generate plots in new windows.
"""

# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
## Week 2 Lesson 4

# Go to www.data.gov or any a data source of your choice.

# * download a dataset, and examine that data.
# * Do this for a json file and a csv file. 

# Example:
#    * Find the mean, median mode of a data attribution or 
#    * Plot the data  

 
  
  
# My go to is pandas to read in new data.  But, you can use any package(s) that you like.


if __name__=="__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import json
    import os
    jsonfilenm = "./2006_-_2011_NYS_Math_Test_Results_by_Grade_-_Citywide_-_by_Race-Ethnicity.json"
    csvfilenm = "./2006_-_2011_NYS_Math_Test_Results_by_Grade_-_Citywide_-_by_Race-Ethnicity.csv"
    csv_df = pd.read_csv(csvfilenm)
    with open(jsonfilenm) as json_data:
        json_df = json.load(json_data)
    print(csv_df.columns)
# Index(['Grade', 'Year', 'Category', 'Number Tested', 'Mean Scale Score',
#       'Level 1 #', 'Level 1 %', 'Level 2 #', 'Level 2 %', 'Level 3 #',
#       'Level 3 %', 'Level 4 #', 'Level 4 %', 'Level 3+4 #', 'Level 3+4 %'],
#      dtype='object')
    print(csv_df.describe())
#               Year  Number Tested  Mean Scale Score  ...   Level 4 %    Level 3+4 #  Level 3+4 %
# count   168.000000     168.000000        168.000000  ...  168.000000     168.000000   168.000000
# mean   2008.500000   30543.142857        678.458333  ...   27.016667   19810.988095    70.810714
# std       1.712931   36902.292411         19.745038  ...   16.990838   22575.959582    18.705259
# min    2006.000000    9433.000000        628.000000  ...    2.300000    6491.000000    27.300000
# 25%    2007.000000   10200.750000        664.000000  ...   12.450000    8706.250000    54.225000
# 50%    2008.500000   21126.500000        677.500000  ...   22.500000    9975.500000    76.250000
# 75%    2010.000000   28592.500000        695.000000  ...   42.600000   17366.000000    86.050000
# max    2011.000000  177382.000000        716.000000  ...   64.000000  132637.000000    97.600000
#
# [8 rows x 13 columns]
#   csv_df.plot(x="Year", y="Mean Scale Score")
#   plt.show()
#   print("We can see that this naive plotting is uninformative. Let us examine the JSON.")
# As expected, this naive plotting is terrible.  Let's look at the JSON.
    print(json_df.keys())
    type(json_df['data'])
    
    df_json = pd.DataFrame(json_df['data'])
    A = df_json.iloc[:,-15:]
    A=A.rename(columns={8:'Grade', 9:'Year', 10:'Ethnicity', 11:'Number_Tested', 12:'Mean_Scale_Score'})
    A['Year'] = A['Year'].astype(int)
    A['Number_Tested'] = A['Number_Tested'].astype(int)
    interest = A.__getitem__(A['Ethnicity'] == 'Asian')
    interest_B = A.__getitem__(A['Ethnicity'] == 'White')
    interest = interest.__getitem__(A['Grade'] == '3')
    interest_B = interest_B.__getitem__(A['Grade'] == '3')
    interest['Year'] = interest['Year'].astype(int)
    interest['Mean_Scale_Score'] = interest['Mean_Scale_Score'].astype(int)
    plt.plot(interest['Year'], interest['Mean_Scale_Score'], label='Asian 3rd graders, 2006 - 2011')
    interest_B['Year'] = interest_B['Year'].astype(int)
    interest_B['Mean_Scale_Score'] = interest_B['Mean_Scale_Score'].astype(int)
    plt.plot(interest_B['Year'], interest_B['Mean_Scale_Score'], label='White 3rd graders, 2006 - 2011')
    plt.xlabel('Academic Year')
    plt.ylabel('Mean Scale Score')
    plt.legend()
    plt.show()
    