# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime

os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
df=pd.read_csv('281.csv',header=0, parse_dates=['dttm_utc'])
df['5_min_interval'] = df['dttm_utc'].dt.time
#df['day']=df['dttm_utc'].dt.day
myarray = df[['timestamp','5_min_interval', 'value']]
sumevery3rows = myarray.groupby(myarray.index//3*3).sum() # sum every 3 rows
#day= myarray['day'] #keep the date based on the interval
#day1 = df[day.index % 3 == 0]
#day2 = day1['day']



#Datetime = pd.to_datetime(df_test["dttm_utc"]).astype(str)
#df_test['Time'] = df_test['Datetime'].apply(lambda x: datetime.datetime.strptime(x, '%H%M%S'))
#str_time = datetime.datetime.strptime(df_test.Datetime, "%H:%M:%S")

#generate date range
a=pd.date_range("00:00", "23:45", freq="15min").time.astype(str)
#make a dataframe and shift 00:00 to the bottom
time = pd.DataFrame(a)
target_row=time.loc[[0],:]
time=time.shift(-1)
time.iloc[-1] = target_row.squeeze()


#make time 366 times so can merge later
fifteen_min = pd.concat([time]*366)
fifteen_min.column=['15_interval']
#df['15_interval]=pd.to_datetime(df['fifteen_minute_interval']) #change df to datetime so it can sort based on time


#make sure all the index match up
sumevery3rows.index = range(len(sumevery3rows.index))
fifteen_min.index = range(len(fifteen_min.index))
#day2.index = range(len(day2.index))

#merge all the data 
result = pd.concat([fifteen_min, sumevery3rows], axis=1, join='inner')
#result.columns = ['day','15_min_interval','kWh']
#result['time of the day'] = [d.time() for d in result['15_min_interval']] #delete the today's date
#del result['15_min_interval']
#result = result[['day','time of the day','kWh']]
#cols = list(result.columns.values)
#print(result)
result.to_csv('new_281.csv')


##########################################################
#find sum and mean of the year
#sum_intervals= result.groupby('time of the day')[['kWh']].sum()
#mean_intervals= result.groupby('time of the day')[['kWh']].mean()
#print(sum_intervals)

#plot
#sum_intervals.index
#x=sum_intervals.index
#y=sum_intervals['kWh']
#fig = plt.figure(figsize=(20,10))
#plt.plot(x,y)
#fig.suptitle('2012 consumption in 15 minute interval')
#plt.xlabel('time of day')
#plt.ylabel('kWh')
#plt.ylim([0,25000])
#plt.xlim(['0:00','23:45'])
#ax = plt.axes()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(3600))
#fig.savefig('281.jpg')







