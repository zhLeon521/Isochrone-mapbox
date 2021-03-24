# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:52:14 2021

@author: szu
"""

import urllib
import urllib.request
import pandas as pd
import time
zhandian = pd.read_csv('zhandian.csv',sep=',',encoding='gbk')

for i in range(len(zhandian)):
    
    Lng = zhandian['wgs84_lng'].iloc[i]
    Lat = zhandian['wgs84_lat'].iloc[i]
    print(Lng,Lat)
    
    name = zhandian['name'].iloc[i] #保存文件名用的


    YOUR_MAPBOX_ACCESS_TOKEN = 'your mapbox access token' # 换成你的token
    # # 15min-60min
    # url = 'https://api.mapbox.com/isochrone/v1/mapbox/walking/{}%2C{}?contours_minutes=15%2C30%2C45%2C60&polygons=true&access_token={}'.format(Lng,Lat,YOUR_MAPBOX_ACCESS_TOKEN)
    
    # 15min-60min
    url = 'https://api.mapbox.com/isochrone/v1/mapbox/walking/{}%2C{}?contours_minutes=15&polygons=true&access_token={}'.format(Lng,Lat,YOUR_MAPBOX_ACCESS_TOKEN)
    
    

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    data = response.read().decode('utf-8')
    
    f = open("15min_isochrone/json/{}_{}.json".format(i,name),mode='w')
    f.write(data)
    f.close()
    print("json文件下载完毕")
    
    
    import geopandas as gpd
    data = gpd.read_file("15min_isochrone/json/{}_{}.json".format(i,name))
    data.to_file("15min_isochrone/shp/{}_{}".format(i,name))
    print("shp文件下载完毕")
    
    
    print("歇火30s")
    time.sleep(5)
    
    
    
    
    
    
    
    