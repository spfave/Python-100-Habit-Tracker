import os
from dotenv import load_dotenv
import requests
load_dotenv()


# Constants
token = os.getenv("TOKEN")
username = os.getenv("USERNAME")


# Endpoint
pixela_endpoint = "https://pixe.la/v1/users"


# Create user
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Create new Pixela graph
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Hiking Graph",
    "unit": "Miles",
    "type": "float",
    "color": "momiji",
}

headers={
    "X-USER-TOKEN": token,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)