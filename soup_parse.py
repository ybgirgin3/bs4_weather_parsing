#bs4 parsing
from bs4 import BeautifulSoup as BS
import requests


# tanımlamalar

# url üzerinden site verilerini çek
url = "https://weather.com/en-IN/weather/tenday/l/453cfbbd56d2feadb92b63729bbdfb0e278db70a2bae2d700e3c2a20c8efb7ae"
webpage = requests.get(url)

# çekilen verileri BS üzerinden tanıml
soup = BS(webpage.content, 'html.parser')
if soup:
    print('thumbs up')
else:
    print('ya internet gitti ya site çöktü')

# blokların tanımlanması
# bana lazım olan blocklar:
#   anlık sıcaklık
#   önceki sıcaklıklar (her şehir için 10 tane)
temp_block = soup.find('span', attrs={'class': 'DailyContent--temp--_8DL5'})

# eski sıcaklık değerlerini classları aynı fakat id'leri farklı
old_temp_values = soup.find('h2', attrs={'class': 'DetailsSummary--daypartName--1Mebr'})

# blocklardaki textlerin alınması
temp = temp_block.text.strip()
old_temp = 


