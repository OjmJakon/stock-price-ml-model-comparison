import yfinance as yf

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

