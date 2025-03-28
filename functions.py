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
    stock['Return'] = stock['Close'].pct_change()
    stock['Cum_Return'] = stock['Close'].pct_change().cumsum()

    return stock

