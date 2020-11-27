#!/usr/bin/env python
# coding: utf-8

# In[112]:


### yapılması planlanan
# bir şehrin 1 aylık/1 yıllık vs sıcaklık değerlerini bul onların üzerinden işlem yap
# en az 500 veri olma gerekliliğini bir şekilde tamamla


# In[113]:


#bs4 parsing
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import sys

# In[114]:


# tanımlamalar

# url üzerinden site verilerini çek
# sehir ismine göre farklı linkleri çek
city_input = sys.argv[1]
url = 'https://weather.com/tr-TR/weather/monthly/l/453cfbbd56d2feadb92b63729bbdfb0e278db70a2bae2d700e3c2a20c8efb7ae'
webpage = requests.get(url)

# çekilen verileri BS üzerinden tanıml
soup = BS(webpage.content, 'html.parser')
if soup:
    print('thumbs up')


# In[117]:


# defining
# yılın hangi ayında olduğunu bul
# çıktı: kasım 2020
month_of_the_year = soup.find('option', selected=True)

# haftanın hangi günü olduğunu bul
# çıktı: Pazartesi, Salı, Çarşamba...
### !!! günleri for döngüsü içinde komple olarak geçirmek lazım
# aksi takdirde sadece bir tane gün değerini gönderiyor
day_of_the_week = soup.find_all('dt')
days_name = []
for day in day_of_the_week:
    days_name.append(day.string)

# ayın günlerini al (hepsini, aylık gösterim olacağından dolayı)
# çıktı: 1, 2, 3..
dayCells = soup.find_all('div', attrs={'class': 'date'})

# alınan günlerde yaşanan sıcaklıklar
dayTemps = soup.find_all('div', attrs={'class': 'temp hi'})


#spliting
month = month_of_the_year.text.split()
dayList = [x.text for x in dayCells]
dayTemp = [x.text for x in dayTemps]

# belirli günleri ve o günlerdeki sıcaklıkları index temelli olarak birleştir
day_temp = list(zip(dayList, dayTemp))



#calling
#month
#day_temp
#days_name

from pprint import pprint
pprint(month)
pprint(day_temp)
pprint(days_name)
