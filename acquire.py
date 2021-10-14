import pandas as pd
import numpy as np
import os


def new_data():
    '''
    This function takes in 2 seperate csv files
    and merges them together
    then returns a merged pandas dataframe with that data
    '''
    emotify_df = pd.read_csv('emotify.csv')
    key_df = pd.read_csv('AudioKeychain_export.csv')
    emotify_df = emotify_df.rename(columns={'track id':'track_id', ' genre': 'genre', ' amazement':'amazement', ' solemnity': 'solemnity', ' tenderness':'tenderness',
       ' nostalgia':'nostalgia', ' calmness':'calmness', ' power':'power', ' joyful_activation':'joyful_activation', ' tension':'tension',
       ' sadness':'sadness', ' mood':'mood', ' liked':'liked', ' disliked':'disliked', ' age':'age', ' gender':'gender',
       ' mother tongue':'mother_tongue'})
    key_df = key_df.rename(columns=str.lower)
    emotify_plus_df = pd.merge(emotify_df, key_df, left_on='track_id', right_on='track', how='left')
    emotify_plus_df = emotify_plus_df.drop(columns=['track', 'genre_y', 'filename'])
    
    
    return emotify_plus_df

########################## Clean and Prepare DF ########################

def prep_data(emotify_plus_df):
    '''
    This function takes in the newly aqcuired df
    and creates new columns/features out of combining or cutting existing columns
    It will also assign encoded columns for categorical values to be used later in modeling
    '''
    #reassigning df for ease
    df = emotify_plus_df

    #combining the induced emotions into three supercategories
    #supercategories are grouped as per GEMS, but renamed for clarity
    df['ind_sublime'] = df['amazement'] + df['solemnity'] + df['tenderness'] + df['nostalgia'] + df['calmness']
    df['ind_energy'] = df['power'] + df['joyful_activation']
    df['ind_unease'] = df['tension'] + df['sadness']
    
    #creating columns that will contain a 1 if any subcategory or 0 if no subcategory emotions were induced 
    #energy emotions
    col         = 'ind_energy'
    conditions  = [ df[col] >= 1, df[col] < 1 ]
    choices     = [ 1, 0 ]
    df["energized"] = np.select(conditions, choices, default=0)
    #sublime emotions
    col         = 'ind_sublime'
    conditions  = [ df[col] >= 1, df[col] < 1 ]
    choices     = [ 1, 0 ]
    df["feel_sublime"] = np.select(conditions, choices, default=0)
    #unease emotions
    col         = 'ind_unease'
    conditions  = [ df[col] >= 1, df[col] < 1 ]
    choices     = [ 1, 0 ]
    df["agitated"] = np.select(conditions, choices, default=0)

    #creating columns to represent if song is minor.
    #value 1 means the key is minor, value 0 means the key is major
    col         = 'key'
    conditions  = [ df[col].str.contains(r'(?!$)m'), df[col] != '%m' ]
    choices     = [ 1, 0 ]
    df["minor_key"] = np.select(conditions, choices, default=0)

    #creating a column containing cut value groups for tempo
    #0-90BPM: slow; 90-108BPM: medium; 108-156: fast; >156: very fast
    df['tempo'] = pd.cut(df.bpm, [0, 90, 108, 156, np.inf], labels=['slow', 'medium', 'fast', 'very_fast'])
    
    #filtering out unecessary columns and reassigning df for clarity
    df1 = df.filter(['track_id', 'genre_x', 'mood', 'age', 'gender', 'key', 'minor_key', 'tempo', 'liked', 'disliked',  'feel_sublime', 'agitated', 'energized'], axis=1)

    #creating dummy columns for modelng
    genre_dummies = pd.get_dummies(df1.genre_x, drop_first=True)
    df1 = pd.concat([df1, genre_dummies], axis=1)

    tempo_dummies = pd.get_dummies(df1.tempo, drop_first=True)
    df1 = pd.concat([df1, tempo_dummies], axis=1)

    return df1
