import requests
import time

def get_weather(): # функция вывода информации о погоде 
    
    #прописывем параметры обращения к api сервиса погоды 
    endpoint =  "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    api_key =  "3Q6F87RZLUU6DDZFCQFMLKHGX"
    query_params = {"key": api_key,
                    #"location": "59.9386300,30.3141300",
                    "location": "Saint-Petersburg RU",
                    "datestart": "2024-03-27",
                    "dateend": "2024-03-28",
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
    
    for date in days:
        hours = date["hours"]

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


    
        
