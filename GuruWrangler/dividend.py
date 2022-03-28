import requests
import pandas as pd
from datetime import date


def io(ticker: str, token: str):
    return requests.get('https://api.gurufocus.com/public/user/' + token + '/stock/' + ticker + '/dividend').json()


def to_df(ticker: str, token: str):
    div_list = io(ticker, token)
    div_df = pd.DataFrame(div_list)
    div_df['ex_date'] = pd.to_datetime(div_df['ex_date'])
    div_df['amount'] = div_df['amount'].astype(float)
    div_final_df = div_df.set_index('ex_date')
    return div_final_df


def to_csv(ticker: str, token: str):
    div_hist = to_df(ticker, token)
    return div_hist.to_csv(ticker.upper() + '-DividendData@' + str(date.today()) + '.csv')

