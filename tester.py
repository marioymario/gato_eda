#!/usr/bin/env python3

from eda_func import *

# Reading data
dataframe = pd.read_csv('out.csv')

print("******************************************************")
print("Start of the information: ")

#information = 
print("******************************************************")
print(basic_info(dataframe))
print("******************************************************")                         
print("******************************************************") 
dictionary = feature_obs(dataframe)
'''
message = dictionary['message']
columns_missing_between_zero_and_five_pct = dictionary['features less than 5%']
columns_missing_more_than_five_pct = dictionary['features over 5%']'''

for i, j in dictionary.items():
    print(f'{i}: {j}')
    
'''
print(message)##
print(columns_missing_between_zero_and_five_pct)##
print(columns_missing_more_than_five_pct)##'''
print("******************************************************")                         
print("******************************************************") 
print('Missing:')
print(missing(dataframe))

## 
print("******************************************************")                         
print("******************************************************") 
print('invalid items:')
inval = invalid_df(dataframe)
print(inval)

print("******************************************************")                         
print("******************************************************") 
sift = siftdatatype(dataframe)
for i, j in sift.items():
    print(f'{i}: {j}')

print("End of the information: ")
