from pprint import pprint
from datetime import datetime as dt

import requests

# 1. Basic theory
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # Ответ: <Response [200]> - объект Response
print(response.status_code)  # Ответ: 200
response.raise_for_status()  # метод для поднятия ошибки
#  Если поставить неверный урл, вызвав 404, то в консоли увидим:
#  requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/is-now.json

data = response.json()  # превращает респонс в словарь питона
print(data)
# Ответ: {'message': 'success', 'iss_position': {'latitude': '-30.8561', 'longitude': '177.3097'}, 'timestamp': 1762800344}

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
print(latitude)  # Ответ: -36.1299 - обращаемся как к словарю

iss_position = (longitude, latitude)
print(iss_position)  # Ответ: ('-167.3248', '-41.6195') - сделали кортеж

# 2. Запрос с параметрами
# 2.1
# sunrise_response = requests.get("https://api.sunrise-sunset.org/json")
# Не указывая обязательные параметры, которые требует АПИ дока, получаем ошибку 400
# sunrise_response.raise_for_status()

# 2.2
MY_LAT = -61.1383
MY_LNG = -26.5759
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG
}
sunrise_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sunrise_response.raise_for_status()
sunrise_data = sunrise_response.json()
pprint(sunrise_data)
# ОТвет: {'results': {'sunrise': '5:00:42 AM', 'sunset': '9:59:47 PM', 'solar_noon': '1:30:14 PM', 'day_length': '16:59:05', 'civil_twilight_begin': '4:00:40 AM', 'civil_twilight_end': '10:59:49 PM', 'nautical_twilight_begin': '12:00:01 AM', 'nautical_twilight_end': '12:00:01 AM', 'astronomical_twilight_begin': '12:00:01 AM', 'astronomical_twilight_end': '12:00:01 AM'}, 'status': 'OK', 'tzid': 'UTC'}

sunrise = sunrise_data["results"]["sunrise"]
print(sunrise)  # 5:00:42 AM
sunset = sunrise_data["results"]["sunset"]
print(sunset)  # 9:59:47 PM

# формат отличается от sunrise и sunset
# Че делать?

# В доке данного апи, есть опциональный параметр "formatted", установив который в 0 (дефолтно 1),
# мы выключим 24х часовое форматирование времени и будет отображаться unix время

parameters_unix_time = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

sunrise_response_unix = requests.get(
    "https://api.sunrise-sunset.org/json",
    params=parameters_unix_time,
)
sunrise_data_unix = sunrise_response_unix.json()
sunrise_unix = sunrise_data_unix["results"]["sunrise"]
print(sunrise_unix)  # 2025-11-10T05:00:42+00:00
sunset_unix = sunrise_data_unix["results"]["sunset"]
print(sunset_unix)  # 2025-11-10T21:59:47+00:00

sunrise_unix = int(sunrise_data_unix["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_unix = int(sunrise_data_unix["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise_unix)
print(sunset_unix)


time_now = dt.now()
print(time_now.hour)