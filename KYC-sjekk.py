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
        r = response.json()
        st.header('Number of hits: ' + str(r['numberOfHits']))
        for hit in r["hits"]:
            st.header(hit['name'])
            st.write('Birth Date: ' + hit['birth_date'])
            st.write('Found in dataset: \n' + hit['dataset'])
            st.write('Aliases: \n' + hit['aliases'])
            st.write('Country: \n' + hit['countries'])
        st.header('Political Exposed Person = ' + str(r['numberOfHits'] > 0))

            



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

