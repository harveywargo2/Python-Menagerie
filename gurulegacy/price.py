import requests
import pandas as pd
from datetime import date


def io(ticker: str, token: str):
    return requests.get('https://api.gurufocus.com/public/user/' + token + '/stock/' + ticker + '/price').json()


def to_df(ticker: str, token: str):
    price_list = io(ticker, token)
    price_df = pd.DataFrame(price_list, columns=['Date', 'SharePrice'])
    price_df['SharePrice'] = price_df['SharePrice'].astype(float)
    price_df['Date'] = pd.to_datetime(price_df['Date'])
    final_df = price_df.set_index('Date')
    return final_df


def to_csv(ticker: str, token: str):
    df = to_df(ticker, token)
    return df.to_csv(ticker.upper() + '-PriceData@' + str(date.today()) + '.csv')