import streamlit as st
import requests



filter = st.sidebar.selectbox("Søk etter", ["PEP-sjekk enkeltperson", "Selskap", "Roller i et selskap", "PEP-sjekk for alle i et selskap"])
st.title(f"Know Your Customer - {filter}")

payload={}
headers = {}

def PepSøk(input):
    url = "https://stacc-code-challenge-2021.azurewebsites.net/api/pep?name=" + input
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    st.write('Number of hits: ' + str(r['numberOfHits']))
    st.subheader('Political Exposed Person = ' + str(r['numberOfHits'] > 0))
    for hit in r["hits"]:
        st.header(hit['name'])
        st.write('BIRTH DATE: ' + hit['birth_date'])
        st.write('FOUND IN DATASET: ' + hit['dataset'])
        st.write('ALIASES: ' + hit['aliases'])
        st.write('COUNTRY: ' + hit['countries'])

if filter == "PEP-sjekk enkeltperson": 
    input = st.text_input("Søk etter person")
    if input:
        PepSøk(input)
    


if filter == "Selskap": 
    input = st.text_input("Søk etter Selskap (Bruk Organisasjonsnummer)")
    if input:
        url = "https://stacc-code-challenge-2021.azurewebsites.net/api/enheter?orgNr=" + input
        response = requests.request("GET", url, headers=headers, data=payload)
        r = response.json()
        st.header(r['navn'])
        st.write('Organisasjonsform: ' + r['organisasjonsform']['beskrivelse'])
        st.write('Stiftelsesdato: ' + r["stiftelsesdato"])
        st.write('Beskrivelse: ' + r["naeringskode1"]['beskrivelse'])
        st.write('Antall ansatte: ' + str(r['antallAnsatte']))
        st.write('Forretningsadresse: ' + r['forretningsadresse']['adresse'][0] + ', ' + r['forretningsadresse']['postnummer'] + ', ' + r['forretningsadresse']['poststed'] + ', ' + r['forretningsadresse']['land'])


if filter == "Roller i et selskap":  
    input = st.text_input("Søk etter Selskap (Bruk Organisasjonsnummer)")
    if input:
        url = "https://stacc-code-challenge-2021.azurewebsites.net/api/roller?orgNr=" + input
        response = requests.request("GET", url, headers=headers, data=payload)
        r = response.json()
        for gruppe in r:
            st.title(gruppe['type']['beskrivelse'])
            st.write('Sist endret: ' + gruppe['sistEndret'])
            for rolle in gruppe['roller']:
                if 'person' in rolle:
                    st.subheader('Navn: ' + rolle['person']['navn']['fornavn'] + ' ' + rolle['person']['navn']['etternavn'])
                    st.write('Rolle: ' + rolle['type']['beskrivelse'])
                    st.write('Fødselsdato: ' + rolle['person']['fodselsdato'])
            st.markdown("____")


if filter == "PEP-sjekk for alle i et selskap":
    input = st.text_input("Søk etter selskap (bruk organisasjonsnummer)")
    if input:
        url = "https://stacc-code-challenge-2021.azurewebsites.net/api/roller?orgNr=" + input
        response = requests.request("GET", url, headers=headers, data=payload)
        r = response.json()
        for gruppe in r:
            st.title(gruppe['type']['beskrivelse'])
            st.write('Sist endret: ' + gruppe['sistEndret'])
            for rolle in gruppe['roller']:
                if 'person' in rolle:
                    st.subheader('Navn: ' + rolle['person']['navn']['fornavn'] + ' ' + rolle['person']['navn']['etternavn'])
                    st.write('Rolle: ' + rolle['type']['beskrivelse'])
                    st.write('Fødselsdato: ' + rolle['person']['fodselsdato'])
                    PepSøk(rolle['person']['navn']['fornavn'] + ' ' + rolle['person']['navn']['etternavn'])
                    st.markdown("____")
            



