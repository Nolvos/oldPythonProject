import requests
import streamlit as st
url = "https://game-prices.p.rapidapi.com/games"
game = st.text_input("Enter a Game")
country = st.text_input("Enter a region for your Game")
querystring = {"title":game,"region":country,"offset":"0","limit":"10"}




#["games"]["currency"]["currentLowestPrice"]
headers = {
	"X-RapidAPI-Key": "1385ec22c2msh815332cdc6be417p128e61jsnd93d11e4e2ce",
	"X-RapidAPI-Host": "game-prices.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
st.write(data)
st.write(data)