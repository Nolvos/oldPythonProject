import streamlit as st
import requests

st.write("welcome User!")
user = st.text_input("Enter the city")
st.write(user)

url = "https://api.openweathermap.org/data/2.5/weather?q="+user+"&appid=2c3fec021c22536656a477f652496c81"
save = requests.get(url)
data = save.json()
#st.write(data["weather"][0]["description"])
st.write(data)
temp = str(round(data["main"]["temp"]-273.15)) + "°C"
st.header(temp)
sky = data["weather"][0]["description"]
st.header(sky)

if  "clear" in sky:
    st.image("sky.jpg")
elif "few" in sky:
    st.image("cloud.jpg")