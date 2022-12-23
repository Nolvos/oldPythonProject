import requests

username = input("Enter your name")
url = "https://api.nationalize.io?name="+username
call = requests.get(url)
data = call.json()
for i in range(len(data["country"])):
    print(data["country"][i]["country_id"],end=" ")