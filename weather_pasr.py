import requests
import time
import os
from datetime import date,timedelta
from dotenv import load_dotenv


def get_weather(): # функция вывода информации о погоде

    load_dotenv()
    today = date.today()
    tomorrow = today + timedelta(days=1)

    #прописывем параметры обращения к api сервиса погоды
    endpoint =  "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    query_params = {"key": os.getenv("API_KEY"),
                    #"location": "59.9386300,30.3141300",
                    "location": "Saint-Petersburg RU",
                    "datestart": today,
                    "dateend": tomorrow,
                    "unitGroup" : "metric",
                    "include": "hours",
                    "elements": "datetime,hours,tempmax,tempmin,temp,humidity,pressure" }
    response = requests.get(endpoint, query_params)
    #парсим полученные данные
    days = response.json()["days"]
    stations = response.json()["address"]
    data_from = days[0]["datetime"]
    data_to = days[len(days)-1]["datetime"]

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
            "from": data_from,
            "to": data_to,
            "temperature": temp_out,
            "humidity": humidity_out,
            "pressure": pressure_out }
    json_data = {"service": "weather", "data": data}
    return json_data


def get_info(): # функция вывода общей информации о проекте
    json_data = {"version":"0.1", "service":"weather", "autor":"P.Zemlyanskiy"}
    return json_data




