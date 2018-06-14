# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:48:41 2018

@author: apb38
"""


import pandas as pd
import numpy as np
import os
import datetime
import csv
import sys
import pytz

#original ISO-8601 thought process
os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
file = open('281.csv')
next(file)
  
for line in file:
    # get the fist column as "timestamp"
    (timestamp,	dttm_utc,	value,	estimated,	anomaly) = line.split(',')
    
    # convert the string into a datetime object
    PythonTime = datetime.datetime.fromtimestamp(int(timestamp))
    
    Year=PythonTime.year
    Month=PythonTime.month
    Day=PythonTime.day
    Hour=PythonTime.hour
    
    InDayLightSavings=True
 
    if (Month<3): InDayLightSavings=False

    if (Month==3) and (Day<11): InDayLightSavings=False

    if (Month>11): InDayLightSavings=False

    if (Month==11) and (Day>4): InDayLightSavings=False
    
    if (InDayLightSavings):
        PythonTime=PythonTime-datetime.timedelta(hours=1)
    
    if (Month==11) and (Day>=4) and (Hour>=2):
       PythonTime=PythonTime+datetime.timedelta(hours=1)
#        
#    print(PythonTime.year)
#    print(PythonTime.month)
#    print(PythonTime.day)
#    print(PythonTime.hour)
    print (PythonTime)
    
    # onvert to ISO String formatted time
#    ISOFormatedTime=PythonTime.strftime('%Y-%m-%dT%H:%M:%SZ%Z-07:00')
#    print(ISOFormatedTime)
