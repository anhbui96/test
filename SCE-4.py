# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:40:06 2018

@author: apb38
"""
#code to change to ISO format

import pandas as pd
import numpy as np
import os
import datetime
import csv
import sys
import pytz

#need a little more with logic and it should work well
os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
file = open('281.csv')
next(file)

result=[]

def ISOFormatedTime():
#    os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
#    file = open('281.csv')
#    next(file)
    # get the fist column as "timestamp"
    (timestamp,	dttm_utc,	value,	estimated,	anomaly) = line.split(',')

    # convert the string into a datetime object
    PythonTime = datetime.fromtimestamp(int(timestamp))
#
#    Month=PythonTime.month
#    Day=PythonTime.day
#    Hour=PythonTime.hour
##    ISOFormatedTime=PythonTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z+08:00')
##    Minute=PythonTime.minute
#    
#    InDayLightSavings=True
# 
#    if (Month<3): InDayLightSavings=False
#
#    if (Month==3) and (Day<10) and (Hour<17): InDayLightSavings=False
#
#    if (Month>11): InDayLightSavings=False
#
#    if (Month==11) and (Day>4) and (Hour>=2): InDayLightSavings=False
#    
#    if (InDayLightSavings):
    ISOFormatedTime=PythonTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z+09:00')
    
#    if (Month==11) and (Day>=4) and (Hour>=2):
#       PythonTime=PythonTime+datetime.timedelta(hours=1)
       
#    print(PythonTime.year)
#    print(PythonTime.month)
#    print(PythonTime.day)
#    print(PythonTime.hour)    
    
    ISOFormatedTime=PythonTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-08:00')
    return(ISOFormatedTime)
    
for line in file:
    result.append(ISOFormatedTime())
    
iso_8601= pd.DataFrame({'time_daylight_savings':result})
iso_8601.to_csv('iso_8601.csv')   
    # onvert to ISO String formatted time
#    ISOFormatedTime=PythonTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-07:00')
#    print(ISOFormatedTime)
