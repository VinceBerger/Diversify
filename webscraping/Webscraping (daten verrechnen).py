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

# For Schleife geht alle in CSV Datei gespeicherten ISINs durch

# for link in ISINs
#    response = requests 
# isins = ["isin1", "isin2"]
# for link in isins:
#   response = requests.get(f"https://api.zendepot.de/finance/etf/{link}")


ISIN = "LU0592215403"

response = requests.get('https://api.zendepot.de/finance/etf/'+str(ISIN), headers=headers)
data2 = {"Countries": "", "Holdings": "", "Sectors": ""}
responseData = response.json()
for scrapedData in responseData:
    data2["Countries"] = response.json()["exposure"]["countries"]
    data2["Holdings"] = response.json()["exposure"]["holdings"]
    data2["Sectors"] = response.json()["exposure"]["sectors"]


for info in data2["Countries"]: 
    print(info["name"], info["percentage"]*100)

#for info in data["Holdings"]: 
 #   print(info["name"], info["percentage"]*100)
    
#for info in data["Sectors"]: 
 #   print(info["name"], info["percentage"]*100)    

# %% [markdown]
# ## Länderverteilung eines ETFs

# %%
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


ISIN = "IE00B4L5Y983"

response = requests.get('https://api.zendepot.de/finance/etf/'+str(ISIN), headers=headers)
data = {"Countries": "", "Holdings": "", "Sectors": ""}
responseData = response.json()
for scrapedData in responseData:
    data["Countries"] = response.json()["exposure"]["countries"]
   # data["Holdings"] = response.json()["exposure"]["holdings"]
   # data["Sectors"] = response.json()["exposure"]["sectors"]


for info in data["Countries"]: 
    print(info["name"], info["percentage"]*100)

# %% [markdown]
# ## ETF Prozent Verteilung

# %%
x = 500
y= 10000

# Länderverteilung in ETF 1
for info in data["Countries"]:
    print(info["name"], x/(x+y)*info["percentage"]*100)
    
# Länderverteilung in ETF 2
for info in data2["Countries"]:
    print(info["name"], y/(x+y)*info["percentage"]*100)    

# %% [markdown]
# ## Test mehrere ISINs eingeben
# 

# %%
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


WKN = ["A0RPWH","A0MW0M"]
ISIN = ["IE00B4L5Y983","IE00B1XNHC34"]


for etf in ISIN:
    response = requests.get('https://api.zendepot.de/finance/etf/'+str(etf), headers=headers)
    data = {"Countries": "", "Holdings": "", "Sectors": ""}
    responseData = response.json()
    
    for scrapedData in responseData:
        data["Countries"] = response.json()["exposure"]["countries"]
        data["Holdings"] = response.json()["exposure"]["holdings"]
        data["Sectors"] = response.json()["exposure"]["sectors"]


for info in data["Countries"]: 
    print(info["name"], info["percentage"]*100)



# %%
ISIN = ["IE00B4L5Y983","IE00B1XNHC34","LU0592215403"]

for x in ISIN:
    print(x)


