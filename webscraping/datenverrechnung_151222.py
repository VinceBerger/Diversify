# Zusammenrechnung der Depots mit Import



import requests

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

# Input:

# ETF_1
ISIN_1 = "IE00B4L5Y983"
Money_1 = 3000

# ETF_2
ISIN_2 = "IE00B0M63177"
Money_2 = 1000

# Outputformat bestimmen in Listen

# ETF 1
ETF_countries_1 = {}
ETF_sectors_1 = {}
ETF_holdings_1 = {}

# ETF 2
ETF_countries_2 = {}
ETF_sectors_2 = {}
ETF_holdings_2 = {}


# ETF 1 Daten scrapen und in Dictonary übertragen
# Erst werden die Daten in ein gesammeltes Dictonary eingetragen und dann entsprechend der Werte aufgeteilt#

response_1 = requests.get('https://api.zendepot.de/finance/etf/'+str(ISIN_1), headers=headers)
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

# ETF 2 Daten scrapen und in Dictonary übertragen
# Erst werden die Daten in ein gesammeltes Dictonary eingetragen und dann entsprechend der Werte aufgeteilt

response_2 = requests.get('https://api.zendepot.de/finance/etf/'+str(ISIN_2), headers=headers)
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


# Werte zusammenrechnen

# 1. Gewichtung bestimmen

Summe_Depot = Money_1 + Money_2

percent_ETF_1 = Money_1/Summe_Depot
percent_ETF_2 = Money_2/Summe_Depot

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


# Neue Listen zusammenrechnen

# In Worten:
# 1. Finale Liste definieren
# 2. For Scheleife für jedes Element in Liste 1
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




# Daten ausgeben

# Verrechnete Liste (Depot Verteilung)
print("Depot Verteilung")
print()
print("Countries:")
print(Depot_countries_sum)
print()
print("Sectors:")
print(Depot_sectors_sum)
print()
print("Holdings:")
print(Depot_holdings_sum)