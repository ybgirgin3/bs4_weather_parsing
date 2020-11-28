#!/usr/bin/env python
# coding: utf-8


### yapılması planlanan
# bir şehrin 1 aylık/1 yıllık vs sıcaklık değerlerini bul onların üzerinden işlem yap
# en az 500 veri olma gerekliliğini bir şekilde tamamla



#bs4 parsing
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import csv



# tanımlamalar

# url üzerinden site verilerini çek
#url = "https://weather.com/en-IN/weather/tenday/l/453cfbbd56d2feadb92b63729bbdfb0e278db70a2bae2d700e3c2a20c8efb7ae"
url = 'https://weather.com/tr-TR/weather/monthly/l/453cfbbd56d2feadb92b63729bbdfb0e278db70a2bae2d700e3c2a20c8efb7ae'
webpage = requests.get(url)

# çekilen verileri BS üzerinden tanıml
soup = BS(webpage.content, 'html.parser')
if soup:
    print('thumbs up')



# defining
# yılın hangi ayında olduğunu bul
# çıktı: kasım 2020
month_of_the_year = soup.find('option', selected=True)

# haftanın hangi günü olduğunu bul
# çıktı: Pazartesi, Salı, Çarşamba...
### !!! günleri for döngüsü içinde komple olarak geçirmek lazım
# aksi takdirde sadece bir tane gün değerini gönderiyor

"""
## günleri datetime modülü üzerinden alacağım 
#### günleri el ile yazacağım
day_of_the_week = soup.find_all('dt')
days_name = []
for day in day_of_the_week:
    days_name.append(day.string)
"""

days_name = ['pazar', 'pzrtesi', 'salı', 'çrşmb', 'prşmb', 'cuma', 'cmt']
# ayın günlerini al (he


"""
KASIM-2020  'pazar', 'pzrtesi', 'salı', 'çrşmb', 'prşmb', 'cuma', 'cmt'
1           15          17          15      10
2
3
.
.
.
.
"""
# çıktı: 1, 2, 3..
#dayCells = soup.find_all('div', attrs={'class': 'date'})
### daycell kısmında gerek yok direk olarak 31 tane tanımla geç 


# alınan günlerde yaşanan sıcaklıklar
dayTemp_div = soup.find_all('div', attrs={'class': 'temp hi'})


#spliting
month = month_of_the_year.text.split()
# dayList 1'den 31'e kadar sayılar olacak
#dayList = [x.text for x in dayCells]
dayList = [num for num in range(1,32)]
dayTemp = [x.text for x in dayTemp_div]

# belirli günleri ve o günlerdeki sıcaklıkları index temelli olarak birleştir
day_temp = list(zip(dayList, dayTemp))


