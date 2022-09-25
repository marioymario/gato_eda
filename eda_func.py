import pandas as pd
import numpy as np

def feature_obs(dataframe):
    """ Recieve a pandas dataframe and check for null elements, 
    (NaN in numeric arrays, None or NaN in object arrays,
    NaT in datetimelike). It returns a dictionary with keys 
    with information like message and a list of columns names
    that are missing information"""
    
    # Runnig validation of the argument.
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    
    # Assign values
    df = dataframe
    feat_to_look = []
    feat_to_kill = []
    for i in df.columns:
        #pct_miss[i] = (df[i].isnull().sum()/df[i].isnull().count())
        if (df[i].isnull().sum()/df[i].isnull().count()) > 0.05:
            feat_to_kill.append(i)
        elif (df[i].isnull().sum()/df[i].isnull().count()) > 0:
            feat_to_look.append(i)
        else:pass
    
    # Dictionary
                          
    result = {
    
        'message' : f'{len(feat_to_look)} features are missing less than 5% and {len(feat_to_kill)} columns are missing more than 5%',
        'features over 5%' : feat_to_kill,
        'features less than 5%' : feat_to_look, 
    
    }
    
    return result
        
                    
if __name__ ==  "__main__":
                          
    dataframe = pd.read_csv('out.csv')
    dictionary = feature_obs(dataframe)
                          
    message = dictionary['message']
    columns_missing_between_zero_and_five_pct = dictionary['features less than 5%']
    columns_missing_more_than_five_pct = dictionary['features over 5%']
                          
    print(message)
    print(columns_missing_between_zero_and_five_pct)
    print(columns_missing_more_than_five_pct)