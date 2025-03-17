from datetime import *

import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "somenameorotheryes"
TOKEN = "lasfdhdlaiewhi3230"
GRAPH_ID = "graph1"
colors = {
    "green":"shibafu",
    "red":"momiji",
    "sora":"blue",
    "yellow":"ichou",
    "purple":"ajisai",
    "black":"kuro"
}

# graph_config = {
#     "id":GRAPH_ID
#     "name":"Med Graph",
#     "unit":"Hours",
#     "type":"int",
#     "color":colors["red"]
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# user_params = {
#     "token":TOKEN,
#     "username":USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

#yesterday = datetime(year=2025, month=3, day=16)

today = datetime.now()
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"1",
}

# Posting a data point
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "2"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# requests.delete(url=delete_endpoint, headers=headers)

