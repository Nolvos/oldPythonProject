import requests

url = "https://catfact.ninja/fact"
call = requests.get(url)
print(call)
data = call.json()
print(data["fact"])