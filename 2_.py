#!/usr/bin/env python
# coding: utf-8

# In[78]:


### yapılması planlanan
# bir şehrin 1 aylık/1 yıllık vs sıcaklık değerlerini bul onların üzerinden işlem yap
# en az 500 veri olma gerekliliğini bir şekilde tamamla


# In[79]:


#bs4 parsing
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import numpy as np
import csv


# In[80]:


# tanımlamalar

# url üzerinden site verilerini çek
#url = "https://weather.com/en-IN/weather/tenday/l/453cfbbd56d2feadb92b63729bbdfb0e278db70a2bae2d700e3c2a20c8efb7ae"
url = 'https://weather.com/tr-TR/weather/monthly/l/453cfbbd56d2feadb92b63729bbdfb0e278db70a2bae2d700e3c2a20c8efb7ae'
webpage = requests.get(url)

# çekilen verileri BS üzerinden tanıml
soup = BS(webpage.content, 'html.parser')
if soup:
    print('thumbs up')


# In[81]:


# defining
# yılın hangi ayında olduğunu bul
# çıktı: kasım 2020
month_of_the_year = soup.find('option', selected=True)

# haftanın hangi günü olduğunu bul
# çıktı: Pazartesi, Salı, Çarşamba...
### !!! günleri for döngüsü içinde komple olarak geçirmek lazım
# aksi takdirde sadece bir tane gün değerini gönderiyor
# günleri el ile yaz
"""
day_of_the_week = soup.find_all('dt')
days_name = []
for day in day_of_the_week:
    days_name.append(day.string)
"""

days_name = ['pzrtsi', 'salı', 'çrş', 'prş', 'cuma', 'cts', 'pzr' ]
# ayın günlerini al (hepsini, aylık gösterim olacağından dolayı)
# çıktı: 1, 2, 3..
alldays = soup.find_all('div', attrs={'class': 'date'})

# alınan günlerde yaşanan sıcaklıklar
alltemp = soup.find_all('div', attrs={'class': 'temp hi'})


#spliting
# KASIM 2020
month = month_of_the_year.text.split()
# 1, 2, 3
dayList = [x.text for x in alldays]
# 15, 17, 14, 15
dayTemp = [x.text for x in alltemp]
remove_sign = lambda x: x.replace("°","")
dayTemp = list(map(remove_sign, dayTemp))
del dayTemp[-1]


# In[82]:


"""
index_label = KASIM-2020 -> bunu csv'ye yazarken yazacağız
index = 1,2,3,4
column = pz, pzts, salı, çarş
data = 15, 14, 15, 16
"""


# In[83]:


# günleri en tepedeki title satırınına yazdırdıktan sonra
# her bir gün değeri için 7'de birini yazdır


# In[84]:


arr = np.array(dayTemp)
arr = arr.reshape(5,7)


# In[85]:


df = pd.DataFrame(arr, columns= days_name)
df.index += 
print(df)
#df.to_csv('sakarya_weather.csv')

