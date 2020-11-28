#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
#from sklearn.externals import joblib
import joblib
from sklearn.preprocessing import RobustScaler
import csv
import datetime
from sklearn.svm import SVR
import sklearn.svm as svm
from sklearn.linear_model import LinearRegression


# In[ ]:


#dataset from
#'https://www.meteoblue.com/en/weather/archive/export/basel_switzerland_2661604?daterange=2019-01-01%20to%202020-11-28&domain=NEMSAUTO&params%5B%5D=temp2m&params%5B%5D=relhum2m&params%5B%5D=wind%2Bdir10m&min=2019-01-01&max=2020-11-28&utc_offset=0&timeResolution=daily&temperatureunit=CELSIUS&velocityunit=KILOMETER_PER_HOUR&energyunit=watts&lengthunit=metric'


# In[ ]:


from datetime import datetime
# read dataset
dataset = 'basel_daily.csv'
df  = pd.read_csv(dataset, skiprows=9)
#df.drop(columns=['Temperature.1', 'Relative Humidity.1', 'Wind Speed.1'])


# In[116]:


def train_data():
    # gereksiz sütunları sil
    df.drop(columns=['Temperature.1', 'Relative Humidity.1', 'Wind Speed.1'])
    
    # tarihleri bilgisayarın anlayacağı şekle çevir
    df['timestamp'] = df['timestamp'].str.replace('T0000', '')
    return df['timestamp']

print(train_data())



# In[]:
    
df.timestamp = pd.to_datetime(df.timestamp, format='%Y%m%d', errors='coerce')

    
    
    
    
    