import requests
from datetime import datetime as dt, timedelta

USERNAME = "ihar"
TOKEN = "asdf34r3e33efdase42342sadf"
GRAPH_ID = "graph1"
UI_URL = "https://pixe.la/v1/users/ihar/graphs/graph1.html"

URL_PIXELA = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{URL_PIXELA}/{USERNAME}/graphs"
today = dt.now()
day_datetime = f"{today.year}{today.month}{today.day}"
yesterday = today - timedelta(days=1)
yesterday_strftime = yesterday.strftime("%Y%m%d")

PUT_DELETE_PIXEL_ENDPOINT = f"{URL_PIXELA}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_strftime}"
print(today)
print(day_datetime)

# Указываем формат strftime, чтоб сконвертить дату в строку
day_strftime = today.strftime("%Y%m%d")
print(day_strftime)

body = {
    "quantity": "3"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# 1. обновить граф пиксель
response_put = requests.put(
    url=PUT_DELETE_PIXEL_ENDPOINT,
    json=body,
    headers=headers
)
print(response_put.status_code)
print(response_put.json())
print(response_put.text)

# 2. удалить граф пиксель
response_del = requests.delete(
    url=PUT_DELETE_PIXEL_ENDPOINT,
    headers=headers
)
print(response_del.status_code)
print(response_del.json())
print(response_del.text)
