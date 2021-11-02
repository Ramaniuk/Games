import requests
import datetime

USERNAME = "olgar"
TOKEN = "sagyapowhgvcf8934573efh"
GRAPH_ID = "graph1"

date = datetime.datetime.today()
date_today = date.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Sport Graph",
    "unit": "min",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
pixel_params = {
    "date": date_today,
    "quantity": "20",
}

# response = requests.post(url=pixel_create_endpoint, json=pixel_params, headers=headers)
# print(response.text)

##PUT
date_update = datetime.datetime(year=2021,month=10,day=29)
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{date_update.strftime('%Y%m%d')}"
new_pixel_params = {
    "quantity": "15",
}

# response = requests.put(url=pixel_update_endpoint, json=new_pixel_params, headers=headers)
# print(response.text)

## DELETE
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{date_today}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)


# # https://pixe.la/v1/users/olgar/graphs/graph1.html
