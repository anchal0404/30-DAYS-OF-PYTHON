import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.horoscope.com/us/index.aspx")

soup= BeautifulSoup(req.content,"html.parser")

print(soup.get_text())
