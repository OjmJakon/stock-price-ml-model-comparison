import yfinance as yf
import requests

def get_data(ticker, period):

    end_data = dict()
    if isinstance(ticker, list):
        for i in ticker:
            ticker = yf.Ticker(i)
            data = ticker.history(period=period)
            end_data[i] = data
    else:
        data = ticker.history(period=period)
        end_data[ticker] = data

    return end_data


def generate_columns(stock):

    if isinstance(stock, dict):
        for i in stock.keys():
            stock[i]['Return'] = stock[i]['Close'].pct_change()
            stock[i]['Cum_Return'] = stock[i]['Close'].pct_change().cumsum()
    else:
        stock['Return'] = stock['Close'].pct_change()
        stock['Cum_Return'] = stock['Close'].pct_change().cumsum()

    return stock

def get_overview_data(ticker, API_KEY):
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + API_KEY
    r = requests.get(url)
    data = r.json()

    return data
