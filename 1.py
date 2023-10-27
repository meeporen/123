import requests 
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%B5%D1%80%D0%B1%D0%BB%D1%8E%D0%B6%D0%B8%D0%B9_%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81"


response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find("div", class_="mw-parser-output").text

print (data)