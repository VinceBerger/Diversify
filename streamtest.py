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

# ETF 1 auswählen
title = st.text_input('Type in the ETF ISIN (for example "IE00B4L5Y983" for the iShares Core MSCI World UCITS ETF)', 'IE00B4L5Y983')
amount = st.text_input('Type in the amount of money (in $), you are invested in this specific ETF', '7.000')

# ETF 2 auswählen
title2 = st.text_input('Type in the ETF ISIN (for example "IE00B0M63177" for the iShares MSCI EM UCITS ETF USD)', 'IE00B0M63177')
amount2 = st.text_input('Type in the amount of money (in $), you are invested in this specific ETF', '3.000')


#Ticker Symbol eingeben und die Daten dazu bekommen 
tickerData = yf.Ticker(title)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Zusammensetzung des ETFs (Top 10 Positionen) -- muss noch bearbeitet werden 
tickerHolding = tickerData.get_major_holders()
st.bar_chart(tickerHolding)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75


st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)