# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:29:15 2018

@author: apb38
"""

import pandas as pd
#import numpy as np
import os
#import datetime
#import csv
#import sys
#import pytz

#os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/meta')
#
#data = pd.read_csv('all_sites.csv')
#groceries = data[data['SUB_INDUSTRY'] == 'Grocer/Market']
#LA_groceries = groceries[groceries['TIME_ZONE'] == 'America/Los_Angeles']
#LA_groceries = LA_groceries.reset_index()
#
##testing if forloops work
#
os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
#read dttm_utc as datetime
df_test=pd.read_csv('281.csv',header=0, parse_dates=['dttm_utc'])
#generate date range
a=pd.date_range("00:00", "23:45", freq="15min").time.astype(str)
#make a dataframe and shift 00:00 to the bottom
time = pd.DataFrame(a)
target_row=time.loc[[0],:]
time=time.shift(-1)
time.iloc[-1] = target_row.squeeze()

#df_test['just_time'] = df_test['dttm_utc'].dt.time
df_test=pd.read_csv('281.csv',header=0,parse_dates=['dttm_utc'])
(timestamp,	dttm_utc,	value,	estimated,	anomaly) = line.split(',')
# convert the string into a datetime object
df_test['dttm_utc']= pd.to_datetime[df_test['dttm_utc']]
df_test['dttm_utc'].dt

file = open('281.csv')
next(file)

import datetime
file = open('281.csv')
next(file)

for line  in file:
    (timestamp,	dttm_utc,	value,	estimated,	anomaly) = line.split(',')
    isoTime = datetime.datetime.fromtimestamp(int(timestamp))
    print (isoTime)
#    print(isoTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-07:00'))

#can use this later:
#from datetime import datetime, timedelta
#
#def datetime_range(start, end, delta):
#    current = start
#    while current < end:
#        yield current
#        current += delta
#
#dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
#       datetime_range(datetime(2016, 9, 1, 7), datetime(2016, 9, 1, 9+12), 
#       timedelta(minutes=15))]

#print(dts)


#df281.drop(df281.columns[[0,3,4]], axis=1, inplace=True)
#new_df281 = df281.assign(UniqueID='281')
#final_df281 = new_df281.rename(columns={'dttm_utc':'DateTime','value':'Usage_KWH'})
#print(final_df281)


#for i in range(len(LA_groceries)):
#    lat = LA_groceries.loc[i,'LAT']
#    lon = LA_groceries.loc[i,'LNG']
#    site_id = LA_groceries.loc[i,'SITE_ID']
#    year = 2012
#    print( site_id )
    
#os.chdir('C:/Users/apb38/Desktop/DR/datasets')
#data=pd.read_csv('SampleFileFormat.csv')
#data['DateTime']=pd.to_datetime[data['DateTime']]
#data['dttm_iso8601'] = datetime.datetime.strptime(data['DateTime'], '%Y-%m-%s %h:%m:%s').isoformat()

#cant rely on timestamp....


#utc_time = datetime.datetime(2014, 1, 24, 0, 32, 30, 998654)
#utc_dt = utc_time.replace(tzinfo=pytz.utc) # make it timezone aware
#pc_dt = utc_dt.astimezone(pytz.timezone('America/Los_Angeles')) # convert to PST
#
#print(pc_dt.strftime('%Y-%m-%d %H:%M:%S.%f %Z%z'))
#
#import pytz
#
#utc_time = datetime.datetime(data['DateTime'])
#utc_dt = utc_time.replace(tzinfo=pytz.utc) # make it timezone aware
#pc_dt = utc_dt.astimezone(pytz.timezone('America/Los_Angeles')) # convert to PST
#
#print(pc_dt.strftime('%Y-%m-%d %H:%M:%S.%f %Z%z'))

