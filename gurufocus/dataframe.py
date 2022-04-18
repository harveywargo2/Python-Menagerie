import requests
import pandas as pd


def annuals(ticker: str, token: str):
    fin_dict = requests.get('https://api.gurufocus.com/public/user/' + token + '/stock/' + ticker + '/financials').json()
    fin_df = pd.DataFrame.from_dict(fin_dict)
    init_df = pd.json_normalize(fin_df.loc['annuals'])

    ann_df = pd.DataFrame()
    x_loc = 0

    for item, values in init_df.iteritems():
        series_expand = pd.Series(values, name=item).explode(ignore_index=True)
        ann_df.insert(loc=x_loc, column=item, value=series_expand)
        x_loc += 1

    ann_df.convert_dtypes()
    df_indexed = ann_df.set_index('Fiscal Year')
    final_df = df_indexed.drop(index=['TTM'])
    return final_df


def dividend(ticker: str, token: str):
    div_list = requests.get('https://api.gurufocus.com/public/user/' + token + '/stock/' + ticker + '/dividend').json()
    div_df = pd.DataFrame(div_list)
    div_df['ex_date'] = pd.to_datetime(div_df['ex_date'])
    div_df['amount'] = div_df['amount'].astype(float)
    final_df = div_df.set_index('ex_date')
    return final_df


def price(ticker: str, token: str):
    price_list = requests.get('https://api.gurufocus.com/public/user/' + token + '/stock/' + ticker + '/price').json()
    price_df = pd.DataFrame(price_list, columns=['Date', 'SharePrice'])
    price_df['SharePrice'] = price_df['SharePrice'].astype(float)
    price_df['Date'] = pd.to_datetime(price_df['Date'])
    final_df = price_df.set_index('Date')
    return final_df


