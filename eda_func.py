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
        
def missing(dataframe):
    """Takes a pandas df as an argument, and returns
    another one with information about the NaN in numeric 
    arrays, None or NaN in object arrays, NaT in datetimelike"""
                    
    # Running validation of the argument
<<<<<<< HEAD
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.
=======
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    
    # Assign values
    df = dataframe
>>>>>>> missing
    
    # Assign values
    total_missing = df.isnull().sum().sort_values(ascending=False)
    percent_missing = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total_missing, percent_missing], axis=1, keys=['Total', 'Percent'])
<<<<<<< HEAD
    return(missing_data.head(len(df.columns)))
=======
    
    return(missing_data.head(len(df.columns)))

>>>>>>> missing
