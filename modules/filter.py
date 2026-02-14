from datetime import datetime
import yfinance as yf

GOOD_SECTORS = [
    "Technology",
    "Healthcare",
    "Industrials",
    "Financial Services",
    "Consumer Defensive",
    "Energy"
]

MIN_MARKETCAP = 20000 * 10**7   # ₹20,000 Cr approx
MAX_DE = 0.3
MIN_ROE = 0.15
MIN_AGE = 15


def stock_age(symbol):
    data = yf.Ticker(symbol).history(period="max")
    if data.empty:
        return 0
    first_date = data.index[0].year
    return datetime.now().year - first_date


def passes_filter(info, symbol):

    if not info.get("marketCap") or info["marketCap"] < MIN_MARKETCAP:
        return False

    #if info.get("debtToEquity") and info["debtToEquity"] > MAX_DE:
    #    return False

    #if info.get("returnOnEquity") and info["returnOnEquity"] < MIN_ROE:
    #    return False

    if info.get("sector") not in GOOD_SECTORS:
        return False

    #if stock_age(symbol) < MIN_AGE:
    #    return False

    # crude PSU detection
    name = info.get("longName","").lower()
    if "government" in name or "india" in name and "corp" in name:
        return False

    return True
