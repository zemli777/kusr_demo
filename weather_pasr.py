import requests
import time
import os
from datetime import date,timedelta
from dotenv import load_dotenv
import json

from dataclasses import dataclass



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

    def __post_init__(self):
        print(type(self.hours))
        count = 0
        for id in self.hours:
            count = count + 1
            json_obj = json.loads(json.dumps(id))
            print(type(id))
            hours_buf = Hours(**json_obj)
            self.hours[count] = hours_buf


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

  def __post_init__(self):

        print("@@@@@@@@@@@")
        print(type(self.days))
        print("@@@@@@@@@@@")
        print(type(self.days[0]))


        json_obj = json.loads(json.dumps(self.days[0]))
        print("#################")
        print(type(json_obj))
        for id in json_obj:
            day = Days(**json_obj)
            print(type(day))
            self.days.append(day)







# test = {"queryCost":48,"latitude":55.757,"longitude":37.615,"resolvedAddress":"Москва, Центральный федеральный округ, Россия","address":"Moscow","timezone":"Europe/Moscow","tzoffset":3.0,"days":[{"datetime":"2020-10-01","temp":12.7,"humidity":52.9,"pressure":1025.0,"hours":[{"datetime":"00:00:00","temp":11.8,"humidity":57.22,"pressure":1024.5},{"datetime":"01:00:00","temp":10.8,"humidity":59.39,"pressure":1024.5},{"datetime":"02:00:00","temp":10.2,"humidity":61.73,"pressure":1024.5},{"datetime":"03:00:00","temp":8.8,"humidity":67.91,"pressure":1024.5},{"datetime":"04:00:00","temp":9.6,"humidity":66.15,"pressure":1024.5},{"datetime":"05:00:00","temp":8.8,"humidity":69.9,"pressure":1024.5},{"datetime":"06:00:00","temp":8.2,"humidity":70.63,"pressure":1024.5},{"datetime":"07:00:00","temp":8.4,"humidity":69.49,"pressure":1025.0},{"datetime":"08:00:00","temp":9.7,"humidity":66.19,"pressure":1025.5},{"datetime":"09:00:00","temp":11.6,"humidity":60.35,"pressure":1025.5},{"datetime":"10:00:00","temp":13.7,"humidity":52.98,"pressure":1025.5},{"datetime":"11:00:00","temp":15.8,"humidity":44.48,"pressure":1025.5},{"datetime":"12:00:00","temp":16.8,"humidity":37.16,"pressure":1025.0},{"datetime":"13:00:00","temp":17.0,"humidity":36.97,"pressure":1025.0},{"datetime":"14:00:00","temp":17.4,"humidity":32.52,"pressure":1025.0},{"datetime":"15:00:00","temp":17.6,"humidity":33.18,"pressure":1025.0},{"datetime":"16:00:00","temp":18.0,"humidity":31.33,"pressure":1024.5},{"datetime":"17:00:00","temp":16.7,"humidity":37.49,"pressure":1024.5},{"datetime":"18:00:00","temp":14.3,"humidity":43.75,"pressure":1025.0},{"datetime":"19:00:00","temp":12.8,"humidity":50.29,"pressure":1025.0},{"datetime":"20:00:00","temp":13.2,"humidity":50.71,"pressure":1025.5},{"datetime":"21:00:00","temp":12.4,"humidity":53.26,"pressure":1025.5},{"datetime":"22:00:00","temp":11.2,"humidity":57.8,"pressure":1026.0},{"datetime":"23:00:00","temp":10.9,"humidity":58.72,"pressure":1026.5}]},{"datetime":"2020-10-02","temp":12.5,"humidity":57.8,"pressure":1027.2,"hours":[{"datetime":"00:00:00","temp":10.3,"humidity":61.04,"pressure":1026.5},{"datetime":"01:00:00","temp":10.3,"humidity":60.35,"pressure":1026.5},{"datetime":"02:00:00","temp":9.2,"humidity":65.23,"pressure":1026.5},{"datetime":"03:00:00","temp":8.4,"humidity":67.45,"pressure":1026.5},{"datetime":"04:00:00","temp":8.2,"humidity":67.42,"pressure":1026.5},{"datetime":"05:00:00","temp":7.4,"humidity":71.34,"pressure":1026.5},{"datetime":"06:00:00","temp":6.8,"humidity":72.09,"pressure":1026.5},{"datetime":"07:00:00","temp":7.4,"humidity":71.34,"pressure":1026.5},{"datetime":"08:00:00","temp":9.0,"humidity":66.82,"pressure":1027.5},{"datetime":"09:00:00","temp":11.2,"humidity":59.12,"pressure":1028.3},{"datetime":"10:00:00","temp":12.8,"humidity":52.47,"pressure":1027.5},{"datetime":"11:00:00","temp":14.8,"humidity":52.38,"pressure":1027.5},{"datetime":"12:00:00","temp":16.0,"humidity":49.17,"pressure":1027.5},{"datetime":"13:00:00","temp":17.2,"humidity":45.68,"pressure":1027.5},{"datetime":"14:00:00","temp":18.0,"humidity":44.08,"pressure":1027.5},{"datetime":"15:00:00","temp":18.6,"humidity":40.6,"pressure":1027.0},{"datetime":"16:00:00","temp":18.6,"humidity":41.31,"pressure":1027.0},{"datetime":"17:00:00","temp":17.6,"humidity":43.96,"pressure":1027.0},{"datetime":"18:00:00","temp":15.4,"humidity":50.5,"pressure":1027.0},{"datetime":"19:00:00","temp":13.6,"humidity":57.44,"pressure":1027.5},{"datetime":"20:00:00","temp":12.8,"humidity":59.88,"pressure":1027.5},{"datetime":"21:00:00","temp":12.6,"humidity":60.55,"pressure":1028.0},{"datetime":"22:00:00","temp":12.2,"humidity":62.2,"pressure":1028.0},{"datetime":"23:00:00","temp":11.8,"humidity":63.95,"pressure":1028.5}]}]}
test = {"queryCost":48,"latitude":55.757,"longitude":37.615,"resolvedAddress":"Москва, Центральный федеральный округ, Россия","address":"Moscow","timezone":"Europe/Moscow","tzoffset":3.0,"days":[{"datetime":"2020-10-01","tempmax":18.0,"tempmin":8.2,"temp":12.7,"humidity":52.9,"pressure":1025.0,"hours":[{"datetime":"00:00:00","temp":11.8,"humidity":57.22,"pressure":1024.5},{"datetime":"01:00:00","temp":10.8,"humidity":59.39,"pressure":1024.5},{"datetime":"02:00:00","temp":10.2,"humidity":61.73,"pressure":1024.5},{"datetime":"03:00:00","temp":8.8,"humidity":67.91,"pressure":1024.5},{"datetime":"04:00:00","temp":9.6,"humidity":66.15,"pressure":1024.5},{"datetime":"05:00:00","temp":8.8,"humidity":69.9,"pressure":1024.5},{"datetime":"06:00:00","temp":8.2,"humidity":70.63,"pressure":1024.5},{"datetime":"07:00:00","temp":8.4,"humidity":69.49,"pressure":1025.0},{"datetime":"08:00:00","temp":9.7,"humidity":66.19,"pressure":1025.5},{"datetime":"09:00:00","temp":11.6,"humidity":60.35,"pressure":1025.5},{"datetime":"10:00:00","temp":13.7,"humidity":52.98,"pressure":1025.5},{"datetime":"11:00:00","temp":15.8,"humidity":44.48,"pressure":1025.5},{"datetime":"12:00:00","temp":16.8,"humidity":37.16,"pressure":1025.0},{"datetime":"13:00:00","temp":17.0,"humidity":36.97,"pressure":1025.0},{"datetime":"14:00:00","temp":17.4,"humidity":32.52,"pressure":1025.0},{"datetime":"15:00:00","temp":17.6,"humidity":33.18,"pressure":1025.0},{"datetime":"16:00:00","temp":18.0,"humidity":31.33,"pressure":1024.5},{"datetime":"17:00:00","temp":16.7,"humidity":37.49,"pressure":1024.5},{"datetime":"18:00:00","temp":14.3,"humidity":43.75,"pressure":1025.0},{"datetime":"19:00:00","temp":12.8,"humidity":50.29,"pressure":1025.0},{"datetime":"20:00:00","temp":13.2,"humidity":50.71,"pressure":1025.5},{"datetime":"21:00:00","temp":12.4,"humidity":53.26,"pressure":1025.5},{"datetime":"22:00:00","temp":11.2,"humidity":57.8,"pressure":1026.0},{"datetime":"23:00:00","temp":10.9,"humidity":58.72,"pressure":1026.5}]},{"datetime":"2020-10-02","tempmax":18.6,"tempmin":6.8,"temp":12.5,"humidity":57.8,"pressure":1027.2,"hours":[{"datetime":"00:00:00","temp":10.3,"humidity":61.04,"pressure":1026.5},{"datetime":"01:00:00","temp":10.3,"humidity":60.35,"pressure":1026.5},{"datetime":"02:00:00","temp":9.2,"humidity":65.23,"pressure":1026.5},{"datetime":"03:00:00","temp":8.4,"humidity":67.45,"pressure":1026.5},{"datetime":"04:00:00","temp":8.2,"humidity":67.42,"pressure":1026.5},{"datetime":"05:00:00","temp":7.4,"humidity":71.34,"pressure":1026.5},{"datetime":"06:00:00","temp":6.8,"humidity":72.09,"pressure":1026.5},{"datetime":"07:00:00","temp":7.4,"humidity":71.34,"pressure":1026.5},{"datetime":"08:00:00","temp":9.0,"humidity":66.82,"pressure":1027.5},{"datetime":"09:00:00","temp":11.2,"humidity":59.12,"pressure":1028.3},{"datetime":"10:00:00","temp":12.8,"humidity":52.47,"pressure":1027.5},{"datetime":"11:00:00","temp":14.8,"humidity":52.38,"pressure":1027.5},{"datetime":"12:00:00","temp":16.0,"humidity":49.17,"pressure":1027.5},{"datetime":"13:00:00","temp":17.2,"humidity":45.68,"pressure":1027.5},{"datetime":"14:00:00","temp":18.0,"humidity":44.08,"pressure":1027.5},{"datetime":"15:00:00","temp":18.6,"humidity":40.6,"pressure":1027.0},{"datetime":"16:00:00","temp":18.6,"humidity":41.31,"pressure":1027.0},{"datetime":"17:00:00","temp":17.6,"humidity":43.96,"pressure":1027.0},{"datetime":"18:00:00","temp":15.4,"humidity":50.5,"pressure":1027.0},{"datetime":"19:00:00","temp":13.6,"humidity":57.44,"pressure":1027.5},{"datetime":"20:00:00","temp":12.8,"humidity":59.88,"pressure":1027.5},{"datetime":"21:00:00","temp":12.6,"humidity":60.55,"pressure":1028.0},{"datetime":"22:00:00","temp":12.2,"humidity":62.2,"pressure":1028.0},{"datetime":"23:00:00","temp":11.8,"humidity":63.95,"pressure":1028.5}]}]}
#https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Moscow/2020-10-01/2020-10-02/?unitGroup=metric&key=FWH5GGAWQY9UQ8ENCBEHQMYUZ&include=hours&elements=datetime,hours,tempmax,tempmin,temp,humidity,pressure

def go_to_weather_service(location='Saint-Petersburg RU',datestart='2024-03-28',dateend='2024-03-28',include='hours',elements='datetime,hours,tempmax,tempmin,temp,humidity,pressure'):

    # endpoint =  "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    # query_params = {"key": os.getenv("API_KEY"),
    #                 "location": location,
    #                 "datestart": datestart,
    #                 "dateend": dateend,
    #                 "unitGroup" : "metric",
    #                 "include": include,
    #                 "elements": elements }
    # response = requests.get(endpoint, query_params).json()
    # print(response)
    # json_obj =json.loads(response)
    json_obj = json.loads(json.dumps(test))
    weather = Weather_api(**json_obj)
    return weather


def get_weather(location='Saint-Petersburg RU',datestart='2024-03-28',dateend='2024-03-28'): # функция вывода информации о погоде

    load_dotenv()
    response = go_to_weather_service(location,datestart,dateend)
    #парсим полученные данные
    days = response["days"]

    stations = response.address

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


weather = go_to_weather_service()
print (weather.days[1])



def get_info(): # функция вывода общей информации о проекте
    json_data = {"version":os.getenv("VERSION"), "service":"weather", "autor":"P.Zemlyanskiy"}
    return json_data


