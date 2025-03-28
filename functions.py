def generate_columns(stock):
    stock['Return'] = stock['Close'].pct_change()
    stock['Cum_Return'] = stock['Close'].pct_change().cumsum()

    return stock

