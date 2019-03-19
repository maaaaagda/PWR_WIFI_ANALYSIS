#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import re
import glob, os    

# use data from first two months, "./PWR-WiFi/**" will take all the folders
path = "./PWR-WiFi/2015-0[1, 2]"


# get all files containing statistics
all_files = glob.glob(os.path.join(path, 'statystyki-wifi*.csv'), recursive=True)  

#filter not matching files
all_files = list(filter(lambda x: re.search('(statystyki-wifi-)\d{4}[-]\d{2}[-]\d{2}.(csv)', x), all_files))

# read and concatenate data from all files
df_from_each_file = (pd.read_csv(f, header=None, sep=';', engine='python') for f in all_files)
df = pd.concat(df_from_each_file, ignore_index=True)

df.head()


# In[66]:


# trim the last semicolon in .csv treated by pandas as a column
df = df.iloc[:, :22]

# set columns names
df.columns = ['datetime', 'location', 'bsnApIfNoOfUsers',
'bsnAPIfDot11TransmittedFragmentCount',
'bsnAPIfDot11MulticastTransmittedFrameCount',
'bsnAPIfDot11RetryCount',
'bsnAPIfDot11MultipleRetryCount',
'bsnAPIfDot11FrameDuplicateCount',
'bsnAPIfDot11RTSSuccessCount',
'bsnAPIfDot11RTSFailureCount',
'bsnAPIfDot11ACKFailureCount',
'bsnAPIfDot11ReceivedFragmentCount',
'bsnAPIfDot11MulticastReceivedFrameCount',
'bsnAPIfDot11FCSErrorCount',
'bsnAPIfDot11TransmittedFrameCount',
'bsnAPIfDot11WEPUndecryptableCount',
'bsnAPIfDot11FailedCount',
'bsnAPIfLoadRxUtilization',
'bsnAPIfLoadTxUtilization',
'bsnAPIfLoadChannelUtilization',
'bsnAPIfLoadNumOfClients',
'bsnAPIfPoorSNRClients']

# drop rows with missing values
df.dropna(inplace=True)

# change data types of rows
df = df.astype({c: 'int64' for c in df.columns if c != 'datetime' and c != 'location' })

df.head()


# In[ ]:




