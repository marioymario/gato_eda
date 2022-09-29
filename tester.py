#!/usr/bin/env python3

from eda_func import *

dataframe = pd.read_csv('out.csv')
dictionary = feature_obs(dataframe)
                          
message = dictionary['message']
columns_missing_between_zero_and_five_pct = dictionary['features less than 5%']
columns_missing_more_than_five_pct = dictionary['features over 5%']

information = basic_info(dataframe)

print(information)
                          
print(message)
print(columns_missing_between_zero_and_five_pct)
print(columns_missing_more_than_five_pct)

print(missing(dataframe))


