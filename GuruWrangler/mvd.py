import pandas as pd
import annual
from datetime import date


def to_df(ticker: str, token: str):
    ann_df = annual.to_df(ticker, token)
    per_share_df = pd.DataFrame(index=ann_df.index)
    per_share_df['PriceLow'] = ann_df['valuation_and_quality.Lowest Stock Price'].astype(float)
    per_share_df['PriceHigh'] = ann_df['valuation_and_quality.Highest Stock Price'].astype(float)
    per_share_df['RPS'] = ann_df['per_share_data_array.Revenue per Share'].astype(float)
    per_share_df['FCF'] = ann_df['per_share_data_array.Free Cash Flow per Share'].astype(float)
    per_share_df['EPS'] = ann_df['per_share_data_array.Earnings per Share (Diluted)'].astype(float)
    per_share_df['DPS'] = ann_df['per_share_data_array.Dividends per Share'].astype(float)
    return per_share_df


def to_csv(ticker: str, token: str):
    ps_df = to_df(ticker, token)
    return ps_df.to_csv(ticker.upper() + '-EBondData@' + str(date.today()) + '.csv')

