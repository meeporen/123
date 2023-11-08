from fastapi import Request, FastAPI
import requests
from bs4 import BeautifulSoup




app = FastAPI()

@app.get("/")
def parser(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "lxml")
    
    data = soup.find("div", class_="mw-parser-output").text
    return (data)


