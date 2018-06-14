# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:22:54 2018

@author: apb38
"""


import pandas as pd
import numpy as np
import os
import datetime
import csv
import sys
import pytz

#probably dont need this
#just testing on the Python time and does not work that well
os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
file = open('281.csv')
next(file)

result=[]

def PythonTime():
#    os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
#    file = open('281.csv')
#    next(file)
    # get the fist column as "timestamp"
    (timestamp,	dttm_utc,	value,	estimated,	anomaly) = line.split(',')
    
    # convert the string into a datetime object
    PythonTime = datetime.datetime.fromtimestamp(int(timestamp))

    Month=PythonTime.month
    Day=PythonTime.day
    Hour=PythonTime.hour
#    Minute=PythonTime.minute
    
    InDayLightSavings=True
 
    if (Month<3): InDayLightSavings=False

    if (Month==3) and (Day<11) and (Hour<2): InDayLightSavings=False

    if (Month>11): InDayLightSavings=False

    if (Month==11) and (Day>4) and (Hour>=2): InDayLightSavings=False
    
    if (InDayLightSavings):
        PythonTime=PythonTime-datetime.timedelta(hours=1)
    
    if (Month==11) and (Day>=4) and (Hour>=2):
       PythonTime=PythonTime+datetime.timedelta(hours=1)
       
#    print(PythonTime.year)
#    print(PythonTime.month)
#    print(PythonTime.day)
#    print(PythonTime.hour)    
    
#    ISOFormatedTime=PythonTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-07:00')
#    return(ISOFormatedTime)
    
for line in file:
    result.append(PythonTime())
    
python_time= pd.DataFrame({'time_daylight_savings':result})
python_time.to_csv('python_time.csv')
    # onvert to ISO String formatted time
#    ISOFormatedTime=PythonTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-07:00')
#    print(ISOFormatedTime)
