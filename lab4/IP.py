import requests

url = "https://api.ipify.org?format=json"
call = requests.get(url)
print(call)
data = call.json()
store = (data["ip"])

url2 = "https://ipinfo.io/"+store+"/geo"
call = requests.get(url2)
print(call)
data2 = call.json()
print(data2)