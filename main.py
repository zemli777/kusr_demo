from typing import Union
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel
from pprint import pprint
from weather_pasr import get_weather, get_info
import uvicorn
import os
from dotenv import load_dotenv

class Item(BaseModel):
    service: str
    data: Union[dict, None] = None


app = FastAPI()

@app.get("/info")
def start():
    info = get_info()
    print(info)
    return info

today = datetime.now()
yesterday = today - timedelta(days=1)
today_str = today.strftime("%Y-%m-%d")
yesterday_str = yesterday.strftime("%Y-%m-%d")

@app.get("/info/weather")
def start(city='SaintPetersburg', date_from=yesterday_str, date_to=today_str):
    weather = get_weather(date_from, date_to, city=city)
    pprint(weather)
    return weather

def main():
    load_dotenv()
    port = int(os.getenv("PORT"))
    uvicorn.run("main:app", host='0.0.0.0', port=port)

if __name__ == "__main__":
    main()

