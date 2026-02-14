import yfinance as yf
from modules.filter import passes_filter

symbols = [
    "INFY.NS",
    "RELIANCE.NS",
    "TCS.NS",
    "IRCTC.NS",
    "TATASTEEL.NS"
]

for symbol in symbols:
    stock = yf.Ticker(symbol)
    info = stock.info

    result = passes_filter(info, symbol)

    print(symbol, "PASS" if result else "FAIL")
