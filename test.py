# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:00:27 2018

@author: apb38
"""

import pandas as pd
import numpy as np
import os
import datetime
import csv
import sys

os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/meta')

data = pd.read_csv('all_sites.csv')
groceries = data[data['SUB_INDUSTRY'] == 'Grocer/Market']
LA_groceries = groceries[groceries['TIME_ZONE'] == 'America/Los_Angeles']
LA_groceries = LA_groceries.reset_index()

#testing if forloops work

#testing if forloops work
os.chdir('C:/Users/apb38/Desktop/DR/datasets/enernoc-comm/enernoc-comm/enernoc-comm/csv')
for i in range(len(LA_groceries)):
    lat = LA_groceries.loc[i,'LAT']
    lon = LA_groceries.loc[i,'LNG']
    site_id = LA_groceries.loc[i,'SITE_ID']
    year = 2012
    print( site_id )



def get_weather(lat,lon,year):
    #function call
    api_key = 'sFLzhDFG2hyThFRmHO6FbrBfMg9X8FFtfbdBEYpF'
    attributes = 'ghi,dni,dhi,surface_air_temperature_nwp,surface_relative_humidity_nwp,wind_speed_10m_nwp,total_precipitable_water_nwp,surface_pressure_background'
    leap_year = 'true'
    interval = '30'
    utc = 'false'
    your_name = 'Anh+Bui'
    reason_for_use = 'Research'
    your_affiliation = 'Schatz+Energy+Research+Center'
    your_email = 'apb38@humboldt.edu'
    mailing_list = 'false'
    url = 'http://developer.nrel.gov/api/solar/nsrdb_0512_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
    
    # Return just the first 2 lines to get metadata:
    info = pd.read_csv(url, nrows=1)
    # See metadata for specified properties, e.g., timezone and elevationlat,
    latitude= info['Latitude']
    longitude = info['Longitude']
    site_id = LA_groceries.loc[i,'SITE_ID']
    
    # Return all 
    df = pd.read_csv(url,skiprows=2)
    # Set the time index in the pandas dataframe:
#    df = df.set_index(pd.date_range(start='1-1-2012 00:00:00', end='12-31-2012 23:30:00', freq='30T'))
    df.rename(columns={'Relative Humidity':'Relative_Humidity','Wind Speed':'Wind_Speed','Precipitable Water':'Precipitable_Water'},inplace = True)
    df.to_csv(str(site_id)+'weather.csv')
    #put into csv
    #import io
    #for i in LA_groceries.index(16):
     #  with io.open("weather_file_" + str(i) + ".csv", 'w', encoding='utf-8') as f:
      #     f.write(str(func(i))
    
    #put lat and long on top of file
    with open(str(site_id)+'weather.csv',newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open(str(site_id)+ 'weather.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['site_id', str(site_id),'lat', float(latitude),'lon', float(longitude)])
        w.writerows(data)




for i in range(len(LA_groceries)):
    get_weather(LA_groceries.loc[i,'LAT'],LA_groceries.loc[i,'LNG'],2012)