# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:45:25 2018

@author: apb38
"""
##########
#SCE format
import os
import pandas as pd
import datetime

os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
#read csv file
df=pd.read_csv('281.csv',header=0, parse_dates=['dttm_utc'])
#make a column of just time
df['5_min_interval'] = df['dttm_utc'].dt.time

#make an array of needed value
myarray = df[['5_min_interval', 'value']]
sumevery3rows = myarray.groupby(myarray.index//3*3).sum() # sum every 3 rows


#generate date range
a=pd.date_range("00:00", "23:45", freq="15min").time.astype(str)
#make a dataframe and shift 00:00 to the bottom
time = pd.DataFrame(a)
target_row=time.loc[[0],:]
time=time.shift(-1)
time.iloc[-1] = target_row.squeeze()

#make time 366 times so can merge later
fifteen_min = pd.concat([time]*366)
fifteen_min.columns=['15_interval']

#make sure all the index match up
sumevery3rows.index = range(len(sumevery3rows.index))
fifteen_min.index = range(len(fifteen_min.index))

#merge all the data 
fifteen_min_data = pd.concat([fifteen_min, sumevery3rows], axis=1, join='inner')
pd.DataFrame(fifteen_min_data)

from datetime import timedelta
#stack: Generate 1/1/2012 00:15:00 to 3/11/2012 01:55:00
def perdelta(start, end, delta):
    curr = start
    while curr <=end:
        yield curr
        curr += delta
dtfmt = '%Y-%m-%d %H:%M'

a = '2012-1-1 00:15'
b = '2012-3-11 01:45'

start = datetime.datetime.strptime(a,dtfmt)
end = datetime.datetime.strptime(b,dtfmt)

stack=[]
for result in perdelta(start , end, timedelta(minutes=15)):
    stack.append(str(result))

print(stack)
stack=pd.DataFrame(stack)

#stack1: Generate 3/11/2012 03:00:00 to 11/4/2012 01:45:00
def perdelta1(start1, end1, delta1):
    curr1 = start1
    while curr1 <=end1:
        yield curr1
        curr1 += delta1
dtfmt = '%Y-%m-%d %H:%M'

a1 = '2012-3-11 03:00'
b1 = '2012-11-4 01:45'
start1 = datetime.datetime.strptime(a1,dtfmt)
end1 = datetime.datetime.strptime(b1,dtfmt)

stack1=[]
for result in perdelta1(start1 , end1, timedelta(minutes=15)):
    stack1.append(str(result))

stack1=pd.DataFrame(stack1)

#stack2: Generate 11/4/2012 02:00:00 to 11/4/2012 02:45:00
def perdelta2(start2, end2, delta2):
    curr2 = start2
    while curr2 <=end2:
        yield curr2
        yield curr2
        curr2 += delta2
dtfmt = '%Y-%m-%d %H:%M'


a2 = '2012-11-4 02:00'
b2 = '2012-11-4 02:45'
start2 = datetime.datetime.strptime(a2,dtfmt)
end2 = datetime.datetime.strptime(b2,dtfmt)

stack2=[]
for result in perdelta2(start2 , end2, timedelta(minutes=15)):
    stack2.append(str(result))

stack2=pd.DataFrame(stack2)


#stack 3: Generate 11/4/2012 03:00:00 to 1/1/2013 00:00:00
def perdelta3(start3, end3, delta3):
    curr3 = start3
    while curr3 <=end3:
        yield curr3   
        curr3 += delta3
dtfmt = '%Y-%m-%d %H:%M'

a3 = '2012-11-4 03:00'
b3 = '2013-1-1 00:00'

start3 = datetime.datetime.strptime(a3,dtfmt)
end3 = datetime.datetime.strptime(b3,dtfmt)

stack3=[]
for result in perdelta3(start3 , end3, timedelta(minutes=15)):
    stack3.append(str(result))

stack3=pd.DataFrame(stack3)


SCE_format=stack.append([stack1,stack2,stack3])
pd.DataFrame(SCE_format)
SCE_format.columns=['daylightsavin_format']
SCE_format.index=range(len(SCE_format.index)) #make sure index is not jumble up after append
final=pd.merge(SCE_format,fifteen_min_data,left_index=True,right_index=True)

final['daylightsavin_format']=pd.to_datetime(final['daylightsavin_format'],format= '%Y-%m-%d %H:%M:%S')
#final['daylightsavin_format'].astype(str)
final.to_csv('SCE_format.csv')

#####################################################
#ISO daylight saving 
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
ISOtime = []
def ISOFormatedTime():
    (Index,timestamp,dttm_utc)=line.split(',')
    isoTime = datetime.datetime.fromtimestamp(int(timestamp))
    return(isoTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-08:00'))
    
for line in file:
    ISOtime.append(ISOFormatedTime())
    
iso_8601= pd.DataFrame({'ISO_8601_time':ISOtime})
iso_8601.to_csv('iso_8601.csv') 

#2am repeat
#repeat_time = iso_8601.iloc[29567:29571]
#Generate 11/4/2012 03:00:00 to 1/1/2013 00:00:00
after_daylight=iso_8601.iloc[29575:]

final_ISO=before_daylight.append([daylight,after_daylight])
final_ISO=final_ISO.reset_index()
final_ISO.to_csv('final_ISO.csv')

final_model_site=pd.merge(final_ISO,final,left_index=True,right_index=True)
#####################################test

load = pd.DataFrame(fifteen_min_data['value'])
load = load.assign(CustomerID= str(281))
site_281=pd.merge(SCE_format,load,left_index=True,right_index=True)
site_281.to_csv('site_281.csv')