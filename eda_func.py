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

    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    
    # Assign values
    df = dataframe

    # Assign values
    total_missing = df.isnull().sum().sort_values(ascending=False)
    percent_missing = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total_missing, percent_missing], axis=1, keys=['Total', 'Percent'])
    
    return(missing_data.head(len(df.columns)))


def basic_info(dataframe):
    """Takes a pandas df as an argument, and prints
    basic information information about the dataset"""
    df = dataframe 
    print(df.head())
    print(df.info())
    
    
def invalid_df(dataframe: pd.DataFrame):
    """
    Take a pandas df as argument, looks for the items 
    in an invalid list. returns a pd df with
    the columns: column, nulls, invalids, 
    and the unique values.
    Args:
        df(pd.DataFrame): a pdDataFrame.
    """
    # Running validation on the argument recieved
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    df = dataframe
    invalid_list = [np.nan, None, [], {}, 'NaN', 'Null','NULL','None','NA','?','-', '--','.','', ' ', '   ']
    columnas_con_invalidos = []
    nan_or_nones = []
    invalids = []
    uniques = []
    invalid_dict = {
        'column': columnas_con_invalidos,
        'nulls': nan_or_nones,
        'invalids': invalids, 
        'unique_item': []
    }
    for c in df.columns:
        string_null = np.array([x in invalid_list[2:] for x in df[c]])
        columnas_con_invalidos.append(c)
        nan_or_nones.append((df[c].isnull().sum()))
        invalids.append(string_null.sum())
        uniques.append(df[c].unique())
        invalid_dict = {
        'columns': columnas_con_invalidos,
        'nulls': nan_or_nones,
        'invalids': invalids,
        'unique_item': uniques
        }
        
    result = pd.DataFrame(invalid_dict)
    return(result.head(len(df.columns)))
    
def siftdatatype(dataframe: pd.DataFrame):
    """
    Recive a pandas data frame as an argument
    returns a dictionary with a message and 
    keys categorical and numerical, the values
    are two list each corresponding to the keys.
    Args:
        df(pd.DataFrame): a pdDataFrame.
    """
    # Running validation on the argument recieved
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    df = dataframe
    # groupping columns with numbers, dtypes can increase in types len.
    num_features = df.select_dtypes(['int64', 'float64']).columns.to_list()
    # groupping object columns
    cat_features = df.select_dtypes(['object']).columns.to_list()
    lenghts = [len(num_features), len(cat_features)]
    elementos = [num_features, cat_features]
    results = {
        "message" : f"{lenghts[0]} features are numerical and {lenghts[1]} features are categorical.",
        "numerical" : elementos[0], 
        "categorical" : elementos[1]
    }
    return results

def filler_of_the_nans(technique, df, list_to_fill):
    """
    Fill in nans of a fill_list from a pandas df,
    the fill list should be defined by the technique to use. 
    The options are mean, median, mode or interpolation.

    Args:
        technique (list): a technique to use, from the list
        df(pd.DataFrame): a pdDataFrame.
        fill_list (pd.Series): pd.Series or list of Series with
        missing values. 
        
    """
    # Running validation on the argument recieved
    tecnicas = ('mean', 'median', 'interpolation', 'mode')
    assert type(df) == pd.DataFrame, f'{df} is not a pandas df.'
    assert technique in tecnicas, f'{technique} not in options:\
        [mean|median|interpolation|mode]'

    # Deffining and populating a dataframe
    dff = pd.DataFrame()
    dff = df.copy()

    if technique == 'mean':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].mean())
        return dff
    elif technique == 'median':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].median())
        return dff
    elif technique == 'interpolation':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].interpolate())
        return dff
    elif technique == 'mode':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].mode()[0])
        return dff
    else: return dff