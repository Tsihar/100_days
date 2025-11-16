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
for data in weather_data:
    if data["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    print("Take an umbrella")
pprint(data)