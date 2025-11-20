from twilio.rest import Client

import requests

API_KEY = ""
LAT = 53.9
LON = 27.5667
params = {
    "lon": LON,
    "lat": LAT,
    "cnt": 4,
    "appid": "f3116c3af4d"
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
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body="Take an umbrella for tomorrow",
    #     from_="",
    #     to="",
    # )

    print(message.status)

    # Что такое переменные окружения (env variables)
# 1. Мы их используем, чтобы скрыть чувствительные данные, если ранаем код удаленно
# 2. И если большой проект их удобно хранить в одном месте (креды, токены, и т п)

# 3. Раная удаленно (python anywhere) в баш скрипте выполняем команду 'env' (локально в терминале 'dir Env:')
# можно увидеть все установленные на машине переменные окружения
# 4. Чтобы добавить новую переменную в баш скрипте прописываем команду 'export AUTH_TOKEN=a3f450ef24cb44d71bbcb068bc0e3d'
# 5. Чтобы пользоваться переменной в коде мы уже прописываем не 'auth_token = "a3f450ef24cb44d71bbbb068bc0e3d"',
# а auth_token = os.environ.get("AUTH_TOKEN")
# 6. Получается, чтобы автоматически сетапить переменные окружения, мы должны подготовить скрипты, которые их засетапят (из п.4)
# в python anywhere в скедулере прокидываем команду:
# 'export AUTH_TOKEN=a3f450ef24cb44d71bbcbbb068bc0e3d; export NUMBER=+375293043'
# т о перед стартом скрипта сначала установятся переменные, а потом код будет их использовать через os.environ.get("BLABLA")
# я не смог в этом попрактиковаться, потому что на мой телефон не отправляется смс-ка о погоде почему-то