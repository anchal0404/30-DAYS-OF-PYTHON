import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen("https://www.horoscope.com/us/index.aspx")
soup = bs(page)

names = soup.body.findAll('a')
function_names= re.findall('id="src-hp-.\w+',str(names))
function_names=[item[11:] for item in function_names]

description=soup.body.find_all('p')
function_usage=[]

for item in description:
    item=item.text
    item=item.replace('/n','')
    function_usage.append(item)
print(function_names[:12])
print(function_usage[:12])