import streamlit as st
import requests

st.title("Know Your Customer. PEP-sjekk")

filter = st.sidebar.selectbox("Søk etter", ["Personer", "Selskap", "Roller i et selskap"])

payload={}
headers = {}

if filter == "Personer":
    input = st.text_input("Søk etter person")


    if input:
        url = "https://stacc-code-challenge-2021.azurewebsites.net/api/pep?name=" + input

        response = requests.request("GET", url, headers=headers, data=payload)

        st.write(response.json())

if filter == "Selskap":
    input = st.text_input("Søk etter Selskap (Bruk Organisasjonsnummer)")


    if input:
        url = "https://stacc-code-challenge-2021.azurewebsites.net/api/enheter?orgNr=" + input

        response = requests.request("GET", url, headers=headers, data=payload)

        st.write(response.json())
        

if filter == "Roller i et selskap":
    input = st.text_input("Søk etter Selskap (Bruk Organisasjonsnummer)")

    if input:
        url = "https://stacc-code-challenge-2021.azurewebsites.net/api/roller?orgNr=" + input

        response = requests.request("GET", url, headers=headers, data=payload)

        st.write(response.json())

