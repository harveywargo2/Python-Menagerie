import requests
import pandas as pd
from datetime import date


def io(ticker: str, token: str):
    return requests.get('https://api.gurufocus.com/public/user/' + token + '/stock/' + ticker + '/financials').json()


def to_df(ticker: str, token: str):
    fin_dict = io(ticker, token)
    fin_df = pd.DataFrame.from_dict(fin_dict)
    annuals = pd.json_normalize(fin_df.loc['annuals'])
    ann_df = pd.DataFrame()
    x_loc = 0

    for item, values in annuals.iteritems():
        series_expand = pd.Series(values, name=item).explode(ignore_index=True)
        ann_df.insert(loc=x_loc, column=item, value=series_expand)
        x_loc += 1

    ann_df.convert_dtypes()
    df_indexed = ann_df.set_index('Fiscal Year')
    return df_indexed


def to_csv(ticker: str, token: str):
    ann_df = to_df(ticker, token)
    return ann_df.to_csv(ticker.upper() + '-AnnualData@' + str(date.today()) + '.csv')