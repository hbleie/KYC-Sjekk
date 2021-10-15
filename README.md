# KYC-Sjekk

Stacc code challenge 2021

Oppgavebeskrivelse

Jeg har forsøkt meg på forslag a) lag en enkel webapp som lar brukeren utføre en KYC-sjekk av en person.

Jeg har brukt streamlit i Python for å utvikle appen. 

Prosjektet mitt er en enkel webapp med fire muligheter: Kjøre PEP-sjekk på enkeltpersoner, søke info om et selskap, søke etter hvem som innehar roller i et selskap og kjøre en PEP-sjekk på alle som har en rolle i selskapet. Disse fire ulike filtrene er sortert i et sidefelt med en dropdown-meny.

førstesiden er PEP-sjekk på enkeltpersoner. Ønsker man å endre side så, velger man i menyen på sidefeltet til venstre.

Første side: PEP-sjekk enkeltperson. Her kan man skrive inn et navn og få informasjon om denne personen er en PEP eller ikke. 

andre side: Selskap. Her kan man søke etter et selskap ved å bruke organisasjonsnummeret til selskapet, og i retur får man ut informasjon om dette selskapet.

tredje side: Roller i et selskap. Her kan man søke etter et selskap ved å bruke organisasjonsnummeret til selskapet, og i retur får man ut informasjon om hvem som innehar vesentlige roller i selskapet.

fjerde side: PEP-sjekk for alle i et selskap. Her kan man søke etter et selskap ved å bruke organisasjonsnummeret, og få informasjon om hvem som innehar vesentlige roller i selskapet og en PEP-sjekk av hver person.

Jeg tolket oppgaven dithen at en PEP-sjekk er en tilstrekkelig KYC-sjekk. Derfor inneholder ikke KYC-sjekken i programmet mer enn en PEP-sjekk.



Hvordan kjøre prosjektet
Prosjektet er publisert med streamlit og kan kjøres ved å klikke på lenken under.
lenke til webapp:
https://share.streamlit.io/hbleie/kyc-sjekk/main/KYC-sjekk.py


Kommentarer
Jeg valgte å bruke Python og streamlit fordi jeg nettopp hadde laget en litt liknende webapp i kodeoppgaven til fagkvelden med STACC. Derfor var jeg allerede godt kjent med funksjoner og løsninger streamlit inneholder. 

Eventuellt andre kommentarer / utfordringer?
Jeg brukte litt på å forstå dataene jeg fikk fra API'et, og hvordan jeg kunne jobbe med dem. 

I starten hadde jeg og litt problemer med Github siden jeg brukte spyder til å kode i. Jeg endte opp med å bruke visual studio code i stedet, som det var mye lettere å bruke sammen med Github. 

