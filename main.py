import requests
import datetime

TOKEN = "dfgvglehflerhfliewru"
USERNAME = "sinaeshrati"
headers = {
    "X-USER-TOKEN": TOKEN
}

# ------------------------------------- Creating Username ---------------------------------------
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post("https://pixe.la/v1/users", json=user_params)
# print(response.text)

# ------------------------------------- Creating Graph -----------------------------------------
graph_config = {
    "id": "graph-1",
    "name": "Coding graph",
    "unit": "hour",
    "type": "float",
    "color": "momiji"
}

# response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_config, headers=headers)
# print(response.text)

# -------------------------------------- Posting Pixels -----------------------------------------
today = datetime.datetime.now()
value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}

response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/graph-1", json=value_config, headers=headers)
print(response.text)

# -------------------------------------- Updating Pixels -----------------------------------------
edit_config = {
    "quantity": "4"
}
# response = requests.put(f"https://pixe.la/v1/users/{USERNAME}/graphs/graph-1/20210503", json=edit_config,
# headers=headers)
# print(response.text)

# ------------------------------------- Deleting Pixels ------------------------------------------
# response = requests.delete(f"https://pixe.la/v1/users/{USERNAME}/graphs/graph-1/20210503", headers=headers)
# print(response.text)
