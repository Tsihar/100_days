import requests
from datetime import datetime as dt

USERNAME = "ihar"
TOKEN = "asdf34r3e33efdase42342sadf"
GRAPH_ID = "graph1"
UI_URL = "https://pixe.la/v1/users/ihar/graphs/graph1.html"

URL_PIXELA = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{URL_PIXELA}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{URL_PIXELA}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.now()
day_datetime = f"{today.year}{today.month}{today.day}"
print(today)
print(day_datetime)

# Указываем формат strftime, чтоб сконвертить дату в строку
day_strftime = today.strftime("%Y%m%d")
print(day_strftime)

body = {
    "date": day_strftime,
    "quantity": "2"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# 2. Прокидываем хедер
response = requests.post(
    url=POST_PIXEL_ENDPOINT,
    json=body,
    headers=headers
)
print(response.status_code)
print(response.json())
print(response.text)
