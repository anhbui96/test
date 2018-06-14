# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:55:02 2018

@author: apb38
"""

import os 
import pandas as pd
import pytz
from datetime import datetime

os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
df= pd.read_csv('281.csv',header=0, parse_dates=['dttm_utc'])
#df['5_min_interval'] = df['dttm_utc'].dt.time
#sumfor3rows = df['value'].groupby(df['value'].index//3*3).sum()

#change to dailight saving
for i in range(len(df)):
    timestamp=df.loc[i,'timestamp']
#    print(timestamp)
    
res=[]
def ISOformat():
    tz = pytz.timezone('America/Los_Angeles')
    print(datetime.datetime.fromtimestamp(1325376300, tz).isoformat())
#    isoTime = datetime.datetime.fromtimestamp(int(timestamp))
#    ISOFormatedTime=isoTime.strftime('%Y-%m-%dT%H:%M:%SZ')
#    return(ISOFormatedTime)

for i in range(len(df)):
    res.append(ISOformat())
    
#make a dataframe of the ISO 8601
iso_8601_test= pd.DataFrame({'time_daylight_savings':res})


pytz.timezone('US/Pacific')


ISO_fifteen=pd.merge(SCE_format,fifteen_min_data,left_index=True,right_index=True)
myarray = df[['5_min_interval', 'time_daylight_savings']]


myarray.to_csv('iso_8601.csv')

os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/test')
df281=pd.read_csv('281-data.csv')