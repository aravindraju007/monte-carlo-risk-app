import yfinance as yf
import pandas_datareader.data as pdr
from datetime import date, timedelta

yf.pdr_override()

def fetch_stock_data(symbol, start=None, end=None):
    if not start:
        end = date.today()
        start = end - timedelta(days=3652)
    return pdr.get_data_yahoo(symbol, start=start, end=end)
