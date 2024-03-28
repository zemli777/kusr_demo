from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse,FileResponse

from weather_pasr import get_weather,get_info

class Item(BaseModel):
    service: str
    data: Union[dict, None] = None


app = FastAPI()

@app.get("/info")
def start():
    info = get_info()
    print(info)
    return info


@app.get("/info/weather")
def start(location='Saint-Petersburg RU',datestart='2024-03-28',dateend='2024-03-28'):
    weather = get_weather(location, datestart, dateend)
    print(weather)
    return weather

