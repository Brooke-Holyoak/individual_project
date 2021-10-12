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