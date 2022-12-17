# Y-Finance noch benötigt?
import yfinance as yf


#LOAD PACKAGES
import requests
import time
import streamlit as st

#web scraping 
headers = {
    'authority': 'api.zendepot.de',
    'accept': 'application/json, text/plain, /',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
    'origin': 'https://zendepot.de',
    'referer': 'https://zendepot.de/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

# Logo einfügen
from PIL import Image
image = Image.open('Diversify_Logo.png')

st.image(image)


# Überschrift
st.write("""
#  **How diversified is your ETF portfolio?**
### Now choose which ETFs you have in your portfolio!
""")

# ETF 1 auswählen
isin1 = st.text_input('Type in the ETF ISIN (for example "IE00B4L5Y983" for the iShares Core MSCI World UCITS ETF)', 'IE00B4L5Y983')
amount1 = st.text_input('Type in the amount of money (in $), you are invested in this specific ETF', '7.000')

# ETF 2 auswählen
isin2 = st.text_input('Type in the ETF ISIN (for example "IE00B0M63177" for the iShares MSCI EM UCITS ETF USD)', 'IE00B0M63177')
amount2 = st.text_input('Type in the amount of money (in $), you are invested in this specific ETF', '3.000')


#ISIN 1 eingeben und die Daten dazu bekommen 
response = requests.get('https://api.zendepot.de/finance/etf/'+str(isin1), headers=headers)
data = {"Countries": "", "Holdings": "", "Sectors": ""}
responseData = response.json()
for scrapedData in responseData:
    data["Countries"] = response.json()["exposure"]["countries"]
    data["Holdings"] = response.json()["exposure"]["holdings"]
    data["Sectors"] = response.json()["exposure"]["sectors"]

st.table(data["Countries"])


#ISIN 2 eingeben und die Daten dazu bekommen 
response = requests.get('https://api.zendepot.de/finance/etf/'+str(isin2), headers=headers)
data = {"Countries": "", "Holdings": "", "Sectors": ""}
responseData = response.json()
for scrapedData in responseData:
    data["Countries"] = response.json()["exposure"]["countries"]
    data["Holdings"] = response.json()["exposure"]["holdings"]
    data["Sectors"] = response.json()["exposure"]["sectors"]

st.table(data["Countries"])


# ETFs miteinander verrechnen

# Länderverteilung in ETFs
#amount1/(amount1+amount2)*data["Countries"]
    
# Länderverteilung in ETF 2
#for info in data2["Countries"]:
 #   print(info["name"], y/(x+y)*info["percentage"]*100) 