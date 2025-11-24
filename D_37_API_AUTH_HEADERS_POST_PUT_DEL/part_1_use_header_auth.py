import requests

USERNAME = "ihar"
TOKEN = "asdf34r3e33efdase42342sadf"

URL_PIXELA = "https://pixe.la/v1/users"
params = {
    "token": "asdf34r3e33efdase42342sadf",
    "username": "ihar",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# r = requests.post(
#     url=URL_PIXELA,
#     json=params)  # json это бади post-запроса, params - параметры запроса
# print(r.text)

GRAPH_ENDPOINT = f"{URL_PIXELA}/{USERNAME}/graphs"


graph_config = {
    "id": "graph1",
    "name": "Skiing graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# 1. Будет ошибка, т к авторизация должна передаваться через хедер X-USER-TOKEN
# response = requests.post(
#     url=GRAPH_ENDPOINT,
#     json=graph_config
# )
# print(response.text)  # {"message":"User `ihar` does not exist or the token is wrong.","isSuccess":false}

# 2. Прокидываем хедер
response = requests.post(
    url=GRAPH_ENDPOINT,
    json=graph_config,
    headers=headers
)
print(response.text)
