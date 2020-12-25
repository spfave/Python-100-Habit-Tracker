import os
from dotenv import load_dotenv
import requests
from requests.models import Response
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
hiking_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": "20201224",
    "quantity": "10.0",
}

response = requests.post(url=hiking_graph_endpoint, json=pixel_data, headers=headers)
print(response.text)