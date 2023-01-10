# Streamlit Diversify Webapp

#LOAD PACKAGES
import requests
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


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

# Outputformat bestimmen in Listen

# ETF 1
ETF_countries_1 = {}
ETF_sectors_1 = {}
ETF_holdings_1 = {}

# ETF 2
ETF_countries_2 = {}
ETF_sectors_2 = {}
ETF_holdings_2 = {}

#---------------------------------------------Hintergrund einfügen--------------------------------------------------------------------#
import base64

df = px.data.iris()

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("1214404.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images3.alphacoders.com/104/1044851.jpg");
background-size: 2000%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
#-----------------------------------------------------------------------------------------------------------------#

# Logo einfügen
from PIL import Image
image = Image.open('Diversify_logo1.png')

st.image(image)


# Überschrift
st.write("""
#  **How diversified is your ETF portfolio?**
### Now choose which ETFs you have in your portfolio!
""")

#------------------------------------Etfs in einer select Box auswählen ---------------------------------------------#

# Create dictionary
etfs = {
'The most popular ETFs': 'LU1737652237',    
'MSCI World': 'LU1737652237',
'MSCI All Country World': 'IE00B6R52259',
'MSCI Emerging Markets': 'LU1737652583',
'EURO STOXX 50': 'IE0008471009',
'STOXX Europe 600': 'LU0328475792',
'MSCI Europe': 'LU1242369327',
'DAX': 'LU2090062436',
'MDAX': 'LU1033693638',
'SDAX': 'LU0603942888',
'TecDAX': 'DE000ETF9082',
'S&P 500': 'IE000Z9SJA06',
'Nasdaq 100': 'IE00BMFKG444',
'Russell 2000': 'IE00BJZ2DD79',
'MSCI USA': 'IE00BG04M077',
'Nikkei 225': 'LU0839027447',
'MSCI Emerging Markets Asia': 'IE00B5L8K969',
'MSCI China': 'LU0514695690'

 }

#------------------------------------ Select the 2 ETFs from the select box -----------------------------------------#
#Absatz einfügen
st.markdown('')

# Create select box for the first ETF
selected_etf = st.selectbox('Select your first ETF:', list(etfs.keys()))

use_isin = st.checkbox('Tick the box if you have not found an ETF in the list and simply enter the ISIN yourself 😃')

if use_isin:
    isin1 = st.text_input('Enter your first ISIN:')
    

else:
  isin1 = etfs[selected_etf]

# Display ISIN for selected ETF
st.write(f'ISIN for your first ETF {selected_etf}: {etfs[selected_etf]}')


amount1 = st.text_input('Type in the amount of money (in $), you are invested in this specific ETF', '7.000')

#-------------------second ETF----------------------------#
#Absatz einfügen
st.markdown('')
st.markdown('')
# Create select box for the second ETF

selected_etf2 = st.selectbox('Select your second ETF:', list(etfs.keys()))

use_isin2 = st.checkbox('Tick the box if you have not found the second ETF in the list and simply enter the ISIN yourself 🤪')

if use_isin2:
    isin2 = st.text_input('Enter your second ISIN:')
    

else:
  isin2 = etfs[selected_etf2]

# Display ISIN for selected ETF
st.write(f'ISIN for your second ETF {selected_etf2}: {etfs[selected_etf2]}')

# isin2 = etfs[selected_etf2]

amount2 = st.text_input('Type in the amount of money (in $), you are invested in this specific ETF', '3.000')

#------------------------------------Geldbetrag mit einem Slider auswählen-------------------------------------------#

# Create money slider
#slider = st.slider('Select the amount of money (in $), you are invested in this specific ETF:', 0, 1000000, 20000)

# Display slider
#st.write(slider)

#--------------------------------------------------------------------------------------------------------------------#

    #ISIN 1 eingeben und die Daten dazu bekommen
    # ETF 1 Daten scrapen und in Dictonary übertragen
    # Erst werden die Daten in ein gesammeltes Dictonary eingetragen und dann entsprechend der Werte aufgeteilt
  

response_1 = requests.get('https://api.zendepot.de/finance/etf/'+str(isin1), headers=headers)
data_1 = {"Countries": "", "Holdings": "", "Sectors": ""}
responseData_1 = response_1.json()
for scrapedData in responseData_1:
    data_1["Countries"] = response_1.json()["exposure"]["countries"]
    data_1["Holdings"] = response_1.json()["exposure"]["holdings"]
    data_1["Sectors"] = response_1.json()["exposure"]["sectors"]

for info_countries_1, info_sectors_1, info_holdings_1 in zip(data_1["Countries"], data_1["Sectors"], data_1["Holdings"]):
    ETF_countries_1[info_countries_1["name"]] = info_countries_1["percentage"]*100
    ETF_sectors_1[info_sectors_1["name"]] = info_sectors_1["percentage"]*100
    ETF_holdings_1[info_holdings_1["name"]] = info_holdings_1["percentage"]*100


#ISIN 2 eingeben und die Daten dazu bekommen 
# ETF 2 Daten scrapen und in Dictonary übertragen
# Erst werden die Daten in ein gesammeltes Dictonary eingetragen und dann entsprechend der Werte aufgeteilt

response_2 = requests.get('https://api.zendepot.de/finance/etf/'+str(isin2), headers=headers)
data_2 = {"Countries": "", "Holdings": "", "Sectors": ""}
responseData_2 = response_2.json()
for scrapedData in responseData_2:
    data_2["Countries"] = response_2.json()["exposure"]["countries"]
    data_2["Holdings"] = response_2.json()["exposure"]["holdings"]
    data_2["Sectors"] = response_2.json()["exposure"]["sectors"]

for info_countries_2, info_sectors_2, info_holdings_2 in zip(data_2["Countries"], data_2["Sectors"], data_2["Holdings"]):
    ETF_countries_2[info_countries_2["name"]] = info_countries_2["percentage"]*100
    ETF_sectors_2[info_sectors_2["name"]] = info_sectors_2["percentage"]*100
    ETF_holdings_2[info_holdings_2["name"]] = info_holdings_2["percentage"]*100

# Nur als Beispiel / Info ETF_countries_1 = 
# {'US': 68.56, 'JP': 6.03, 'other': 5.9, 'GB': 4.25, 'CA': 3.47, 'FR': 3.27, 'CH': 2.81, 'DE': 2.27, 'AU': 2.22, 'NL': 1.24}

# Werte der beiden ETFs zusammenrechnen

# 1. Gewichtung bestimmen

Summe_Depot = float(amount1) + float(amount2)

percent_ETF_1 = float(amount1)/Summe_Depot
percent_ETF_2 = float(amount2)/Summe_Depot

# Neue Listen definieren

# ETF 1
ETF_countries_1_weight = {}
ETF_sectors_1_weight = {}
ETF_holdings_1_weight = {}

# ETF 2
ETF_countries_2_weight = {}
ETF_sectors_2_weight = {}
ETF_holdings_2_weight = {}

# Werte ausrechnen und in neue Liste überführen

# ETF_1_weight
for info_countries_1, info_sectors_1, info_holdings_1 in zip(data_1["Countries"], data_1["Sectors"], data_1["Holdings"]):
    ETF_countries_1_weight[info_countries_1["name"]] = info_countries_1["percentage"]*100*percent_ETF_1
    ETF_sectors_1_weight[info_sectors_1["name"]] = info_sectors_1["percentage"]*100*percent_ETF_1
    ETF_holdings_1_weight[info_holdings_1["name"]] = info_holdings_1["percentage"]*100*percent_ETF_1

# ETF_2_weight
for info_countries_2, info_sectors_2, info_holdings_2 in zip(data_2["Countries"], data_2["Sectors"], data_2["Holdings"]):
    ETF_countries_2_weight[info_countries_2["name"]] = info_countries_2["percentage"]*100*percent_ETF_2
    ETF_sectors_2_weight[info_sectors_2["name"]] = info_sectors_2["percentage"]*100*percent_ETF_2
    ETF_holdings_2_weight[info_holdings_2["name"]] = info_holdings_2["percentage"]*100*percent_ETF_2

#-------------------------------------------------------------------Background---------------------------------------#
#Absatz einfügen
st.markdown('')

# Überschrift erste Ländertabelle

st.write("""
### Country distribution of your first ETF:
""")
with st.expander("Click to expand the table" ):
    st.table(data_1["Countries"])

with st.expander("Click to expand the bar chart" ):
    st.bar_chart(data_1["Countries"], x="name", y= "percentage", width=1, height=0, use_container_width=True)

#-------------------------------------------------------------------------------------------------------------------#

# Überschrift zweite Ländertabelle

st.write("""
### Country distribution of your second ETF:
""")
with st.expander("Click to expand the table" ):
    st.table(data_2["Countries"])

with st.expander("Click to expand bar chart" ):    
    st.bar_chart(data_2["Countries"], x="name", y= "percentage", width=1, height=0, use_container_width=True)


#-------------------------------------------------------------------------------------------------------------------#

# Überschrift für das erstellte Portfolio

st.write("""
### Distribution of your ETF Portfolio:
""")

#-------------------------------------------------------------------------------------------------------------------#

# Neue Listen zusammenrechnen

# In Worten:
# 1. Finale Liste definieren
# 2. For Schleife für jedes Element in Liste 1
# 3. If Key schon im Dictionary, addiere es zu bestehendem Wert
# 4. Andernfalls, füge sie so der Liste zu


# Listen und Finales Depot definieren
# Listen
ETF_countries_list = [ETF_countries_1_weight, ETF_countries_2_weight]
ETF_sectors_list = [ETF_sectors_1_weight, ETF_sectors_2_weight]
ETF_holdings_list = [ETF_holdings_1_weight, ETF_holdings_2_weight]

#Depot
Depot_countries_sum = {}
Depot_sectors_sum = {}
Depot_holdings_sum = {}


# For Schleifen um Werte einzufügen

# Countries
# iterate etfs
for ETF_countries in ETF_countries_list:
    # iterate countries
    for country in ETF_countries.keys():
        if country not in Depot_countries_sum.keys():
            # add key and value to sum dict
            Depot_countries_sum[country] = ETF_countries[country]
        else:
            # add value to existing key
            Depot_countries_sum[country] += ETF_countries[country]

# Sectors
# iterate etfs
for ETF_sectors in ETF_sectors_list:
    # iterate sectors
    for sector in ETF_sectors.keys():
        if sector not in Depot_sectors_sum.keys():
            # add key and value to sum dict
            Depot_sectors_sum[sector] = ETF_sectors[sector]
        else:
            # add value to existing key
            Depot_sectors_sum[sector] += ETF_sectors[sector]


# Sectors
# iterate etfs
for ETF_holdings in ETF_holdings_list:
    # iterate sectors
    for holding in ETF_holdings.keys():
        if holding not in Depot_holdings_sum.keys():
            # add key and value to sum dict
            Depot_holdings_sum[holding] = ETF_holdings[holding]
        else:
            # add value to existing key
            Depot_holdings_sum[holding] += ETF_holdings[holding]


#-------------------------------------------------------------------------------------------------------------------#

# Daten des Portfolios ausgeben 


st.write("""
#### Countries:
""")

Depot_countries_df = pd.DataFrame.from_dict(Depot_countries_sum, orient='index')

with st.expander("Click to expand" ):
    #st.write(Depot_countries_sum)
    st.table(Depot_countries_df)
    
# Only show autopct labels for percentages greater than or equal to 1%
def my_autopct(pct):
    if pct >= 1:
        return '%1.1f%%' % pct
    else:
        return ''

# Create a pie chart of the Country Dict
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.pie(Depot_countries_sum.values(), labels= None , autopct=my_autopct, pctdistance=0.83, labeldistance=1.3, textprops={'color':'black'} , shadow=False, startangle=90)

# Add a legend
plt.legend(Depot_countries_sum.keys(), title="Countries" , prop={'size': 4})

# Display the pie chart in the app
with st.expander("Click to expand the pie chart" ):
    st.pyplot()


#-------------------------------------------------------------------------------------------------------------------#

# Verrechnete Liste (Depot Verteilung der Sektoren)
st.write("""
#### Sectors:
""")

Depot_sectors_df = pd.DataFrame.from_dict(Depot_sectors_sum, orient='index')

with st.expander("Click to expand" ):
    #st.write(Depot_sectors_sum)
    st.table(Depot_sectors_df)

# Only show autopct labels for percentages greater than or equal to 1%
def my_autopct(pct):
    if pct >= 1:
        return '%1.1f%%' % pct
    else:
        return ''

# Create a pie chart of the Sectors Dict
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.pie(Depot_sectors_sum.values(), labels=Depot_sectors_sum.keys(), autopct=my_autopct)

# Display the pie chart in the app
with st.expander("Click to expand the pie chart" ):
    st.pyplot()

#---------------------------------------------------------------------------------------------------------------------#

# Verrechnete Liste (Depot Verteilung der Holdings)
st.write("""
#### Holdings:
""")

Depot_holdings_df = pd.DataFrame.from_dict(Depot_holdings_sum, orient='index')

with st.expander("Click to expand" ):
    #st.write(Depot_holdings_sum)
    st.table(Depot_holdings_df)
    
# Create a pie chart of the Sectors Dict
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.pie(Depot_holdings_sum.values(), labels=Depot_holdings_sum.keys())

# Display the pie chart in the app
with st.expander("Click to expand the pie chart" ):
    st.pyplot()

#---------------------------------------------------------------------------------------------------------------------#

# Ab hier reiner Test um später eine Weltkarte zu erstellen ( macht aber Vicent noch besser :) )

import pydeck as pdk

# Dictionary with data
data = {
  "US": 47.53699999999999,
  "JP": 4.34,
  "other": 6.384,
  "GB": 3.0309999999999997,
  "CA": 2.38,
  "FR": 2.3310000000000004,
  "CH": 2.009,
  "DE": 1.603,
  "AU": 1.5819999999999999,
  "NL": 0.8819999999999999,
  "CN": 9.549,
  "IN": 4.389,
  "TW": 4.326,
  "KR": 3.4739999999999998,
  "ZA": 1.068,
  "BR": 0.9089999999999999,
  "SA": 0.9089999999999999,
  "MX": 0.6809999999999999,
  "TH": 0.63
}

# Create a list of dictionaries with the data for each country
#countries = [{'code': code, 'value': value} for code, value in data.items()]

#---------------------------------------------------------------------------------------------------------------------#
#Länder Dict der einflussreichsten Länder 
countries = {
    "US": {"latitude": 37.09024, "longitude": -95.712891},
    "CA": {"latitude": 56.130366, "longitude": -106.346771},
    "MX": {"latitude": 23.634501, "longitude": -102.552784},
    "BR": {"latitude": -14.235004, "longitude": -51.92528},
    "AR": {"latitude": -38.416097, "longitude": -63.616672},
    "CO": {"latitude": 4.570868, "longitude": -74.297333},
    "PE": {"latitude": -9.189967, "longitude": -75.015152},
    "CL": {"latitude": -35.675147, "longitude": -71.542969},
    "EC": {"latitude": -1.831239, "longitude": -78.183406},
    "VE": {"latitude": 6.42375, "longitude": -66.58973},
    "BO": {"latitude": -16.290154, "longitude": -63.588653},
    "PY": {"latitude": -23.442503, "longitude": -58.443832},
    "UY": {"latitude": -32.522779, "longitude": -55.765835},
    "CN": {"latitude": 35.86166, "longitude": 104.195397},
    "IN": {"latitude": 20.593684, "longitude": 78.96288},
    "PK": {"latitude": 30.375321, "longitude": 69.345116},
    "BD": {"latitude": 23.684994, "longitude": 90.356331},
    "JP": {"latitude": 36.204824, "longitude": 138.252924},
    "RU": {"latitude": 61.52401, "longitude": 105.318756},
    "DE": {"latitude": 51.165691, "longitude": 10.451526},
    "FR": {"latitude": 46.227638, "longitude": 2.213749},
    "IT": {"latitude": 41.87194, "longitude": 12.56738},
    "ES": {"latitude": 40.463667, "longitude": -3.74922},
    "GB": {"latitude": 55.378051, "longitude": -3.435973},
    "IE": {"latitude": 53.41291, "longitude": -8.24389},
    "PT": {"latitude": 39.399872, "longitude": -8.224454},
    "NL": {"latitude": 52.132633, "longitude": 5.291266},
    "BE": {"latitude": 50.503887, "longitude": 4.469936},
    "LU": {"latitude": 49.815273, "longitude": 6.129583},
}

#---------------------------------------------------------------------------------------------------------------------#

# Create the map

countries1 = [{'latitude': value, 'longitude': value2 } for value, value2 in countries.items()]
map = pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state={
        'latitude': 37.76,
        'longitude': -122.4,
        'zoom': 2,
        'pitch': 0,
    },
    layers=[
        pdk.Layer(
            'GeoJsonLayer',
            #data=countries,
            get_fill_color=[255, 0, 0],
            auto_highlight=True,
            pickable=True
        ),
    ],
)

# Display the map in the app
st.pydeck_chart(map)

#You can customize the appearance and behavior of the map using various options provided by the pydeck library. 
#For example, you can use the get_fill_color argument to specify the color for each country based on the data, the auto_highlight argument to control whether the countries are highlighted when the user hovers over them, or the pickable argument to control whether the user can click on the countries to trigger an event.


#---------------------------------------------------------------------------------------------------------------------#
