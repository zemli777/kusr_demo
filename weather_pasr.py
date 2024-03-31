import requests
import time
import os
from datetime import date,timedelta
from dotenv import load_dotenv
import json

from dataclasses import dataclass,field
from dataclasses_json import dataclass_json


@dataclass
class Hours:
    datetime: str
    temp: float
    humidity: float
    pressure: float

@dataclass
class Days:
    datetime: str
    tempmax: float
    tempmin: float
    temp: float
    humidity: float
    pressure: float
    hours: dict
    hours_class: dict = field(default_factory=dict)

    def __post_init__(self):
        for i in range(0, len(self.hours)):
            json_obj = json.loads(json.dumps(self.hours[i]))
            hour = Hours(**json_obj)
            self.hours_class[i] = hour

@dataclass
class Weather_api:
  queryCost: int
  latitude: float
  longitude: float
  resolvedAddress: str
  address: str
  timezone: str
  tzoffset: float
  days: dict
  days_class: dict = field(default_factory=dict)

  def __post_init__(self):
    for i in range(0, len(self.days)):
        json_obj = json.loads(json.dumps(self.days[i]))
        day = Days(**json_obj)
        self.days_class[i] = day



@dataclass
class Data:
    city: str
    date_from: str
    date_to: str
    temperature_c: dict
    humidity: dict
    pressure_mb: dict
  

@dataclass_json
@dataclass
class Service:
    service: str 
    data: Data
    # data_class: dict = field(default_factory=dict)
    

    # def __post_init__(self):
    #     json_obj = json.loads(json.dumps(self.data))
    #     # data_buf = Data(**json_obj)
    #     print("####")
    #     # self.data_class = data_buf
    #     print("##")
    #     print(type(self.data_class))   




def go_to_weather_service(city: str, date_from: str, date_to: str, include='hours', elements='datetime,hours,tempmax,tempmin,temp,humidity,pressure'):

    endpoint =  "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    query_params = {"key": os.getenv("API_KEY"),
                    "location": city,
                    "datestart": date_from,
                    "dateend": date_to,
                    "unitGroup" : "metric",
                    "include": include,
                    "elements": elements }
    response = requests.get(endpoint, query_params).json()
    print(response)
    # json_obj =json.loads(response)
    # json_obj = json.loads(json.dumps(test))
    # weather = Weather_api(**json_obj)
    weather = Weather_api(**response)
    return weather


def get_weather(date_from, date_to, city):
    """Функция вывода информации о погоде
    """

    # load_dotenv()
    response = go_to_weather_service(city, date_from, date_to)
    #парсим полученные данные
    
    # stations  = response.address
    date_from = response.days_class[0].datetime
    date_to = response.days_class[len(response.days_class)-1].datetime

    temp = []
    humidity = []
    pressure = []

    for date in response.days_class:
        for hour in response.days_class[date].hours_class:
            temp.append(response.days_class[date].hours_class[hour].temp)
            humidity.append(response.days_class[date].hours_class[hour].humidity)
            pressure.append(response.days_class[date].hours_class[hour].pressure)

    temp_out = {"max": max(temp), "min": min(temp), "average": (max(temp)+min(temp))/2, "median": temp[int(len(temp)/2)]}
    humidity_out = {"max": max(humidity), "min": min(humidity), "average": (max(humidity)+min(humidity))/2, "median": humidity[int(len(humidity)/2)]}
    pressure_out = {"max": max(pressure), "min": min(pressure), "average": (max(pressure)+min(pressure))/2, "median": pressure[int(len(pressure)/2)]}

    
    weather = {"city": city, "date_from": date_from, "date_to": date_to,"temperature_c": temp_out,"humidity": humidity_out,"pressure_mb": pressure_out}
    service_json = {"service": "weather", "data": weather}
    # json_obj = json.loads(json.dumps(service_json))
    # service = Service(**json_obj)
    # output = service.to_json()  
    return service_json


def get_info(): # функция вывода общей информации о проекте
    json_data = {"version":os.getenv("VERSION", default="0.1.0"), "service": "weather", "author": "P.Zemlyanskiy"}
    return json_data


