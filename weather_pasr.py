import requests
import time
import os
from datetime import date,timedelta
from dotenv import load_dotenv


def go_to_weather_service(location='Saint-Petersburg RU',datestart='2024-03-28',dateend='2024-03-28',include='hours',elements='datetime,hours,tempmax,tempmin,temp,humidity,pressure'):

    endpoint =  "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    query_params = {"key": os.getenv("API_KEY"),
                    "location": location,
                    "datestart": datestart,
                    "dateend": dateend,
                    "unitGroup" : "metric",
                    "include": include,
                    "elements": elements }
    response = requests.get(endpoint, query_params)
    return response.json()


def get_weather(location='Saint-Petersburg RU',datestart='2024-03-28',dateend='2024-03-28'): # функция вывода информации о погоде

    load_dotenv()
    response = go_to_weather_service(location,datestart,dateend)
    #парсим полученные данные
    days = response["days"]
    stations = response["address"]
    date_from = days[0]["datetime"]
    date_to = days[len(days)-1]["datetime"]

    temp = []
    humidity = []
    pressure = []

    for dates in days:
        hours = dates["hours"]

        for hour in hours:
            temp.append(hour["temp"])
            humidity.append(hour["humidity"])
            pressure.append(hour["pressure"])

    temp_out = {"max": max(temp), "min": min(temp), "average": (max(temp)+min(temp))/2, "median": temp[int(len(temp)/2)]}
    humidity_out = {"max": max(humidity), "min": min(humidity), "average": (max(humidity)+min(humidity))/2, "median": humidity[int(len(humidity)/2)]}
    pressure_out = {"max": max(pressure), "min": min(pressure), "average": (max(pressure)+min(pressure))/2, "median": pressure[int(len(pressure)/2)]}

    # подготавливаем данные к отправке в виде JSON
    data = {"city": stations,
            "from": date_from,
            "to": date_to,
            "temperature": temp_out,
            "humidity": humidity_out,
            "pressure": pressure_out }
    json_data = {"service": "weather", "data": data}
    return json_data


def get_info(): # функция вывода общей информации о проекте
    json_data = {"version":os.getenv("VERSION"), "service":"weather", "autor":"P.Zemlyanskiy"}
    return json_data


