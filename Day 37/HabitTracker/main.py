import requests
import datetime

USERNAME = # YOUR USERNAME
TOKEN = # YOUR TOKEN
GRAPH_ID = # YOUR GRAPH ID
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# creating a user
# res = requests.post(url=pixela_endpoint, json=user_params)
# print(res.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "My reading Graph",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# creating a graph
# res_graph = requests.post(url=graph_endpoint, json=graph_params,headers=headers )
# print(res_graph.text)

now = datetime.datetime.now()
today_date = now.date().strftime("%Y%m%d")

commit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
commit_params = {
    "date": today_date,
    "quantity": input("How many pages did you read today?"),
}
# creating a pixel
res_pixel=requests.post(url=commit_endpoint,headers=headers, json=commit_params)
print(res_pixel.text)

# update a pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
update_params = {
    "quantity": "2"
}
# res_update=requests.put(url=update_endpoint,headers=headers, json=update_params)
# print(res_update.text)

del_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
# delete a pixel
# res_delete=requests.delete(url=del_endpoint, headers=headers)
# print(res_delete.text)