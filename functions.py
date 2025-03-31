import yfinance as yf
import requests

def get_data(function: str, ticker, period: str, api_key: str):

    end_data_yf = dict()
    end_data_alpha = dict()
    if isinstance(ticker, list):
        for i in ticker:
            yf_ticker = yf.Ticker(i)
            data_yf = yf_ticker.history(period=period)
            end_data_yf[i] = data_yf
            if function and api_key:
                url = f'https://www.alphavantage.co/query?function={function}&symbol={i}&apikey={api_key}'
                r = requests.get(url)
                end_data_alpha[i] = r.json()
    else:
        yf_ticker = yf.Ticker(ticker)
        data_yf = yf_ticker.history(period=period)
        end_data_yf[ticker] = data_yf
        if function and api_key:
            url = f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}'
            r = requests.get(url)
            end_data_alpha[ticker] = r.json()

    return [end_data_yf, end_data_alpha]


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
