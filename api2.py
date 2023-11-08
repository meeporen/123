from fastapi import Request, FastAPI 
import collections
import uvicorn
import requests


app = FastAPI()


@app.get("/")

async def get_text(text: str):
    res = requests.get("http://127.0.0.1:8000/", params={"url": text})
    words = res.text.split()
    counter = collections.Counter(words)
    most_common, occurrences = counter.most_common()[0]
    longest = max(words, key=len)
    return(most_common,longest)
