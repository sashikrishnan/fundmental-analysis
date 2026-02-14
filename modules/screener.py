from modules.filter import passes_filter
import yfinance as yf

stock = yf.Ticker(symbol)
info = stock.info

if passes_filter(info, symbol):
    print(symbol, "PASSED")
