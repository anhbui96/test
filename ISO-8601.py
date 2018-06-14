# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:03:10 2018

@author: apb38
"""

import pandas as pd
import numpy as np
import os
import datetime
import pytz
from datetime import timedelta 

os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')

df1= pd.read_csv('281.csv',header=0,skiprows=2)
#only keep the 15 min interval 
df2 = df1[df1.index % 3 == 0] 
#rename columns
df2.columns=['timestamp','dttm_utc','Usage_KWH','4','5']
del df2['4'] 
del df2['5']
del df2['Usage_KWH']
df2=df2.reset_index()
del df2['index']
#change to ISO8601 format -8:00
res = df2['timestamp'].apply(lambda time: pd.Timestamp(time,
                                          tz='America/Los_Angeles',unit='s').isoformat())
ISO_non_dls= pd.DataFrame({'ISO_8601_time':res})
#change to ISO8601 format -7:00
res2 = df2['timestamp'].apply(lambda time: pd.Timestamp(time,
                                          tz='America/Phoenix',unit='s').isoformat())
ISO_dls= pd.DataFrame({'ISO_8601_time':res2})

#to find where to cut
ISO_non_dls.to_csv('ISO_LA.csv')
ISO_dls.to_csv('ISO_PHX.csv')
df2.to_csv('df2.csv')

#real cut
#Generate 1/1/2012 00:15:00 to 3/11/2012 01:45:00
before_daylight=ISO_non_dls.iloc[0:6727] #this is correct
#Generate 3/11/2012 03:00:00 to 11/4/2012 01:45:00
daylight=ISO_dls.iloc[6727:29575]


file = open('df1.csv')
next(file)
result = []
def ISOFormatedTime():
    (Index,timestamp,dttm_utc)=line.split(',')
    isoTime = datetime.datetime.fromtimestamp(int(timestamp))
    return(isoTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-08:00'))
    
for line in file:
    result.append(ISOFormatedTime())
    
iso_8601= pd.DataFrame({'ISO_8601_time':result})
iso_8601.to_csv('iso_8601.csv') 

#2am repeat
#repeat_time = iso_8601.iloc[29567:29571]
#Generate 11/4/2012 03:00:00 to 1/1/2013 00:00:00
after_daylight=iso_8601.iloc[29575:]

final_ISO=before_daylight.append([daylight,after_daylight])
final_ISO=final_ISO.reset_index()
final_ISO.to_csv('final_ISO.csv')
#####################################test
