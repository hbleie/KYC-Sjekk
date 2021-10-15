import streamlit as st
import requests

st.title("Know Your Customer. PEP-sjekk")

input = st.text_input("Søk etter person")

if input:
    url = "https://stacc-code-challenge-2021.azurewebsites.net/api/pep?name=" + input

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    st.write(response.json())



