#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import re
import glob, os    

# use data from first two months, "./PWR-WiFi/**" will take all the folders
path = "./PWR-WiFi/2015-0[1, 2]"


# get all files containing statistics
all_files = glob.glob(os.path.join(path, 'statystyki-wifi*.csv'), recursive=True)  

#filter not matching files
all_files = list(filter(lambda x: re.search('(statystyki-wifi-)\d\d\d\d[-]\d\d[-]\d\d.(csv)', x), all_files))

# read and concatenate data from all files
df_from_each_file = (pd.read_csv(f, header=None, sep=';', engine='python') for f in all_files)
df = pd.concat(df_from_each_file, ignore_index=True)


# In[4]:


# give columns the names
df.columns = ['datetime', 'location', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6','column_7', 'column_8', 
              'column_9', 'column_10', 'column_11', 'column_12', 'column_13','column_14', 'column_15', 'column_16',
             'column_17', 'column_18', 'column_19', 'column_20', 'column_21', 'column_22']

# trim the last semicolon in .csv treated by pandas as a column
df = df.loc[:, :'column_21']
df

