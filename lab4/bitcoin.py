import requests

country = input("Enter a country you want to check")
url = "http://universities.hipolabs.com/search?country="+country
call = requests.get(url)
data = call.json()
for i in range(len(data)):
    print(data[i]["name"])
    print(data[i]["web_pages"])
    print()
