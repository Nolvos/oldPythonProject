import requests

username = input("Enter your name")
url = "https://api.genderize.io?name="+username
call = requests.get(url)
data = call.json()
print(data["gender"])
