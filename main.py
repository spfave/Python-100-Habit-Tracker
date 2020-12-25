import os
from dotenv import load_dotenv
import requests
import datetime
load_dotenv()


# Constants
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = "graph1"


# Endpoint
pixela_endpoint = "https://pixe.la/v1/users"


# Create user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Create new Pixela graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Hiking Graph",
    "unit": "Miles",
    "type": "float",
    "color": "momiji",
}
headers={
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Post pixel to graph
# today = datetime.date.today()
today = datetime.date(year=2020, month=12, day=5)
pixel_post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7.56",
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# Update pixel
date = datetime.date(year=2020, month=12, day=5)
date_format = date.strftime("%Y%m%d")

pixel_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date_format}"
pixel_update_data = {
    "quantity": "6.57",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)


# Delete a pixel
pixel_delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date_format}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
