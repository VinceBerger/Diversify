import yfinance as yf
import streamlit as st

# Logo einfügen
from PIL import Image
image = Image.open('Diversify_Logo.png')

st.image(image)


# Überschrift
st.write("""
#  **How diversified is your ETF portfolio?**
### Now choose which ETFs you have in your portfolio!
""")

# ETFs auswählen
title = st.text_input('Type in the ETF WKN (for example "A0RPWH" for the iShares Core MSCI World UCITS ETF)', 'A0RPWH')
amount = st.text_input('Type in the amount of money (in €), you are invested in this specific ETF', '5.000')

#Ticker Symbol eingeben und die Daten dazu bekommen 
tickerData = yf.Ticker(title)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits



# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#tickerSymbol = 'GOOGL'
#get data on this ticker
#tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
#tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)