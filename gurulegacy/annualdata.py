import pandas as pd
import gurulegacy.annual
from datetime import date


def to_df(ticker: str, token: str):

    return data_df


def to_csv(ticker: str, token: str):
    data_df = to_df(ticker, token)
    return data_df.to_csv(ticker.upper() + '-AnnualData@' + str(date.today()) + '.csv')

