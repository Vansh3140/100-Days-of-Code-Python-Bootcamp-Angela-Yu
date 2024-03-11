import requests
import datetime as dt

USERNAME = "vanshsingh"
TOKEN = ""
GRAPH_ID = "graph1"
#POST

# pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

# params = {
#     "date": date.strftime("%Y%m%d"),
#     "quantity": "6"
# }

# response = requests.post(url=pixela_endpoint, json=params, headers=headers)

#PUT

# pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20240311"

# params = {
#     "quantity": "15"
# }

#DELETE

pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20240311"
date = dt.datetime.now()




headers = {
    "X-USER-TOKEN": TOKEN
}



response = requests.delete(url=pixela_endpoint, headers=headers)
print(response.text)
