import smtplib

from pprint import pprint

import requests

API_KEY = "f3116079c010a0477e5e00ff78c3af4d"
LAT = 53.9
LON = 27.5667
params = {
    "lon": LON,
    "lat": LAT,
    "cnt": 4,
    "appid": "f3116079c010a0477e5e00ff78c3af4d"
}


response = requests.get(url=f'https://api.openweathermap.org/data/2.5/forecast',
                        params=params)
response.raise_for_status()
weather_data = response.json()["list"]

will_rain = False
message = ""
for data in weather_data:
    if data["weather"][0]["id"] < 700:
        will_rain = True
        message += f'Date: {data["dt_txt"]} Min: {data["main"]["temp_min"] - 273.15} Max: {data["main"]["temp_max"] - 273.15} Osadki:{data["weather"][0]["main"]}\n'

if will_rain:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="appbrewery87@gmail.com", password="rtqw vcqi bxbn ebvr")
        connection.sendmail(from_addr="appbrewery87@gmail.com",
                            to_addrs="app_brewery@yahoo.com",
                            msg=f'Subject:Take an umbrella\nBeri zont')
